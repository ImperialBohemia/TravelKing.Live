
import requests
import logging

class FacebookAdmin:
    """Full-access Facebook Business & Marketing Admin bridge."""
    
    def __init__(self, vault):
        self.token = vault["facebook"]["access_token"]
        self.version = "v21.0"

    def call(self, endpoint, method="GET", params=None):
        url = f"https://graph.facebook.com/{self.version}/{endpoint}"
        p = params or {}
        p["access_token"] = self.token
        res = requests.request(method, url, params=p)
        return res.json()

    def get_ad_insights(self, ad_account_id):
        return self.call(f"{ad_account_id}/insights")
