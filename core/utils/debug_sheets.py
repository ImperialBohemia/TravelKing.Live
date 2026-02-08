import os
import sys

# Add project root to path
sys.path.append(os.getcwd())

from core.connectors.google import GoogleConnector
from core.hub import hub

def list_google_sheets_tabs():
    """Lists all tabs in the configured spreadsheet."""
    try:
        sheet_id = hub.vault['travelking']['sheet_id']
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}"
        
        print(f"DEBUG: Attempting to fetch spreadsheet info from {url}")
        
        # Using hub.google which is already initialized and handles refresh
        res = hub.google.api_call(url)
        
        if 'sheets' in res:
            title = res.get('properties', {}).get('title', 'Unknown')
            print(f"\n✅ Connected to Sheet: {title}")
            print("📑 Tabs found:")
            for sheet in res['sheets']:
                props = sheet['properties']
                print(f"  - {props['title']} (ID: {props['sheetId']})")
        else:
            print("❌ Error fetching sheets:", res)
            
    except Exception as e:
        print(f"❌ Exception listing sheets: {e}")

def get_status_data():
    """Reads the SYSTEM_STATUS tab."""
    try:
        sheet_id = hub.vault['travelking']['sheet_id']
        range_name = "SYSTEM_STATUS!A1:C10"
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{range_name}"
        
        res = hub.google.api_call(url)
        
        if 'values' in res:
            print(f"\n📊 Data from SYSTEM_STATUS:")
            for row in res['values']:
                print(f"  {row}")
        else:
            print("⚠️ No data found in SYSTEM_STATUS or error:", res)

    except Exception as e:
        print(f"❌ Exception reading data: {e}")

if __name__ == "__main__":
    list_google_sheets_tabs()
    get_status_data()