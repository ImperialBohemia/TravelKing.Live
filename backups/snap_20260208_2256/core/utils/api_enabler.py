
from googleapiclient.discovery import build
from google.oauth2 import service_account

def enable_gsc_api():
    print("💎 OMEGA AUTO-FIX: Attempting to enable Search Console API...")
    try:
        creds = service_account.Credentials.from_service_account_file(
            'config/service_account.json',
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        service = build('serviceusage', 'v1', credentials=creds)
        
        # Enable Search Console API
        request = service.services().enable(
            name='projects/1009428807876/services/searchconsole.googleapis.com'
        )
        response = request.execute()
        print(f"✅ API Enable Request Sent: {response}")
        
    except Exception as e:
        print(f"❌ Auto-Fix Failed: {e}")
        if "403" in str(e):
            print("   -> Bot lacks 'Service Usage Admin' role on the GCP Project.")

if __name__ == "__main__":
    enable_gsc_api()
