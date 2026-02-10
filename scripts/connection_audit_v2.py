import sys
import os
import json
import logging
import requests

# Ensure project root is in sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from core.hub import OmegaHub
from core.connectors.google_admin import GoogleAdmin

def audit():
    print("💎 OMEGA COMPREHENSIVE CONNECTION AUDIT 💎")
    print("-" * 50)

    try:
        # Suppress insecure request warnings for cPanel
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        hub = OmegaHub()
        vault = hub.vault
    except Exception as e:
        print(f"❌ CRITICAL: Failed to initialize OmegaHub: {e}")
        return

    # 1. Basic Status Check from Hub
    print("\n--- [1] CORE HUB STATUS ---")
    try:
        hub_status = hub.status_check()
        for service, status in hub_status.items():
            print(f"{service:15}: {status}")
    except Exception as e:
        print(f"Hub Status Check Error: {e}")

    # 2. Detailed Google Audit
    print("\n--- [2] DETAILED GOOGLE AUDIT ---")
    try:
        google_ok = hub.google.test_connection()
        print(f"Google Main    : {'🟢 ACTIVE' if google_ok else '🔴 OFFLINE'}")
    except Exception as e:
        print(f"Google Audit Error: {e}")

    # 3. Google Admin Check
    print("\n--- [3] GOOGLE ADMIN AUDIT ---")
    try:
        g_admin = GoogleAdmin(vault)
        user_info = g_admin.call("oauth2/v2/userinfo")
        if isinstance(user_info, dict) and "email" in user_info:
            print(f"Google Admin   : 🟢 ACTIVE ({user_info['email']})")
        else:
            print(f"Google Admin   : 🔴 FAILED")
    except Exception as e:
        print(f"Google Admin   : 🔴 ERROR: {e}")

    # 4. Facebook Detailed Audit
    print("\n--- [4] FACEBOOK AUDIT ---")
    try:
        fb_ok = hub.facebook.test_connection()
        print(f"Facebook       : {'🟢 ACTIVE' if fb_ok else '🔴 FAILED'}")
    except Exception as e:
        print(f"Facebook Audit Error: {e}")

    # 5. cPanel Audit
    print("\n--- [5] CPANEL AUDIT ---")
    try:
        if hub.cpanel.test_connection():
            print(f"cPanel         : 🟢 ACTIVE ({hub.cpanel.user}@{hub.cpanel.host})")
        else:
            print(f"cPanel         : 🔴 FAILED")
    except Exception as e:
        print(f"cPanel Audit Error: {e}")

    # 6. Bing Audit
    print("\n--- [6] BING AUDIT ---")
    try:
        if hub.bing.test_connection():
             print(f"Bing Webmaster : 🟢 ACTIVE")
        else:
             print(f"Bing Webmaster : 🔴 FAILED")
    except Exception as e:
        print(f"Bing Audit Error: {e}")

    # 7. Travelpayouts Audit
    print("\n--- [7] TRAVELPAYOUTS AUDIT ---")
    try:
        tp_ok = hub.travelpayouts.test_connection()
        print(f"Travelpayouts  : {'🟢 ACTIVE' if tp_ok else '🔴 FAILED'}")
    except Exception as e:
        print(f"Travelpayouts Audit Error: {e}")

    # 8. Gemini AI Audit
    print("\n--- [8] GEMINI AI AUDIT ---")
    api_key = vault.get("google", {}).get("api_key")
    project_id = vault.get("google", {}).get("project_id")

    if api_key:
        print(f"Mode           : GOOGLE AI STUDIO (Free)")
    elif project_id:
        print(f"Mode           : VERTEX AI (Enterprise/Paid)")
    else:
        print(f"Mode           : UNKNOWN (No credentials)")

    try:
        res = hub.gemini.generate_content("Say 'Gemini Active'")
        if res and "Error" not in res:
            print(f"Gemini Status  : 🟢 ACTIVE")
        else:
            print(f"Gemini Status  : 🔴 FAILED")
    except Exception as e:
        print(f"Gemini Status  : 🔴 ERROR: {e}")

    # 9. GitHub Audit
    print("\n--- [9] GITHUB AUDIT ---")
    try:
        gh_cfg = vault.get("github", {})
        gh_token = gh_cfg.get("token")
        if gh_token:
            headers = {"Authorization": f"token {gh_token}"}
            resp = requests.get("https://api.github.com/user", headers=headers)
            if resp.status_code == 200:
                print(f"GitHub         : 🟢 ACTIVE ({resp.json().get('login')})")
            else:
                print(f"GitHub         : 🔴 FAILED")
        else:
            print(f"GitHub         : ⚪ NOT CONFIGURED")
    except Exception as e:
        print(f"GitHub Audit Error: {e}")

if __name__ == "__main__":
    audit()
