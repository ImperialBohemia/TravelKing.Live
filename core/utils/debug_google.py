
import json
import os
import requests
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def debug_refresh():
    creds_path = "/home/q/.gemini/oauth_creds.json"
    if not os.path.exists(creds_path):
        print("No oauth_creds.json found")
        return

    with open(creds_path) as f:
        data = json.load(f)

    print("Found creds for:", data.get("access_token")[:10] + "...")
    print("Refresh Token:", data.get("refresh_token")[:10] + "...")

    # Client ID from the token itself (azp)
    client_id = "681255809395-oo8ft2oprdrnp9e3aqf6av3hmduib135j.apps.googleusercontent.com"

    # Try 1: Standard Refresh without secret (Public Client)
    print("\n--- Attempt 1: Public Client Refresh ---")
    creds = Credentials(
        token=data["access_token"],
        refresh_token=data["refresh_token"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        # client_secret=None
    )

    try:
        creds.refresh(Request())
        print("SUCCESS! New Token:", creds.token[:10] + "...")
        return
    except Exception as e:
        print("Failed:", e)

    # Try 2: Cloud SDK Client ID (Common fallback)
    print("\n--- Attempt 2: Cloud SDK Client ID ---")
    cloud_id = "764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com"
    cloud_secret = "d-ayG_F3U9yU1fT-3B-6BfE9"

    creds = Credentials(
        token=data["access_token"],
        refresh_token=data["refresh_token"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=cloud_id,
        client_secret=cloud_secret
    )

    try:
        creds.refresh(Request())
        print("SUCCESS! New Token:", creds.token[:10] + "...")
        return
    except Exception as e:
        print("Failed:", e)

    # Try 3: Raw POST with Cloud SDK
    print("\n--- Attempt 3: Raw POST Cloud SDK ---")
    res = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": cloud_id,
        "box_secret": cloud_secret, # typo intentional to check behavior? no, use correct
        "client_secret": cloud_secret,
        "refresh_token": data["refresh_token"],
        "grant_type": "refresh_token"
    })
    print("Response:", res.json())

if __name__ == "__main__":
    debug_refresh()
