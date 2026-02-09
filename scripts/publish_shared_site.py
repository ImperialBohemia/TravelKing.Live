import json
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = '/home/q/TravelKing.Live/config/service_account.json'
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file']

print("🤖 Authenticating as Service Account (The Bot)...")
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

service = build('drive', 'v3', credentials=creds)

print("🔍 Scanning for Shared Google Sites...")
# Query for Google Sites shared with me
results = service.files().list(
    q="mimeType='application/vnd.google-apps.site' and sharedWithMe=true",
    fields="files(id, name, webViewLink, owners)",
    pageSize=10
).execute()

files = results.get('files', [])

if not files:
    print("❌ No shared sites found yet. Google replication might take a minute.")
else:
    print(f"✅ Found {len(files)} Shared Sites!")
    for file in files:
        print(f"   ------------------------------------------------")
        print(f"   Name: {file['name']}")
        print(f"   ID: {file['id']}")
        print(f"   Link: {file.get('webViewLink', 'N/A')}")
        
        # Try to Publish (Make Public)
        print("   🌍 Attempting to Publish (Public Read Access)...")
        try:
            permission = {
                'type': 'anyone',
                'role': 'reader'
            }
            service.permissions().create(
                fileId=file['id'],
                body=permission,
                fields='id'
            ).execute()
            print("   🎉 SUCCESS! Site is now PUBLIC.")
        except Exception as e:
            print(f"   ⚠️ Publish warning: {e}")

print("------------------------------------------------")
