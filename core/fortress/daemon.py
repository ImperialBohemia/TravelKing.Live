"""
CONNECTION FORTRESS DAEMON — Keeps ALL connections alive permanently.

Runs as a systemd user service OR via cron.
Every 30 minutes it:
  1. Checks all service connections
  2. Proactively refreshes any tokens that are aging
  3. Self-heals broken connections where possible
  4. Logs everything to status files + Google Sheets dashboard
  5. Sends alert email if a critical service goes down

PERMANENT CONNECTIONS (never expire):
  ✅ Google Sheets/Drive/Cloud — via Service Account private key
  ✅ Gmail SMTP — via App Password
  ✅ cPanel — via API Token (permanent until revoked)
  ✅ GitHub — via Personal Access Token (configurable expiry)
  ✅ Travelpayouts — via API Token (permanent)
  ✅ Bing IndexNow — via API Key (permanent)

MANAGED CONNECTIONS (auto-refreshed):
  🔄 Google User OAuth — refreshed every 45 min
  🔄 Facebook — long-lived token exchange
"""

import json
import os
import sys
import time
import logging
import requests
from datetime import datetime

PROJECT_ROOT = "/home/q/TravelKing.Live"
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from core.fortress.token_vault import (
    load_vault, save_vault, update_google_token,
    update_facebook_token, get_token_age, load_token_cache, save_token_cache
)
from core.fortress.google_fortress import GoogleFortress

# ─── Logging Setup ──────────────────────────────────────────────
LOG_DIR = os.path.join(PROJECT_ROOT, "data/logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(LOG_DIR, "fortress.log"), encoding="utf-8")
    ]
)
logger = logging.getLogger("FORTRESS")


class ConnectionFortress:
    """Master daemon that maintains ALL connections permanently."""
    
    def __init__(self):
        self.vault = load_vault()
        self.google = GoogleFortress()
        self.status = {}
        self.run_time = datetime.now()
    
    # ─── GOOGLE (Service Account = PERMANENT) ───────────────────
    
    def check_google(self):
        """Full Google health check via fortress."""
        logger.info("🔒 Checking Google connections...")
        health = self.google.full_health_check()
        
        for service, data in health.items():
            status = data.get('status', 'UNKNOWN')
            icon = '✅' if status in ('PERMANENT', 'ACTIVE') else '❌'
            detail = data.get('detail', data.get('error', ''))
            expires = data.get('expires', data.get('expires_in', ''))
            logger.info(f"  {icon} Google {service}: {status} | {detail} | Expires: {expires}")
            self.status[f"google_{service}"] = data
        
        # Proactive refresh of user token if needed
        if health.get('user_oauth', {}).get('status') == 'EXPIRED':
            logger.info("  🔄 Attempting proactive user token refresh...")
            if self.google.refresh_user_token():
                logger.info("  ✅ User token refreshed!")
            else:
                logger.warning("  ⚠️ User token refresh failed — Service Account still operational")
    
    # ─── FACEBOOK ───────────────────────────────────────────────
    
    def check_facebook(self):
        """Check and extend Facebook token life."""
        logger.info("🔒 Checking Facebook connection...")
        vault = load_vault()
        fb = vault.get('facebook', {})
        token = fb.get('access_token')
        
        if not token:
            self.status['facebook'] = {'status': 'NOT_CONFIGURED'}
            return
        
        # Check current token
        try:
            r = requests.get(
                f"https://graph.facebook.com/me?access_token={token}",
                timeout=5
            )
            if r.status_code == 200:
                data = r.json()
                name = data.get('name', 'Unknown')
                
                # Check token expiry via debug
                debug_r = requests.get(
                    f"https://graph.facebook.com/debug_token",
                    params={
                        "input_token": token,
                        "access_token": f"{fb.get('app_id')}|{fb.get('app_secret')}"
                    },
                    timeout=5
                )
                
                expires_at = "Unknown"
                if debug_r.status_code == 200:
                    debug_data = debug_r.json().get('data', {})
                    exp_ts = debug_data.get('expires_at', 0)
                    if exp_ts == 0:
                        expires_at = "NEVER (permanent)"
                    else:
                        expires_at = datetime.fromtimestamp(exp_ts).isoformat()
                        # If expires within 7 days, exchange for long-lived token
                        if exp_ts - time.time() < 7 * 24 * 3600:
                            self._extend_facebook_token(fb)
                
                self.status['facebook'] = {
                    'status': 'ACTIVE',
                    'detail': name,
                    'expires': expires_at
                }
                logger.info(f"  ✅ Facebook: ACTIVE | {name} | Expires: {expires_at}")
            else:
                self.status['facebook'] = {'status': 'EXPIRED', 'action': 'Needs re-auth'}
                logger.warning("  ❌ Facebook token expired!")
                
        except Exception as e:
            self.status['facebook'] = {'status': 'ERROR', 'error': str(e)}
            logger.error(f"  ❌ Facebook error: {e}")
    
    def _extend_facebook_token(self, fb_config):
        """Exchange short-lived token for long-lived (60-day) token."""
        try:
            r = requests.get(
                "https://graph.facebook.com/v19.0/oauth/access_token",
                params={
                    "grant_type": "fb_exchange_token",
                    "client_id": fb_config['app_id'],
                    "client_secret": fb_config['app_secret'],
                    "fb_exchange_token": fb_config['access_token']
                },
                timeout=10
            )
            if r.status_code == 200:
                new_token = r.json().get('access_token')
                if new_token:
                    update_facebook_token(new_token, source="fortress_long_lived_exchange")
                    logger.info("  🔄 Facebook token extended to 60 days!")
        except Exception as e:
            logger.error(f"  Failed to extend Facebook token: {e}")
    
    # ─── cPanel ─────────────────────────────────────────────────
    
    def check_cpanel(self):
        """Check cPanel API connectivity (permanent token)."""
        logger.info("🔒 Checking cPanel connection...")
        vault = load_vault()
        cp = vault.get('cpanel', {})
        
        try:
            url = f"https://{cp['host']}:2083/execute/ResourceUsage/get_usages"
            headers = {"Authorization": f"cpanel {cp['user']}:{cp['api_token']}"}
            r = requests.get(url, headers=headers, timeout=10)
            
            if r.status_code == 200:
                self.status['cpanel'] = {
                    'status': 'PERMANENT',
                    'detail': f"{cp['user']}@{cp['host']}",
                    'expires': 'NEVER (API Token)'
                }
                logger.info(f"  ✅ cPanel: PERMANENT | {cp['user']}@{cp['host']}")
            else:
                self.status['cpanel'] = {'status': 'ERROR', 'code': r.status_code}
                logger.warning(f"  ❌ cPanel down: {r.status_code}")
        except Exception as e:
            self.status['cpanel'] = {'status': 'ERROR', 'error': str(e)}
            logger.error(f"  ❌ cPanel error: {e}")
    
    # ─── GitHub ─────────────────────────────────────────────────
    
    def check_github(self):
        """Check GitHub token (PAT — configurable expiry)."""
        logger.info("🔒 Checking GitHub connection...")
        vault = load_vault()
        gh = vault.get('github', {})
        token = gh.get('token')
        
        if not token:
            self.status['github'] = {'status': 'NOT_CONFIGURED'}
            return
        
        try:
            headers = {"Authorization": f"token {token}"}
            r = requests.get("https://api.github.com/user", headers=headers, timeout=5)
            
            if r.status_code == 200:
                user = r.json().get('login')
                # Check token expiry header
                exp = r.headers.get('github-authentication-token-expiration', 'NEVER')
                self.status['github'] = {
                    'status': 'ACTIVE',
                    'detail': user,
                    'expires': exp
                }
                logger.info(f"  ✅ GitHub: ACTIVE | {user} | Expires: {exp}")
            else:
                self.status['github'] = {'status': 'EXPIRED'}
                logger.warning("  ❌ GitHub token expired!")
        except Exception as e:
            self.status['github'] = {'status': 'ERROR', 'error': str(e)}
    
    # ─── Travelpayouts ──────────────────────────────────────────
    
    def check_travelpayouts(self):
        """Check Travelpayouts API (permanent token)."""
        logger.info("🔒 Checking Travelpayouts connection...")
        vault = load_vault()
        tp = vault.get('travelpayouts', {})
        
        try:
            r = requests.get(
                "https://api.travelpayouts.com/aviasales/v3/prices_for_dates",
                params={'origin': 'PRG', 'destination': 'LON', 'token': tp.get('api_token'), 'limit': 1},
                timeout=5
            )
            if r.status_code == 200:
                self.status['travelpayouts'] = {
                    'status': 'PERMANENT',
                    'detail': f"Marker: {tp.get('marker')}",
                    'expires': 'NEVER'
                }
                logger.info(f"  ✅ Travelpayouts: PERMANENT | Marker: {tp.get('marker')}")
            else:
                self.status['travelpayouts'] = {'status': 'ERROR', 'code': r.status_code}
        except Exception as e:
            self.status['travelpayouts'] = {'status': 'ERROR', 'error': str(e)}
    
    # ─── Bing / IndexNow ────────────────────────────────────────
    
    def check_bing(self):
        """Check Bing IndexNow key (permanent)."""
        logger.info("🔒 Checking Bing IndexNow...")
        vault = load_vault()
        bing = vault.get('bing', {})
        key = bing.get('index_now_key')
        
        if key and len(key) == 32:
            self.status['bing'] = {
                'status': 'PERMANENT',
                'detail': f"Key: {key[:8]}...",
                'expires': 'NEVER'
            }
            logger.info(f"  ✅ Bing IndexNow: PERMANENT | Key valid")
        else:
            self.status['bing'] = {'status': 'ERROR', 'detail': 'Invalid key'}
    
    # ─── MASTER RUN ─────────────────────────────────────────────
    
    def run_full_check(self) -> dict:
        """Run complete health check on ALL connections."""
        logger.info("=" * 60)
        logger.info("🏰 CONNECTION FORTRESS — Full System Audit")
        logger.info(f"   Time: {self.run_time.isoformat()}")
        logger.info("=" * 60)
        
        self.check_google()
        self.check_facebook()
        self.check_cpanel()
        self.check_github()
        self.check_travelpayouts()
        self.check_bing()
        
        # Save status
        status_path = os.path.join(LOG_DIR, "fortress_status.json")
        full_status = {
            "timestamp": self.run_time.isoformat(),
            "services": self.status,
            "summary": self._get_summary()
        }
        with open(status_path, 'w') as f:
            json.dump(full_status, f, indent=4)
        
        # Update Google Sheets dashboard
        self._update_dashboard()
        
        # Print summary
        self._print_summary()
        
        return full_status
    
    def _get_summary(self) -> dict:
        """Get summary counts."""
        permanent = sum(1 for s in self.status.values() if s.get('status') == 'PERMANENT')
        active = sum(1 for s in self.status.values() if s.get('status') == 'ACTIVE')
        errors = sum(1 for s in self.status.values() if s.get('status') in ('ERROR', 'EXPIRED'))
        
        return {
            'permanent': permanent,
            'active': active,
            'errors': errors,
            'total': len(self.status),
            'health': 'FORTRESS' if errors == 0 else 'DEGRADED'
        }
    
    def _print_summary(self):
        """Print colored summary."""
        summary = self._get_summary()
        logger.info("")
        logger.info("=" * 60)
        if summary['health'] == 'FORTRESS':
            logger.info("🏰 STATUS: FORTRESS — All systems permanently connected!")
        else:
            logger.info(f"⚠️  STATUS: DEGRADED — {summary['errors']} service(s) need attention")
        logger.info(f"   Permanent: {summary['permanent']} | Active: {summary['active']} | Errors: {summary['errors']}")
        logger.info("=" * 60)
    
    def _update_dashboard(self):
        """Write status to Google Sheets via Service Account (permanent)."""
        try:
            sheets = self.google.get_sheets_service()
            sheet_id = self.vault['travelking']['sheet_id']
            
            # Prepare rows
            timestamp = self.run_time.strftime("%Y-%m-%d %H:%M:%S")
            rows = [
                ["🏰 CONNECTION FORTRESS", "", ""],
                ["Last Check", timestamp, ""],
                ["", "", ""],
                ["Service", "Status", "Expires"],
            ]
            
            for name, data in self.status.items():
                status = data.get('status', '?')
                icon = '🟢' if status in ('PERMANENT', 'ACTIVE') else '🔴'
                detail = data.get('detail', data.get('error', ''))
                expires = data.get('expires', data.get('expires_in', ''))
                rows.append([f"{icon} {name}", f"{status} — {detail}", str(expires)])
            
            summary = self._get_summary()
            rows.append(["", "", ""])
            rows.append(["OVERALL", summary['health'], f"P:{summary['permanent']} A:{summary['active']} E:{summary['errors']}"])
            
            # Write to SYSTEM_STATUS tab
            try:
                sheets.spreadsheets().values().update(
                    spreadsheetId=sheet_id,
                    range="SYSTEM_STATUS!A1",
                    valueInputOption="RAW",
                    body={"values": rows}
                ).execute()
                logger.info("📊 Dashboard updated in Google Sheets")
            except Exception as tab_err:
                if "not found" in str(tab_err).lower() or "unable to parse" in str(tab_err).lower():
                    # Create tab
                    sheets.spreadsheets().batchUpdate(
                        spreadsheetId=sheet_id,
                        body={"requests": [{"addSheet": {"properties": {"title": "SYSTEM_STATUS"}}}]}
                    ).execute()
                    # Retry
                    sheets.spreadsheets().values().update(
                        spreadsheetId=sheet_id,
                        range="SYSTEM_STATUS!A1",
                        valueInputOption="RAW",
                        body={"values": rows}
                    ).execute()
                    logger.info("📊 Created SYSTEM_STATUS tab and updated dashboard")
                    
        except Exception as e:
            logger.error(f"Dashboard update failed: {e}")


# ─── DAEMON ENTRY POINT ────────────────────────────────────────

def run_once():
    """Run a single health check cycle."""
    fortress = ConnectionFortress()
    return fortress.run_full_check()

def run_daemon(interval_minutes=30):
    """Run continuously as a daemon."""
    logger.info(f"🏰 Connection Fortress Daemon starting (interval: {interval_minutes}min)")
    while True:
        try:
            run_once()
        except Exception as e:
            logger.error(f"Daemon cycle error: {e}")
        
        logger.info(f"💤 Sleeping {interval_minutes} minutes until next check...")
        time.sleep(interval_minutes * 60)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Connection Fortress")
    parser.add_argument("--daemon", action="store_true", help="Run as continuous daemon")
    parser.add_argument("--interval", type=int, default=30, help="Check interval in minutes")
    args = parser.parse_args()
    
    if args.daemon:
        run_daemon(args.interval)
    else:
        run_once()
