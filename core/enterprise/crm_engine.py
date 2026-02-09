import json
import os
import sys
from datetime import datetime
from loguru import logger
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Paths
ROOT_DIR = '/home/q/TravelKing.Live'
VAULT_PATH = os.path.join(ROOT_DIR, 'config/access_vault.json')
SERVICE_ACCOUNT_PATH = os.path.join(ROOT_DIR, 'config/service_account.json')

class CRMEngine:
    def __init__(self):
        with open(VAULT_PATH, 'r') as f:
            self.vault = json.load(f)
        
        self.sheet_id = self.vault['travelking']['sheet_id']
        self.creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_PATH,
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        self.service = build('sheets', 'v4', credentials=self.creds)

    def get_new_leads(self):
        """
        Fetches unprocessed leads from the 'Leads' sheet.
        Assumes status column (index 5, 'F') is empty or 'NEW' for fresh leads.
        """
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.sheet_id, range="Leads!A2:F"
            ).execute()
            rows = result.get('values', [])
            
            new_leads = []
            for i, row in enumerate(rows):
                # Check status column (index 5). If missing or 'NEW', it's a lead.
                status = row[5] if len(row) > 5 else "NEW"
                if status == "NEW" or status == "":
                    # Normalize row length
                    while len(row) < 6:
                        row.append("")
                    
                    new_leads.append({
                        "row_id": i + 2, # 1-based index, +header
                        "timestamp": row[0],
                        "name": row[1],
                        "email": row[2],
                        "interest": row[3],
                        "source": row[4]
                    })
            return new_leads
        except Exception as e:
            logger.error(f"❌ Failed to fetch leads: {e}")
            return []

    def update_lead_status(self, row_id, status):
        """Updates the status of a lead processing."""
        try:
            body = {'values': [[status]]}
            self.service.spreadsheets().values().update(
                spreadsheetId=self.sheet_id, 
                range=f"Leads!F{row_id}", 
                valueInputOption="USER_ENTERED", 
                body=body
            ).execute()
            logger.info(f"✅ Lead status updated: Row {row_id} -> {status}")
        except Exception as e:
            logger.error(f"❌ Failed to update status: {e}")

    def log_lead(self, name, email, interest, source="Form"):
        """Logs a new lead to the CRM sheet."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        values = [[timestamp, name, email, interest, source, "NEW"]]
        
        body = {'values': values}
        try:
            result = self.service.spreadsheets().values().append(
                spreadsheetId=self.sheet_id,
                range="Leads!A:F",
                valueInputOption="RAW",
                body=body
            ).execute()
            logger.success(f"📈 Lead logged to CRM: {email}")
            return result
        except Exception as e:
            logger.error(f"❌ Failed to log lead: {e}")
            return None

    def get_pending_tasks(self):
        """Retrieves technical tasks or maintenance logs from the sheet."""
        # This will be used to feed the Google Site "Authority Hub"
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.sheet_id,
                range="Tasks!A:E"
            ).execute()
            return result.get('values', [])
        except Exception as e:
            logger.error(f"❌ Failed to fetch tasks: {e}")
            return []

if __name__ == "__main__":
    crm = CRMEngine()
    # Test logging
    crm.log_lead("Test User", "test@example.com", "Private Jet Charter", source="AI Test")
