
import json
import os
import requests
import subprocess
from loguru import logger
import time

ROOT = "/home/q/TravelKing.Live"
VAULT_PATH = "/home/q/TravelKing.Live/config/access_vault.json"

def load_vault():
    with open(VAULT_PATH, "r") as f:
        return json.load(f)

def check_google_ai():
    logger.info("🧪 Testing Google AI (Gemini)...")
    try:
        from ai.logic.brain import Brain
        brain = Brain()
        if brain.mode != "Dumb":
            return True, f"Success ({brain.mode})"
        return False, "Auth Failed"
    except Exception as e:
        return False, str(e)

def check_google_drive():
    logger.info("🧪 Testing Google Drive Access...")
    try:
        from services.google.drive_handler import DriveHandler
        drive = DriveHandler()
        # Just try to list something or check quota if possible, or just init
        return True, "Initialized"
    except Exception as e:
        return False, str(e)

def check_cpanel(vault):
    logger.info("🧪 Testing cPanel API...")
    try:
        cfg = vault['cpanel']
        url = f"https://{cfg['host']}:2083/execute/DomainInfo/domains_data"
        headers = {"Authorization": f"cpanel {cfg['user']}:{cfg['api_token']}"}
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            return True, f"Connected as {cfg['user']}"
        return False, f"Status {res.status_code}"
    except Exception as e:
        return False, str(e)

def check_facebook(vault):
    logger.info("🧪 Testing Facebook Graph API...")
    try:
        cfg = vault['facebook']
        url = f"https://graph.facebook.com/v19.0/me?access_token={cfg['access_token']}"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            return True, "Token Valid"
        return False, f"Status {res.status_code} (Expired/Invalid)"
    except Exception as e:
        return False, str(e)

def check_bing(vault):
    logger.info("🧪 Testing Bing / IndexNow...")
    try:
        api_key = vault['bing']['api_key']
        # Bing doesn't have a simple 'ping' without a site, but we can check if the key looks valid
        if len(api_key) == 32:
            return True, "Key format valid"
        return False, "Invalid key format"
    except Exception as e:
        return False, str(e)

def check_travelpayouts(vault):
    logger.info("🧪 Testing Travelpayouts API...")
    try:
        token = vault['travelpayouts']['api_token']
        url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
        params = {'origin': 'PRG', 'destination': 'LON', 'token': token, 'limit': 1}
        res = requests.get(url, params=params, timeout=10)
        if res.status_code == 200:
            return True, "Connected"
        return False, f"Status {res.status_code}"
    except Exception as e:
        return False, str(e)

def check_github(vault):
    logger.info("🧪 Testing GitHub Token...")
    try:
        token = vault['github']['token']
        headers = {"Authorization": f"token {token}"}
        res = requests.get("https://api.github.com/user", headers=headers, timeout=10)
        if res.status_code == 200:
            user = res.json()['login']
            return True, f"Connected as {user}"
        return False, f"Status {res.status_code}"
    except Exception as e:
        return False, str(e)

def check_playwright():
    logger.info("🧪 Testing Playwright / Browser Engine...")
    try:
        # Check if browsers are installed
        res = subprocess.run(["playwright", "--version"], capture_output=True, text=True)
        if res.returncode == 0:
            return True, res.stdout.strip()
        return False, "Not installed"
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    vault = load_vault()
    
    results = {
        "Google AI": check_google_ai(),
        "Google Drive": check_google_drive(),
        "cPanel": check_cpanel(vault),
        "Facebook": check_facebook(vault),
        "Bing/IndexNow": check_bing(vault),
        "Travelpayouts": check_travelpayouts(vault),
        "GitHub": check_github(vault),
        "Playwright": check_playwright()
    }
    
    print("\n" + "="*50)
    print("💎 ANTIGRAVITY ENTERPRISE - FULL SYSTEM AUDIT")
    print("="*50)
    
    for service, (status, detail) in results.items():
        icon = "✅" if status else "❌"
        print(f"{icon} {service:<15} : {detail}")
    print("="*50)
