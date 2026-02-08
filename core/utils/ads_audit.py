from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests
import json

def check_ads_access():
    print("💎 OMEGA ADS VERIFIER: Checking Access via Email Invitation...")
    
    # 1. Load SA Creds
    creds = service_account.Credentials.from_service_account_file(
        'config/service_account.json',
        scopes=['https://www.googleapis.com/auth/adwords']
    )
    creds.refresh(Request())
    token = creds.token
    print(f"✅ Token Generated. (Scope: adwords)")

    # 2. Try to List Customers (REST API)
    # Even without a Developer Token, if we are added as a User, we might be able to see something?
    # NO. The Google Ads API *always* requires a 'developer-token' header.
    # Without it, the API rejects the request with "DEVELOPER_TOKEN_NOT_APPROVED" or similar.
    
    # However, let's TRY with a dummy token just to see the error message.
    # Sometimes standard access allows basic calls.
    
    url = "https://googleads.googleapis.com/v17/customers:listAccessibleCustomers"
    headers = {
        "Authorization": f"Bearer {token}",
        "developer-token": "INSERT_DEV_TOKEN_HERE_IF_YOU_HAVE_ONE" 
    }
    
    # We don't have a Dev Token. The user gave *access* to the account (email invite).
    # But the API *mechanism* requires a Dev Token to act as an App.
    # Unless... the user means they gave access to the *Service Account Email* inside the Google Ads UI?
    # Yes, that authorizes the *Identity*. But the *Tool* (this script) needs a Dev Token to talk to the API.
    
    print("\n⚠️  ANALYSIS:")
    print("You invited the bot (travelking@...) to the Ads Account. That is step 1.")
    print("Step 2 is having a 'Developer Token' to use the API.")
    print("I will try to call the API without a valid Dev Token to confirm this blockage.")
    
    try:
        res = requests.get(url, headers=headers)
        print(f"\nResponse Code: {res.status_code}")
        print(f"Response Body: {res.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_ads_access()