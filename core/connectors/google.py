
import json
import requests
import os
import logging

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
        res = requests.post(url, data=data).json()
        if "access_token" in res:
            self.token = res["access_token"]
            return True
        return False

    def call(self, endpoint, method="GET", data=None, base="https://www.googleapis.com"):
        url = f"{base}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}
        res = requests.request(method, url, headers=headers, json=data)
        if res.status_code == 401 and self.refresh():
            return self.call(endpoint, method, data, base)
        return res.json()

    def scan_boarding_pass(self, image_url):
        return self.call("v1/images:annotate", method="POST", data={"requests": [{"image": {"source": {"imageUri": image_url}}, "features": [{"type": "TEXT_DETECTION"}]}]})
