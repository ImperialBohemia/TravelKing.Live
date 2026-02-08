
import json
import requests
import logging
import os

class GoogleAdmin:
    """High-privilege Google Admin bridge with automatic token refresh."""
    
    def __init__(self, vault):
        self.vault = vault
        self.token = vault["google"]["access_token"]
        self.refresh_token = vault["google"].get("refresh_token")
        self.client_id = "681255809395-oo8ft2oprdrnp9e3aqf6av3hmduib135j.apps.googleusercontent.com" # From token info

    def refresh_access_token(self):
        """Uses the refresh_token to get a new access_token if expired."""
        logging.info("GoogleAdmin: Refreshing access token...")
        url = "https://oauth2.googleapis.com/token"
        data = {
            "client_id": self.client_id,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token"
        }
        res = requests.post(url, data=data).json()
        if "access_token" in res:
            self.token = res["access_token"]
            # Update vault locally
            self.vault["google"]["access_token"] = self.token
            current_dir = os.path.dirname(os.path.abspath(__file__))
            root = os.path.abspath(os.path.join(current_dir, "..", ".."))
            vault_path = os.path.join(root, "config", "access_vault.json")
            with open(vault_path, "w") as f:
                json.dump(self.vault, f, indent=4)
            logging.info("GoogleAdmin: Token refreshed successfully.")
            return True
        return False

    def call(self, endpoint, method="GET", data=None):
        url = f"https://www.googleapis.com/{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}
        res = requests.request(method, url, headers=headers, json=data)
        
        if res.status_code == 401: # Unauthorized/Expired
            if self.refresh_access_token():
                return self.call(endpoint, method, data)
        
        return res.json()
