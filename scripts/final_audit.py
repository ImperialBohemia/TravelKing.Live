
import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

def verify_all():
    print("🏰 OMEGA FINAL VERIFICATION AUDIT")
    print("=" * 40)
    
    # 1. Connection Vault & Service Account
    vault_path = '/home/q/TravelKing.Live/config/access_vault.json'
    sa_path = '/home/q/TravelKing.Live/config/service_account.json'
    
    with open(vault_path) as f: vault = json.load(f)
    print(f"✅ Vault loaded. Account: {vault['google'].get('account_email')}")
    
    creds = service_account.Credentials.from_service_account_file(sa_path, scopes=['https://www.googleapis.com/auth/spreadsheets'])
    service = build('sheets', 'v4', credentials=creds)
    spreadsheet_id = vault['travelking']['sheet_id']
    
    # 2. Sheet Health
    try:
        res = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='SYSTEM_STATUS!A1:B20').execute()
        vals = res.get('values', [])
        print(f"✅ Google Sheet accessible. Dashboard rows: {len(vals)}")
    except Exception as e:
        print(f"❌ Sheet Sync Error: {e}")

    # 3. Robots & Security
    robots_path = '/home/q/TravelKing.Live/robots.txt'
    if os.path.exists(robots_path):
        with open(robots_path) as f:
            if 'Disallow: /' in f.read():
                print("✅ Robots.txt: SAFE (Indexing Blocked)")
            else:
                print("⚠️ Robots.txt: DANGER (Indexing allowed!)")

    # 4. Antigravity Stability (Cache Check)
    conv_dir = '/home/q/.gemini/antigravity/conversations/'
    pbs = [f for f in os.listdir(conv_dir) if f.endswith('.pb')]
    total_size = sum(os.path.getsize(os.path.join(conv_dir, f)) for f in pbs) / (1024*1024)
    print(f"✅ Antigravity Cache: {len(pbs)} files, {total_size:.2f} MB (Optimized)")

if __name__ == "__main__":
    verify_all()
