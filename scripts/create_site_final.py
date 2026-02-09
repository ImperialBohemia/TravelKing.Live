import json
import requests
import sys

# Load Configuration
with open('/home/q/TravelKing.Live/config/access_vault.json', 'r') as f:
    vault = json.load(f)

client_id = vault['google']['client_id']
client_secret = vault['google']['client_secret']
refresh_token = vault['google']['refresh_token']

print("🔄 Refreshing OAuth Token...")

# 1. Get Fresh Access Token
url = "https://oauth2.googleapis.com/token"
data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token,
    'grant_type': 'refresh_token'
}

response = requests.post(url, data=data)

if response.status_code == 200:
    new_token = response.json()['access_token']
    print(f"✅ Token Refreshed: {new_token[:10]}...")
    
    # 2. Update Vault (In Memory for this run, ideally save back)
    vault['google']['access_token'] = new_token
    
    # 3. Create & Publish Site
    sys.path.append('/home/q/TravelKing.Live')
    from core.google.sites import SitesClient
    
    client = SitesClient(new_token)
    
    print("🚀 Creating Site: TravelKing Flight Assistance...")
    result = client.create_site("TravelKing Flight Assistance")
    
    if result.get('success'):
        site_id = result['id']
        print(f"✅ Site Created! ID: {site_id}")
        
        # 4. Make Public (Share to anyone)
        print("🌍 Publishing (Sharing to Public)...")
        share_link = client.make_public(site_id)
        
        if share_link:
            print(f"🎉 DONE! Site is LIVE at: {share_link}")
        else:
            print("⚠️ Site created but failed to get public link. Check permissions.")
            
    else:
        print(f"❌ Failed to create site: {result}")

else:
    print(f"❌ Failed to refresh token: {response.text}")
