import os
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from core.hub import hub

# Force color output
G = "\033[92m" # Green
R = "\033[91m" # Red
X = "\033[0m"  # Reset

def verify_impersonation():
    print(f"\n💎 {G}OMEGA IMPERSONATION CHECK{X}\n")

    target_email = hub.vault['google']['account_email'] # trendnatures@gmail.com
    print(f"Target: {target_email}")

    try:
        # Load SA creds with specific marketing scopes, subject to the user
        creds = service_account.Credentials.from_service_account_file(
            'config/service_account.json',
            scopes=[
                'https://www.googleapis.com/auth/analytics.readonly',
                'https://www.googleapis.com/auth/tagmanager.readonly',
                'https://www.googleapis.com/auth/webmasters.readonly'
            ],
            subject=target_email
        )

        # Test Analytics
        try:
            service = build('analyticsadmin', 'v1beta', credentials=creds)
            accounts = service.accounts().list().execute()
            print(f"{G}✅ Analytics:{X} Success via Impersonation! (Accounts: {len(accounts.get('accounts', []))})")
        except Exception as e:
            print(f"{R}❌ Analytics:{X} Impersonation Failed. {str(e)[:100]}")

    except Exception as e:
        print(f"{R}❌ Setup:{X} Failed to create impersonated creds. {e}")

if __name__ == "__main__":
    verify_impersonation()