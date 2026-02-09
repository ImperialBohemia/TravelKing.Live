import json
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from loguru import logger

# Paths
ROOT_DIR = '/home/q/TravelKing.Live'
VAULT_PATH = os.path.join(ROOT_DIR, 'config/access_vault.json')
SERVICE_ACCOUNT_PATH = os.path.join(ROOT_DIR, 'config/service_account.json')

def init_spreadsheet():
    with open(VAULT_PATH, 'r') as f:
        vault = json.load(f)
    
    sheet_id = vault['travelking']['sheet_id']
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_PATH,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    service = build('sheets', 'v4', credentials=creds)

    # 1. Check/Create "Leads" sheet
    # 2. Check/Create "Tasks" sheet
    try:
        spreadsheet = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
        sheets = [s['properties']['title'] for s in spreadsheet.get('sheets', [])]
        
        requests = []
        if "Leads" not in sheets:
            requests.append({'addSheet': {'properties': {'title': 'Leads'}}})
        if "Tasks" not in sheets:
            requests.append({'addSheet': {'properties': {'title': 'Tasks'}}})
        
        if requests:
            service.spreadsheets().batchUpdate(spreadsheetId=sheet_id, body={'requests': requests}).execute()
            logger.success("📁 Created missing sheets: Leads, Tasks")
        
        # Add headers
        header_requests = [
            {
                'updateCells': {
                    'rows': [{'values': [{'userEnteredValue': {'stringValue': v}} for v in ["Timestamp", "Name", "Email", "Interest", "Source", "Status"]]}],
                    'fields': 'userEnteredValue',
                    'range': {'sheetId': None, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 6}
                }
            }
        ]
        
        # Get sheet IDs
        spreadsheet = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
        for s in spreadsheet['sheets']:
            if s['properties']['title'] == "Leads":
                header_requests[0]['updateCells']['range']['sheetId'] = s['properties']['sheetId']
                service.spreadsheets().batchUpdate(spreadsheetId=sheet_id, body={'requests': header_requests}).execute()
                logger.info("🏷️ Headers added to 'Leads'.")
                
        logger.success("🚀 Spreadsheet initialized successfully.")

    except Exception as e:
        logger.error(f"❌ Initialization failed: {e}")
        logger.info(f"💡 IMPORTANT: Ensure that '{creds.service_account_email}' has Editor access to the spreadsheet.")

if __name__ == "__main__":
    init_spreadsheet()
