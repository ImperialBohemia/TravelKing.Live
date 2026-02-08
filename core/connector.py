import json
import requests
import os
import logging

# Configure logging for perfection
logging.basicConfig(
    filename='/home/q/Gemini CLI/logs/system.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class UniversalConnector:
    """The perfected OMEGA Bridge: Zero-latency access to Google, FB, and cPanel."""
    
    def __init__(self, vault_path="/home/q/Gemini CLI/config/access_vault.json"):
        if not os.path.exists(vault_path):
            logging.critical("Vault missing at path: " + vault_path)
            raise FileNotFoundError("Access vault not found.")
            
        with open(vault_path, "r") as f:
            self.vault = json.load(f)
            
        self.google_token = self.vault["google"]["access_token"]
        self.fb_token = self.vault["facebook"]["access_token"]
        self.cp = self.vault["cpanel"]
        self.cp_base = f"https://{self.cp['host']}:2083/execute"
        self.cp_headers = {"Authorization": f"cpanel {self.cp['user']}:{self.cp['api_token']}"}
        logging.info("UniversalConnector: All bridges established.")

    def google_call(self, endpoint, method="GET", data=None):
        url = f"https://www.googleapis.com/{endpoint}"
        headers = {"Authorization": f"Bearer {self.google_token}"}
        res = requests.request(method, url, headers=headers, json=data)
        logging.info(f"Google API Call: {endpoint} | Status: {res.status_code}")
        return res.json()

    def google_search_console_call(self, site_url, endpoint, method="GET", data=None):
        """Dedicated bridge for Google Search Console data extraction."""
        # URL encode the site_url for the API
        encoded_site = site_url.replace(":", "%3A").replace("/", "%2F")
        full_endpoint = f"webmasters/v3/sites/{encoded_site}/{endpoint}"
        return self.google_call(full_endpoint, method=method, data=data)

    def facebook_call(self, endpoint, method="GET", params=None):
        url = f"https://graph.facebook.com/v21.0/{endpoint}"
        p = params or {}
        p["access_token"] = self.fb_token
        res = requests.request(method, url, params=p)
        logging.info(f"Facebook API Call: {endpoint} | Status: {res.status_code}")
        return res.json()

    def bing_call(self, endpoint, method="POST", data=None):
        """Dedicated bridge for Bing Webmaster API (Instant Indexing)."""
        api_key = self.vault["bing"]["api_key"]
        url = f"https://ssl.bing.com/webmaster/api.svc/json/{endpoint}?apikey={api_key}"
        res = requests.request(method, url, json=data)
        logging.info(f"Bing API Call: {endpoint} | Status: {res.status_code}")
        return res.json()

    def cpanel_call(self, module, function, params=None):
        url = f"{self.cp_base}/{module}/{function}"
        res = requests.get(url, headers=self.cp_headers, params=params, verify=False)
        logging.info(f"cPanel API Call: {module}/{function} | Status: {res.status_code}")
        return res.json()

bridge = UniversalConnector()