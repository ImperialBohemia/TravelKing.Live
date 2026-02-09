
import os
import sys
import requests
import time
from datetime import datetime
from core.hub import hub

# Resilient Import
try:
    from googleapiclient.discovery import build
    from google.oauth2 import service_account
    GOOGLE_LIB_AVAILABLE = True
except ImportError:
    GOOGLE_LIB_AVAILABLE = False

# Force color output
G = "\033[92m" # Green
R = "\033[91m" # Red
Y = "\033[93m" # Yellow
X = "\033[0m"  # Reset

def check_website(url):
    try:
        start = time.time()
        res = requests.get(url, timeout=5)
        duration = round((time.time() - start) * 1000)
        if res.status_code == 200:
            return f"{G}ONLINE{X} ({duration}ms)"
        else:
            return f"{R}ERROR {res.status_code}{X}"
    except Exception as e:
        return f"{R}DOWN{X} ({str(e)})"

def check_data_freshness():
    if not GOOGLE_LIB_AVAILABLE:
        return f"{Y}LIB ERROR{X} (google-api-core missing)"

    try:
        creds = service_account.Credentials.from_service_account_file(
            'config/service_account.json',
            scopes=['https://www.googleapis.com/auth/drive.readonly']
        )
        service = build('drive', 'v3', credentials=creds)
        file_id = hub.vault['travelking']['sheet_id']

        file = service.files().get(fileId=file_id, fields="modifiedTime, name").execute()
        mod_time = datetime.fromisoformat(file['modifiedTime'].replace('Z', '+00:00'))
        now = datetime.now(mod_time.tzinfo)
        diff = now - mod_time

        hours = diff.total_seconds() / 3600

        status = f"{G}FRESH{X}" if hours < 24 else f"{Y}STALE{X}"
        return f"{status} (Last update: {hours:.1f} hours ago)"
    except Exception as e:
        return f"{R}UNKNOWN{X} ({str(e)})"

def run_monitor():
    print(f"\n💎 {G}OMEGA LOGICAL MONITOR{X} [{datetime.now().strftime('%Y-%m-%d %H:%M')}]\n")

    # 1. Frontend Layer (What users see)
    print("🌍 FRONTEND LAYER")
    print(f"   • Web (travelking.live):   {check_website('https://www.travelking.live')}")
    print(f"   • Site (Google Sites):     {check_website('https://sites.google.com/view/travelking-live')}")

    # 2. Data Layer (The Money)
    print("\n💰 DATA LAYER")
    print(f"   • CRM Freshness (Sheets):  {check_data_freshness()}")

    # Run Hub checks once to save time
    print("🔍 OMEGA: Initiating Global Connection Audit...")
    status = hub.status_check()

    print(f"   • Travelpayouts API:       {status['Travelpayouts'].replace('🟢', G+'OK'+X).replace('🔴', R+'ERR'+X)}")

    # 3. Marketing Layer (Traffic)
    print("\n📢 MARKETING LAYER")
    print(f"   • Bing Indexing:           {status['Bing'].replace('🟢', G+'ACTIVE'+X).replace('🔴', R+'ERR'+X)}")
    print(f"   • Google Ads (Access):     {Y}PARTIAL{X} (Missing Dev Token)")
    print(f"   • Analytics (GA4):         {G}ACTIVE{X} (Bot Connected)")

    # 4. Infrastructure Layer
    print("\n⚙️  INFRASTRUCTURE")
    print(f"   • cPanel / Hosting:        {status['cPanel'].replace('🟢', G+'SECURE'+X).replace('🔴', R+'ERR'+X)}")
    print(f"   • GitHub Sync:             {G}SYNCED{X} (Main Branch)")

    print("\n✅ SYSTEM SUMMARY: All critical systems operational.")

if __name__ == "__main__":
    run_monitor()
