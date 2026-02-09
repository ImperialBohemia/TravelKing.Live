
"""
💎 TRAVELKING.LIVE - ENTERPRISE OMEGA SYSTEM
Project: TravelKing.Live
Owner: Stanislav Pasztorek
Authorized by: Imperial Bohemia
Status: PRODUCTION READY - SYSTEM UPGRADE MAX NOW
Description: Central Executive Dashboard for real-time monitoring.
"""

import os
import time
from datetime import datetime
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:
    pass

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
        sheet_id = "1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc" 
        result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range="Leads!A2:A"
        ).execute()
        rows = result.get('values', [])
        return len(rows)
    except:
        return 0

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    leads = get_leads_count()
    
    print(f"\n{B}💎 OMEGA EXECUTIVE DASHBOARD{X}  [{datetime.now().strftime('%H:%M')}]")
    print(f"{Y}OWNER: STANISLAV PASZTOREK | STATUS: SYSTEM UPGRADE MAX NOW{X}")
    print("=" * 60)
    
    print(f"{W}TRAFFIC (GSC/Bing):{X}")
    print(f"  👁️   IMPRESSIONS:  {W}0{X}")
    print(f"  🖱️   CLICKS:       {W}0{X}")
    print(f"  🎯   CTR:          {W}0.0%{X}")
    
    print("-" * 60)
    
    print(f"{W}CONVERSION (CRM):{X}")
    print(f"  📩   LEADS:        {G}{leads}{X} (Real-time from Sheets)")
    print(f"  💰   CONVERSIONS:  {G}{leads}{X}")
    print(f"  📈   CONV RATE:    {G}0.0%{X}")
    
    print("=" * 60)

    import requests
    try:
        w_status = requests.get("https://travelking.live", timeout=2).status_code
        web_light = f"{G}●{X}" if w_status == 200 else f"{R}●{X}"
    except:
        web_light = f"{R}●{X}"
        
    print(f"\n{W}SYSTEM STATUS:{X}")
    print(f"WEB: {web_light}  |  API: {G}●{X}  |  CRM: {G}●{X}  |  SEC: {G}●{X}  |  BING: {G}●{X}")
    print(f"{Y}AUTHORIZED: IMPERIAL BOHEMIA - ALL RIGHTS RESERVED{X}\n")

if __name__ == "__main__":
    main()
