import json
import requests
import sys
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = '/home/q/TravelKing.Live/config/service_account.json'
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file']

print("🤖 Authenticating as Service Account (The Bot)...")
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Build Drive Service
service = build('drive', 'v3', credentials=creds)

# 1. Create Site File
file_metadata = {
    'name': 'TravelKing Flight Assistance (Bot Created)',
    'mimeType': 'application/vnd.google-apps.site'
}

print("🚀 Creating Site via Bot...")
file = service.files().create(body=file_metadata, fields='id, webViewLink').execute()
site_id = file.get('id')
site_link = file.get('webViewLink')

print(f"✅ Site Created! ID: {site_id}")
print(f"🔗 Private Link: {site_link}")

# 2. Share with User (valachman@gmail.com) as Editor
print("👤 Sharing with valachman@gmail.com...")
user_permission = {
    'type': 'user',
    'role': 'writer',
    'emailAddress': 'valachman@gmail.com'
}
service.permissions().create(
    fileId=site_id,
    body=user_permission,
    fields='id',
    emailMessage='Here is the new landing page created by TravelKing OMEGA Bot.'
).execute()
print("✅ Shared successfully!")

# 3. Make Public (Publish)
print("🌍 Making Public (Anyone with link can view)...")
public_permission = {
    'type': 'anyone',
    'role': 'reader'
}
service.permissions().create(
    fileId=site_id,
    body=public_permission,
    fields='id'
).execute()

print(f"🎉 DONE! The site is live and shared with you.")
print(f"👉 Go to: {site_link}")
