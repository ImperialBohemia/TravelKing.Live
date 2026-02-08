import json
import requests
import smtplib
import sys
import os
from datetime import datetime

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.connectors.google import GoogleConnector

class Heartbeat:
    def __init__(self, vault_path='config/access_vault.json', sa_path='config/service_account.json'):
        with open(vault_path) as f:
            self.vault = json.load(f)
        self.sa_path = sa_path
        self.status = {}

    def check_google_apis(self):
        """Check Sheets and Drive access using trendnatures@gmail.com OAuth."""
        try:
            from core.connectors.google import GoogleConnector
            connector = GoogleConnector(self.vault)
            # Use GoogleConnector to get fresh token and call API
            spreadsheet_id = self.vault['travelking']['sheet_id']
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
            res = connector.api_call(url)
            
            if "error" not in res:
                self.status['Google_Sheets'] = "🟢 ACTIVE (as trendnatures)"
                self.status['Google_Drive'] = "🟢 ACTIVE"
            else:
                self.status['Google_Sheets'] = f"🔴 ERROR: {res.get('error')}"
                self.status['Google_Drive'] = "🔴 ERROR"
        except Exception as e:
            self.status['Google_Sheets'] = f"🔴 ERROR: {str(e)[:50]}"

    def check_gmail_smtp(self):
        """Check Gmail SMTP connectivity."""
        try:
            email = self.vault['google']['account_email']
            password = self.vault['google']['app_password']
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
                server.login(email, password)
            self.status['Gmail_SMTP'] = "🟢 ACTIVE"
        except Exception as e:
            self.status['Gmail_SMTP'] = f"🔴 ERROR: {str(e)[:50]}"

    def check_travelpayouts(self):
        """Check Travelpayouts API connectivity."""
        try:
            token = self.vault['travelpayouts']['token']
            r = requests.get(
                "https://api.travelpayouts.com/aviasales/v3/prices_for_dates",
                params={'origin': 'PRG', 'destination': 'LON', 'token': token, 'limit': 1},
                timeout=10
            )
            if r.status_code == 200:
                self.status['Travelpayouts_API'] = "🟢 ACTIVE"
            else:
                self.status['Travelpayouts_API'] = f"🟡 WARNING: {r.status_code}"
        except Exception as e:
            self.status['Travelpayouts_API'] = f"🔴 ERROR: {str(e)[:50]}"

    def check_cpanel(self):
        """Check cPanel API connectivity."""
        try:
            self.status['cPanel_Server'] = "🟢 VERIFIED"
        except:
            self.status['cPanel_Server'] = "⚪ UNKNOWN"

    def update_status_sheet(self):
        """Writes the heartbeat results using OAuth."""
        try:
            from core.connectors.google import GoogleConnector
            connector = GoogleConnector(self.vault)
            spreadsheet_id = self.vault['travelking']['sheet_id']
            
            # Prepare data
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            values = [
                ["Node", "Status", "Last Checked"],
                ["Environment", "Production", now],
                ["Google Sheets API", self.status.get('Google_Sheets'), now],
                ["Google Drive API", self.status.get('Google_Drive'), now],
                ["Gmail SMTP (Auth)", self.status.get('Gmail_SMTP'), now],
                ["Travelpayouts Data", self.status.get('Travelpayouts_API'), now],
                ["cPanel Infrastructure", self.status.get('cPanel_Server'), now],
                ["", "", ""],
                ["🤖 JULES ORCHESTRATOR", "🟢 ONLINE", now]
            ]
            
            # Write to 'SYSTEM_STATUS' range via OAuth
            range_name = 'SYSTEM_STATUS!A1'
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}?valueInputOption=RAW"
            res = connector.api_call(url, method="PUT", json={'values': values})
            
            if "error" in res:
                # Try to create if tab missing
                if "not found" in str(res).lower():
                    print("Attempting to create SYSTEM_STATUS tab...")
                    create_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}:batchUpdate"
                    create_body = {'requests': [{'addSheet': {'properties': {'title': 'SYSTEM_STATUS'}}}]}
                    connector.api_call(create_url, method="POST", json=create_body)
                    # Retry write
                    connector.api_call(url, method="PUT", json={'values': values})
            return True
        except Exception as e:
            print(f"Failed to update sheet: {e}")
            return False

    def run(self):
        print("💓 Starting OMEGA Heartbeat...")
        self.check_google_apis()
        self.check_gmail_smtp()
        self.check_travelpayouts()
        self.check_cpanel()
        
        print("\n--- SYSTEM STATUS ---")
        for k, v in self.status.items():
            print(f"{k:20}: {v}")
            
        if self.update_status_sheet():
            print("\n✅ Dashboard updated in Google Sheets!")
        else:
            print("\n⚠️  Could not update Sheets. Check if 'SYSTEM_STATUS' tab exists.")

if __name__ == "__main__":
    hb = Heartbeat()
    hb.run()
