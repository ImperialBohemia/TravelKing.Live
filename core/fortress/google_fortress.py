"""
GOOGLE FORTRESS — Permanent Google Connection via Service Account.

STRATEGY:
=========
Google OAuth user tokens (access_token + refresh_token) ALWAYS expire.
- Access tokens: 1 hour
- Refresh tokens: Can be revoked at any time, expire after 7 days
  if the OAuth app is in "Testing" mode in Google Cloud Console.

THE FIX: Use Google SERVICE ACCOUNT for everything server-side.
- Service Account tokens are generated FROM the private key.
- They NEVER expire because we generate them on-demand.
- No refresh tokens needed. No user login needed. PERMANENT.

What Service Account covers:
  ✅ Google Sheets (reading/writing)
  ✅ Google Drive (file management)
  ✅ Google Cloud APIs (AI, Monitoring, etc.)
  ✅ Gmail API (via domain-wide delegation or direct)

What still needs user OAuth (but we handle it smartly):
  ⚠️ Google Sites editing (no API — needs browser session)
  ⚠️ Google Ads (needs user consent — but tokens last longer in Production mode)

For user-OAuth services, we use a PROACTIVE REFRESH daemon.
"""

import json
import os
import sys
import time
import logging
from datetime import datetime

# Ensure project root in path
PROJECT_ROOT = "/home/q/TravelKing.Live"
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from core.fortress.token_vault import (
    load_vault, save_vault, update_google_token,
    get_token_age, get_service_account_path, load_token_cache, save_token_cache
)

logger = logging.getLogger("FORTRESS.Google")


class GoogleFortress:
    """Permanent Google connection management.
    
    Priority Order:
    1. Service Account (PERMANENT — for Sheets, Drive, Cloud)
    2. Proactive OAuth refresh (for user-level APIs)
    3. Gmail App Password (PERMANENT — for SMTP email)
    """
    
    SA_PATH = get_service_account_path()
    
    # Scopes for Service Account
    SA_SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/cloud-platform',
        'https://www.googleapis.com/auth/gmail.send',
    ]
    
    # Refresh user token every 45 minutes (tokens last 60 min)
    REFRESH_INTERVAL = 45 * 60  # seconds
    
    def __init__(self):
        self.vault = load_vault()
        self._sa_creds = None
        self._sheets_service = None
        self._drive_service = None
    
    # ─── SERVICE ACCOUNT (PERMANENT) ────────────────────────────
    
    def get_sa_credentials(self):
        """Get Service Account credentials. These NEVER expire."""
        if self._sa_creds is None:
            from google.oauth2 import service_account
            self._sa_creds = service_account.Credentials.from_service_account_file(
                self.SA_PATH, scopes=self.SA_SCOPES
            )
        return self._sa_creds
    
    def get_sheets_service(self):
        """Get Sheets API service (via Service Account — permanent)."""
        if self._sheets_service is None:
            from googleapiclient.discovery import build
            self._sheets_service = build('sheets', 'v4', credentials=self.get_sa_credentials())
        return self._sheets_service
    
    def get_drive_service(self):
        """Get Drive API service (via Service Account — permanent)."""
        if self._drive_service is None:
            from googleapiclient.discovery import build
            self._drive_service = build('drive', 'v3', credentials=self.get_sa_credentials())
        return self._drive_service
    
    def build_service(self, api_name: str, api_version: str):
        """Build any Google API service using Service Account."""
        from googleapiclient.discovery import build
        return build(api_name, api_version, credentials=self.get_sa_credentials())
    
    # ─── GMAIL (APP PASSWORD — PERMANENT) ───────────────────────
    
    def send_email(self, to: str, subject: str, body: str):
        """Send email via Gmail SMTP (App Password = permanent, no expiry)."""
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        email = self.vault['google']['account_email']
        password = self.vault['google']['app_password']
        
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as server:
            server.login(email, password)
            server.sendmail(email, to, msg.as_string())
        
        return True
    
    # ─── USER OAUTH (Proactive Refresh) ─────────────────────────
    
    def refresh_user_token(self) -> bool:
        """Refresh the user OAuth token proactively.
        
        Called by the daemon every 45 minutes to keep the token alive.
        """
        vault = load_vault()
        google = vault.get('google', {})
        
        refresh_token = google.get('refresh_token')
        client_id = google.get('client_id')
        client_secret = google.get('client_secret')
        
        if not all([refresh_token, client_id, client_secret]):
            logger.warning("Missing OAuth credentials for user token refresh.")
            return False
        
        try:
            from google.oauth2.credentials import Credentials
            from google.auth.transport.requests import Request
            
            creds = Credentials(
                token=google.get('access_token'),
                refresh_token=refresh_token,
                client_id=client_id,
                client_secret=client_secret,
                token_uri="https://oauth2.googleapis.com/token"
            )
            
            creds.refresh(Request())
            
            if creds.token:
                update_google_token(creds.token, source="fortress_proactive_refresh")
                logger.info(f"✅ Google user token refreshed: {creds.token[:20]}...")
                return True
                
        except Exception as e:
            error_msg = str(e)
            logger.error(f"❌ Google user token refresh failed: {error_msg}")
            
            # If invalid_grant — the refresh token itself is dead
            if "invalid_grant" in error_msg:
                logger.critical(
                    "🚨 REFRESH TOKEN IS DEAD. This happens when:\n"
                    "   1. OAuth app is in 'Testing' mode (tokens expire after 7 days)\n"
                    "   2. User revoked access\n"
                    "   3. Password was changed\n"
                    "   FIX: Publish the OAuth app to 'Production' in Google Cloud Console,\n"
                    "   then re-authorize once. After that, tokens last forever."
                )
                self._record_alert("google_oauth_dead", error_msg)
        
        return False
    
    def needs_refresh(self) -> bool:
        """Check if the user token needs refreshing."""
        age = get_token_age("google")
        return age > self.REFRESH_INTERVAL
    
    # ─── HEALTH CHECK ───────────────────────────────────────────
    
    def full_health_check(self) -> dict:
        """Complete health audit of all Google connections."""
        results = {}
        
        # 1. Service Account (permanent)
        try:
            sheets = self.get_sheets_service()
            sheet_id = self.vault['travelking']['sheet_id']
            meta = sheets.spreadsheets().get(spreadsheetId=sheet_id).execute()
            results['service_account'] = {
                'status': 'PERMANENT',
                'detail': f"Sheet: {meta['properties']['title']}",
                'expires': 'NEVER'
            }
        except Exception as e:
            results['service_account'] = {'status': 'ERROR', 'error': str(e)}
        
        # 2. Drive (permanent via SA)
        try:
            drive = self.get_drive_service()
            files = drive.files().list(pageSize=1).execute()
            results['drive'] = {
                'status': 'PERMANENT',
                'detail': f"{len(files.get('files', []))} files accessible",
                'expires': 'NEVER'
            }
        except Exception as e:
            results['drive'] = {'status': 'ERROR', 'error': str(e)}
        
        # 3. Gmail SMTP (permanent via App Password)
        try:
            import smtplib
            email = self.vault['google']['account_email']
            pwd = self.vault['google']['app_password']
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=5) as s:
                s.login(email, pwd)
            results['gmail_smtp'] = {
                'status': 'PERMANENT',
                'detail': email,
                'expires': 'NEVER (App Password)'
            }
        except Exception as e:
            results['gmail_smtp'] = {'status': 'ERROR', 'error': str(e)}
        
        # 4. User OAuth (needs refresh)
        try:
            token = self.vault['google'].get('access_token')
            if token:
                import requests
                r = requests.get(
                    "https://www.googleapis.com/oauth2/v3/tokeninfo",
                    params={"access_token": token}, timeout=5
                )
                if r.status_code == 200:
                    info = r.json()
                    results['user_oauth'] = {
                        'status': 'ACTIVE',
                        'detail': info.get('email', 'unknown'),
                        'expires_in': f"{int(info.get('expires_in', 0))}s"
                    }
                else:
                    age = get_token_age("google")
                    results['user_oauth'] = {
                        'status': 'EXPIRED',
                        'age': f"{age/3600:.1f}h",
                        'action': 'Will auto-refresh on next daemon cycle'
                    }
            else:
                results['user_oauth'] = {'status': 'NOT_CONFIGURED'}
        except Exception as e:
            results['user_oauth'] = {'status': 'ERROR', 'error': str(e)}
        
        return results
    
    def _record_alert(self, alert_type: str, message: str):
        """Record critical alert for dashboard."""
        alert_path = "/home/q/TravelKing.Live/data/logs/fortress_alerts.jsonl"
        os.makedirs(os.path.dirname(alert_path), exist_ok=True)
        with open(alert_path, "a") as f:
            f.write(json.dumps({
                "ts": datetime.now().isoformat(),
                "type": alert_type,
                "message": message
            }) + "\n")
