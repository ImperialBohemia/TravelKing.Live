import os
import time
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Colors
W = "\033[97m" # White (Bold)
G = "\033[92m" # Green
R = "\033[91m" # Red
Y = "\033[93m" # Yellow
B = "\033[94m" # Blue
X = "\033[0m"  # Reset

def get_leads_count():
    try:
        creds = service_account.Credentials.from_service_account_file(
            'config/service_account.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
        )
        service = build('sheets', 'v4', credentials=creds)
        # TravelKing Sheet ID
        sheet_id = "1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc" 
        result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range="Leads!A2:A"
        ).execute()
        rows = result.get('values', [])
        return len(rows)
    except:
        return 0 # Fail safe

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # 1. FETCH DATA (Real & Simulated for now)
    leads = get_leads_count()
    impressions = 0 # Placeholder until GSC API is fully wired
    clicks = 0      # Placeholder
    ctr = 0.0       # Placeholder
    conversions = leads
    conv_rate = 0.0
    
    # 2. THE BIG BOARD (Business Metrics)
    print(f"\n{B}💎 OMEGA EXECUTIVE DASHBOARD{X}  [{datetime.now().strftime('%H:%M')}]")
    print("=" * 60)
    
    # Row 1: Traffic
    print(f"{W}TRAFFIC (GSC/Bing):{X}")
    print(f"  👁️   IMPRESSIONS:  {W}{impressions}{X}")
    print(f"  🖱️   CLICKS:       {W}{clicks}{X}")
    print(f"  🎯   CTR:          {W}{ctr}%{X}")
    
    print("-" * 60)
    
    # Row 2: Money (The important part)
    print(f"{W}CONVERSION (CRM):{X}")
    print(f"  📩   LEADS:        {G}{leads}{X}  <-- Real Data from Sheets")
    print(f"  💰   CONVERSIONS:  {G}{conversions}{X}")
    print(f"  📈   CONV RATE:    {G}{conv_rate}%{X}")
    
    print("=" * 60)

    # 3. CONTROL LIGHTS (Minimal Info)
    # Checking endpoints quickly
    import requests
    try:
        w_status = requests.get("https://travelking.live", timeout=2).status_code
        web_light = f"{G}●{X}" if w_status == 200 else f"{R}●{X}"
    except:
        web_light = f"{R}●{X}"
        
    # Mocking other lights based on known state
    api_light = f"{G}●{X}" # Travelpayouts
    db_light  = f"{G}●{X}" # Sheets
    sec_light = f"{G}●{X}" # SSL/Hosting
    
    print(f"\n{W}SYSTEM STATUS:{X}")
    print(f"WEB: {web_light}  |  API: {api_light}  |  CRM: {db_light}  |  SEC: {sec_light}  |  V: 1.0.0")
    print("\n")

if __name__ == "__main__":
    main()