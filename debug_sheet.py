import json
import logging
import sys
import os

# Add project root to path
sys.path.append(os.getcwd())

from core.connectors.google import GoogleConnector
from core.google.sheets import SheetsClient

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    # 1. Load Vault
    with open("config/access_vault.json") as f:
        vault = json.load(f)
    
    # 2. Initialize Connector & Refresh
    connector = GoogleConnector(vault)
    print("🔄 Refreshing Token...")
    if connector.refresh():
        print("✅ Token Refreshed!")
        token = connector.token
        
        # 3. Check Sheet
        sheet_id = "1Kg3jrN5mxPCuD8wKoYmbCXoj0Yyu_LOgsZw6EZzSbAk"
        print(f"🔍 Checking Sheet: {sheet_id}")
        
        client = SheetsClient(token)
        
        # Try to read first row of first sheet
        try:
            # First get spreadsheet metadata to find sheet names
            import requests
            url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}"
            headers = {"Authorization": f"Bearer {token}"}
            resp = requests.get(url, headers=headers)
            
            if resp.status_code == 200:
                meta = resp.json()
                sheets = meta.get("sheets", [])
                print(f"📄 Found {len(sheets)} sheets.")
                
                for sheet in sheets:
                    title = sheet["properties"]["title"]
                    print(f"   - Sheet: {title}")
                    
                    # Read headers
                    rows = client.read_range(sheet_id, f"{title}!A1:Z1")
                    print(f"     Headers: {rows}")
            else:
                print(f"❌ Error reading metadata: {resp.text}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            
    else:
        print("🔴 Failed to refresh token.")

if __name__ == "__main__":
    main()
