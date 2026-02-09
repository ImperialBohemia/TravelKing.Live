import os
import sys
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from core.hub import hub
import json

# Force color output
G = "\033[92m" # Green
R = "\033[91m" # Red
Y = "\033[93m" # Yellow
X = "\033[0m"  # Reset

def get_creds():
    """Constructs user credentials from the vault."""
    v = hub.vault['google']
    return Credentials(
        token=v['access_token'],
        refresh_token=v['refresh_token'],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=v['client_id'],
        client_secret=v['client_secret'],
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )

def get_sa_creds():
    """Constructs Service Account credentials."""
    from google.oauth2 import service_account
    # We know the path is config/service_account.json
    # But we can't read it? heartbeat.py imported it successfully via google libraries?
    # No, heartbeat.py used 'config/service_account.json' path.
    return service_account.Credentials.from_service_account_file(
        'config/service_account.json',
        scopes=[
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive.readonly',
            'https://www.googleapis.com/auth/analytics.readonly',
            'https://www.googleapis.com/auth/tagmanager.readonly',
            'https://www.googleapis.com/auth/webmasters.readonly'
        ]
    )

def verify_all():
    print(f"\n💎 {Y}OMEGA GOOGLE DEEP SCAN{X}\n")
    user_creds = get_creds()
    try:
        sa_creds = get_sa_creds()
        print(f"{G}✅ Service Account:{X} Loaded.")
    except Exception as e:
        sa_creds = None
        print(f"{Y}⚠️  Service Account:{X} Not found/Load failed. {e}")

    # 1. Google Drive (Sites & Files) - TRY SA FIRST
    try:
        service = build('drive', 'v3', credentials=sa_creds or user_creds)
        results = service.files().list(pageSize=5, fields="files(id, name, mimeType)").execute()
        files = results.get('files', [])
        print(f"{G}✅ Google Drive:{X} Connected. (Visible files: {len(files)})")
        for f in files:
            print(f"   - {f['name']} ({f['mimeType']})")
    except Exception as e:
        print(f"{R}❌ Google Drive:{X} Failed. {str(e)[:100]}")

    # 2. Google Sheets - TRY SA FIRST
    try:
        service = build('sheets', 'v4', credentials=sa_creds or user_creds)

        # Try to read the specific sheet from vault
        sheet_id = hub.vault['travelking']['sheet_id']
        sheet = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
        title = sheet['properties']['title']
        print(f"{G}✅ Google Sheets:{X} Connected. (Target: {title})")
    except Exception as e:
        if "403" in str(e):
             print(f"{R}❌ Google Sheets:{X} Access Denied (403). Share '{hub.vault['travelking']['sheet_id']}' with Service Account")
        else:
             print(f"{R}❌ Google Sheets:{X} Failed. {str(e)[:100]}")

    # 3. Google Analytics (GA4)
    try:
        service = build('analyticsadmin', 'v1beta', credentials=sa_creds)
        # Just list accounts to verify access
        accounts = service.accounts().list().execute()
        print(f"{G}✅ Google Analytics:{X} Connected (via Bot). (Accounts: {len(accounts.get('accounts', []))})")
    except Exception as e:
        print(f"{R}❌ Google Analytics:{X} Failed (Bot). Add '{hub.vault['google']['account_email']}' or Service Account to GA4 Admin.")

    # 4. Google Tag Manager
    try:
        service = build('tagmanager', 'v2', credentials=sa_creds)
        accounts = service.accounts().list().execute()
        print(f"{G}✅ Google Tag Manager:{X} Connected (via Bot). (Accounts: {len(accounts.get('account', []))})")
    except Exception as e:
        print(f"{R}❌ Google Tag Manager:{X} Failed (Bot). Add Service Account to GTM Admin.")

    # 5. Google Search Console
    try:
        service = build('searchconsole', 'v1', credentials=sa_creds)
        sites = service.sites().list().execute()
        site_list = sites.get('siteEntry', [])
        print(f"{G}✅ Google Search Console:{X} Connected (via Bot). (Verified Sites: {len(site_list)})")
        for s in site_list[:3]:
            print(f"   - {s['siteUrl']} ({s['permissionLevel']})")
    except Exception as e:
        print(f"{R}❌ Google Search Console:{X} Failed (Bot). FULL ERROR: {str(e)}")

    # 6. Google Ads
    # Ads API is complex and requires specific library, checking raw scope/access via token info
    print(f"{Y}⚠️  Google Ads:{X} Logic integrated via `core/google/crm.py`, but requires Customer ID to test.")

if __name__ == "__main__":
    verify_all()