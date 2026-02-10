import json
import requests
import os

PATHS = [
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'access_vault.json'),
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'config', 'access_vault_restored.json')
]

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return None

def test_google(creds, label="Google"):
    print(f"--- Testing {label} ---")
    email = creds.get('account_email') or creds.get('email')
    access_token = creds.get('access_token')
    
    if not access_token:
        print(f"❌ No access token found for {email}.")
        return False
    
    url = f"https://www.googleapis.com/oauth2/v3/tokeninfo?access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Google Connection Active: {email}")
        return True
    else:
        print(f"⚠️ Google Access Token for {email} Expired or Invalid. Trying refresh...")
        refresh_token = creds.get('refresh_token')
        # We might need client_id/secret which is in the other file sometimes
        client_id = creds.get('client_id') or os.environ.get("GOOGLE_CLIENT_ID")
        client_secret = creds.get('client_secret') or os.environ.get("GOOGLE_CLIENT_SECRET")
        
        if refresh_token:
            refresh_url = "https://oauth2.googleapis.com/token"
            data = {
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
                "grant_type": "refresh_token"
            }
            ref_resp = requests.post(refresh_url, data=data)
            if ref_resp.status_code == 200:
                new_tokens = ref_resp.json()
                print(f"✅ Google Token for {email} Refreshed Successfully!")
                return True
            else:
                print(f"❌ Google Refresh for {email} Failed: {ref_resp.text}")
        else:
            print(f"❌ No refresh token for {email}.")
    return False

def test_facebook(creds):
    print("--- Testing Facebook ---")
    token = creds.get('access_token')
    url = f"https://graph.facebook.com/me?access_token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Facebook Connection Active: {data.get('name')} (ID: {data.get('id')})")
        return True
    else:
        print(f"❌ Facebook Access Token Invalid.")
    return False

def test_cpanel(creds):
    print("--- Testing cPanel ---")
    host = creds.get('host')
    user = creds.get('user')
    token = creds.get('api_token')
    url = f"https://{host}:2083/execute/ResourceUsage/get_usages"
    headers = {"Authorization": f"cpanel {user}:{token}"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"✅ cPanel Connection Active: {user}@{host}")
            return True
        else:
            print(f"❌ cPanel Connection Failed.")
    except:
        print(f"❌ cPanel Connection Error.")
    return False

def test_github(creds):
    print("--- Testing GitHub ---")
    token = creds.get('token')
    if not token: return False
    headers = {"Authorization": f"token {token}"}
    response = requests.get("https://api.github.com/user", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ GitHub Connection Active: {data.get('login')}")
        return True
    return False

def main():
    results = {}
    
    for path in PATHS:
        vault = load_json(path)
        if not vault: continue
        
        print(f"\nChecking vault: {path}")
        if 'google' in vault:
            results[f"google_{vault['google'].get('email') or vault['google'].get('account_email')}"] = test_google(vault['google'])
        if 'facebook' in vault:
            results['facebook'] = test_facebook(vault['facebook'])
        if 'cpanel' in vault:
            results['cpanel'] = test_cpanel(vault['cpanel'])
        if 'github' in vault:
            results['github'] = test_github(vault['github'])

    print("\n--- FINAL STATUS ---")
    for service, status in results.items():
        print(f"{service.upper()}: {'CONNECTED' if status else 'DISCONNECTED'}")

if __name__ == "__main__":
    main()
