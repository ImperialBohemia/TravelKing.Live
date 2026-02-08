
import json
import requests
import os

class UniversalConnector:
    """The OMEGA Bridge: Permanent access to Google, Facebook, and cPanel."""
    
    def __init__(self, vault_path="/home/q/Gemini CLI/access_vault.json"):
        with open(vault_path, "r") as f:
            self.vault = json.load(f)
        self.google_token = self.vault["google"]["access_token"]
        self.fb_token = self.facebook_token = self.vault["facebook"]["access_token"]
        self.cp = self.vault["cpanel"]
        self.cp_base = f"https://{self.cp['host']}:2083/execute"
        self.cp_headers = {"Authorization": f"cpanel {self.cp['user']}:{self.cp['api_token']}"}

    def google_call(self, endpoint, method="GET", data=None):
        url = f"https://www.googleapis.com/{endpoint}"
        headers = {"Authorization": f"Bearer {self.google_token}"}
        return requests.request(method, url, headers=headers, json=data).json()

    def facebook_call(self, endpoint, method="GET", params=None):
        url = f"https://graph.facebook.com/v21.0/{endpoint}"
        p = params or {}
        p["access_token"] = self.fb_token
        return requests.request(method, url, params=p).json()

    def cpanel_call(self, module, function, params=None):
        url = f"{self.cp_base}/{module}/{function}"
        return requests.get(url, headers=self.cp_headers, params=params, verify=False).json()

# Global Instance for AI use
bridge = UniversalConnector()
