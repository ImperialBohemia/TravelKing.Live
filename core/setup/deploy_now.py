import requests
import json
import os
import urllib3

def deploy_to_cpanel():
    print("🚀 OMEGA DEPLOY: Pushing 'Best on Planet' Web to travelking.live...")
    
    # 1. Load Credentials
    try:
        with open('config/access_vault.json', 'r') as f:
            vault = json.load(f)
        cpanel = vault.get('cpanel', {})
        host = cpanel.get('host')
        user = cpanel.get('user')
        token = cpanel.get('api_token')
        # Security: Default to True, allow config override
        verify_ssl = cpanel.get('verify_ssl', True)
        if not verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    except Exception as e:
        print(f"❌ Error loading vault: {e}")
        return

    # 2. Read Local index.html
    try:
        if os.path.exists('index.html'):
            with open('index.html', 'r') as f:
                html_content = f.read()
        else:
            html_content = "<html><body><h1>TravelKing OMEGA Deployment</h1></body></html>"
    except Exception as e:
        print(f"❌ Error reading index.html: {e}")
        return

    # 3. Use cPanel UAPI to save file
    # Function: Fileman::save_file_content
    url = f"https://{host}:2083/execute/Fileman/save_file_content"
    headers = {"Authorization": f"cpanel {user}:{token}"}
    
    params = {
        "dir": "public_html",
        "file": "index.html",
        "content": html_content
    }

    try:
        response = requests.get(url, headers=headers, params=params, verify=verify_ssl)
        result = response.json()
        
        if result.get('status') == 1:
            print("✅ DEPLOY SUCCESS: index.html is now LIVE on travelking.live!")
            print(f"🔗 URL: https://www.travelking.live")
        else:
            print(f"❌ DEPLOY FAILED: {result.get('errors')}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    deploy_to_cpanel()
