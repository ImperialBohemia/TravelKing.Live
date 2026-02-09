
import json
import os
import requests
import sys
import time
import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime
from loguru import logger

class Guardian:
    """Enterprise-grade monitor & self-healing service for TravelKing.Live."""
    
    def __init__(self, root_dir="/home/q/TravelKing.Live"):
        self.root = root_dir
        if self.root not in sys.path:
            sys.path.append(self.root)
        self.config_dir = os.path.join(self.root, "data/config")
        self.vault_path = os.path.join(self.root, "config/access_vault.json")
        self.google_auth_path = os.path.join(self.config_dir, "google_auth.json")
        self.status_path = os.path.join(self.root, "data/logs/guardian_status.json")

    def perform_health_check(self):
        """Deep Audit of ALL enterprise connections."""
        logger.info("🛡️ Guardian: Initiating FULL OMEGA AUDIT...")
        
        with open(self.vault_path, "r") as f:
            vault = json.load(f)

        results = {
            "timestamp": time.time(),
            "services": {
                "google_ai": self._check_google_ai(),
                "google_drive": self._check_google_drive(),
                "google_sheets": self._check_google_sheets(vault),
                "gmail": self._check_gmail(vault),
                "cpanel": self._check_cpanel(vault),
                "facebook": self._check_facebook(vault),
                "travelpayouts": self._check_travelpayouts(vault),
                "github": self._check_github(vault),
                "bing": self._check_bing(vault)
            }
        }
        
        # Save status for Dashboard integration
        with open(self.status_path, "w") as f:
            json.dump(results, f, indent=4)
        
        # Autonomous Update to Google Sheet
        try:
            self.update_dashboard(results)
        except Exception as e:
            logger.error(f"Failed to update Google Sheet: {e}")
            
        logger.success("🛡️ Guardian: Full System Audit + Dashboard Update Complete.")
        return results

    def update_dashboard(self, results):
        """Pushes health status to the specialized SYSTEM_STATUS tab."""
        # Load Vault for Sheet ID
        with open(self.vault_path, "r") as f:
            vault = json.load(f)
        
        sheet_id = vault['travelking']['sheet_id']
        sa_path = os.path.join(self.root, "config/service_account.json")
        
        creds = service_account.Credentials.from_service_account_file(
            sa_path, scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        service = build('sheets', 'v4', credentials=creds)
        
        # 1. Update Main Dashboard Cell (B2)
        # Check if "Dashboard" tab exists, create if not
        sheet_metadata = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
        sheets = sheet_metadata.get('sheets', '')
        titles = [s.get("properties", {}).get("title") for s in sheets]
        
        if "Dashboard" not in titles:
            req = {"addSheet": {"properties": {"title": "Dashboard", "index": 0}}}
            service.spreadsheets().batchUpdate(spreadsheetId=sheet_id, body={"requests": [req]}).execute()
            # Initialize Dashboard Layout
            service.spreadsheets().values().update(
                spreadsheetId=sheet_id, range="Dashboard!A1:B1",
                valueInputOption="RAW", body={"values": [["TRAVELKING ENTERPRISE STATUS", ""]]}
            ).execute()

        overall_status = "🟢 ALL SYSTEMS OPERATIONAL"
        for s in results['services'].values():
            if s['status'] != 'PERFECT':
                overall_status = "🔴 SYSTEM ATTENTION REQUIRED"
                break
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Batch Update for Dashboard
        body_dashboard = {
            "values": [[overall_status], [f"Last Check: {timestamp}"]]
        }
        service.spreadsheets().values().update(
            spreadsheetId=sheet_id, range="Dashboard!B2:B3",
            valueInputOption="RAW", body=body_dashboard
        ).execute()

        # 2. Log Detailed History to SYSTEM_STATUS Tab
        if "SYSTEM_STATUS" not in titles:
            req = {"addSheet": {"properties": {"title": "SYSTEM_STATUS"}}}
            service.spreadsheets().batchUpdate(spreadsheetId=sheet_id, body={"requests": [req]}).execute()
            # Add Header
            header = [["Timestamp", "Service", "Status", "Details"]]
            service.spreadsheets().values().update(
                spreadsheetId=sheet_id, range="SYSTEM_STATUS!A1:D1",
                valueInputOption="RAW", body={"values": header}
            ).execute()
            
        # Prepare Rows
        rows = []
        for name, data in results['services'].items():
            rows.append([
                timestamp, 
                name, 
                data['status'], 
                str(data.get('details', data.get('user', '')))
            ])
            
        service.spreadsheets().values().append(
            spreadsheetId=sheet_id, range="SYSTEM_STATUS!A:D",
            valueInputOption="RAW", body={"values": rows}
        ).execute()
        
        logger.info("📊 Dashboard & History updated successfully.")

    def _check_google_ai(self):
        """Checks Gemini AI connectivity."""
        try:
            from ai.logic.brain import Brain
            brain = Brain()
            if brain.mode != "Dumb":
                return {"status": "PERFECT", "details": f"Connected ({brain.mode})"}
            return {"status": "FAILED", "error": "Auth Failed"}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

    def _check_google_drive(self):
        """Checks Google Drive service initialization."""
        try:
            from services.google.drive_handler import DriveHandler
            drive = DriveHandler()
            if drive.service:
                return {"status": "PERFECT", "details": "Service Account Active"}
            return {"status": "WARNING", "details": "SA Missing"}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

    def _check_google_sheets(self, vault):
        """Checks access to the specific TravelKing Sheet."""
        try:
            from google.oauth2 import service_account
            from googleapiclient.discovery import build
            sa_path = os.path.join(self.root, "config/service_account.json")
            creds = service_account.Credentials.from_service_account_file(
                sa_path, scopes=['https://www.googleapis.com/auth/spreadsheets']
            )
            service = build('sheets', 'v4', credentials=creds)
            sheet_id = vault['travelking']['sheet_id']
            service.spreadsheets().get(spreadsheetId=sheet_id).execute()
            return {"status": "PERFECT", "details": "Sheet Accessible"}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

    def _check_gmail(self, vault):
        """Checks Gmail SMTP Auth."""
        import smtplib
        try:
            email = vault['google']['account_email']
            pwd = vault['google']['app_password']
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=5) as server:
                server.login(email, pwd)
            return {"status": "PERFECT", "details": "SMTP Authenticated"}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

    def _check_cpanel(self, vault):
        """Checks cPanel connectivity."""
        try:
            cfg = vault['cpanel']
            url = f"https://{cfg['host']}:2083/execute/DomainInfo/domains_data"
            headers = {"Authorization": f"cpanel {cfg['user']}:{cfg['api_token']}"}
            res = requests.get(url, headers=headers, timeout=5, verify=False)
            if res.status_code == 200:
                return {"status": "PERFECT", "user": cfg['user']}
            return {"status": "DEGRADED", "code": res.status_code}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

    def _check_facebook(self, vault):
        """Checks Facebook token."""
        try:
            cfg = vault['facebook']
            url = f"https://graph.facebook.com/v19.0/me?access_token={cfg['access_token']}"
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                return {"status": "PERFECT", "details": "Token valid"}
            return {"status": "EXPIRED", "action": "Manual Re-auth"}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

    def _check_travelpayouts(self, vault):
        """Checks Travelpayouts API."""
        try:
            token = vault['travelpayouts']['api_token']
            url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
            params = {'origin': 'PRG', 'destination': 'LON', 'token': token, 'limit': 1}
            res = requests.get(url, params=params, timeout=5)
            if res.status_code == 200:
                return {"status": "PERFECT", "details": "Data Active"}
            return {"status": "DEGRADED", "code": res.status_code}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

    def _check_github(self, vault):
        """Checks GitHub API."""
        try:
            token = vault['github']['token']
            headers = {"Authorization": f"token {token}"}
            res = requests.get("https://api.github.com/user", headers=headers, timeout=5)
            if res.status_code == 200:
                return {"status": "PERFECT", "user": res.json()['login']}
            return {"status": "FAILED", "code": res.status_code}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

    def _check_bing(self, vault):
        """Checks Bing Key format."""
        try:
            key = vault['bing']['api_key']
            if len(key) == 32:
                return {"status": "PERFECT", "details": "Key valid"}
            return {"status": "FAILED", "error": "Invalid Key"}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    g = Guardian()
    print(json.dumps(g.perform_health_check(), indent=2))
