import json
import requests

class GoogleModule:
    """Independent Admin Bridge for all Google Services."""
    def __init__(self, vault):
        self.vault = vault
        self.token = vault['google']['access_token']
        self.refresh_token = vault['google']['refresh_token']
        self.client_id = "681255809395-oo8ft2oprdrnp9e3aqf6av3hmduib135j.apps.googleusercontent.com"

    def refresh(self):
        url = "https://oauth2.googleapis.com/token"
        data = {"client_id": self.client_id, "refresh_token": self.refresh_token, "grant_type": "refresh_token"}
        try:
            res = requests.post(url, data=data).json()
            if "access_token" in res:
                self.token = res["access_token"]
                return True
        except:
            pass
        return False

    def call(self, endpoint, method="GET", data=None, base="https://www.googleapis.com"):
        url = f"{base}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "developer-token": self.vault['google'].get('developer_token', ''),
            "login-customer-id": self.vault['google'].get('customer_id', '')
        }
        try:
            res = requests.request(method, url, headers=headers, json=data)
            if res.status_code == 401 and self.refresh():
                return self.call(endpoint, method, data, base)
            return res.json()
        except Exception as e:
            return {"error": str(e), "status_code": getattr(res, 'status_code', 0)}

    def get_keyword_intel(self, keyword):
        """Immortal Google Ads Keyword Intelligence."""
        # Use Google Ads API v17+ endpoint
        customer_id = self.vault['google'].get('customer_id', '')
        endpoint = f"v17/customers/{customer_id}/googleAds:searchStream"
        # Logic for keyword metrics would go here
        return self.call(endpoint, method="POST", base="https://googleads.googleapis.com")

    def scan_boarding_pass(self, image_url):
        return self.call("v1/images:annotate", method="POST", data={"requests": [{"image": {"source": {"imageUri": image_url}}, "features": [{"type": "TEXT_DETECTION"}]}]})
