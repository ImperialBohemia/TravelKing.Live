
import requests

class TravelpayoutsModule:
    """Independent Admin Bridge for Travelpayouts API."""
    def __init__(self, vault):
        self.marker = vault['travelpayouts']['marker']
        self.token = vault['travelpayouts']['token']
        self.session = requests.Session()
        self.session.headers.update({"X-Access-Token": self.token})

    def call(self, endpoint, method="GET", params=None, data=None):
        url = f"https://api.travelpayouts.com/{endpoint}"
        p = params or {}
        # Some endpoints might require marker in params
        # p["marker"] = self.marker
        res = self.session.request(method, url, params=p, json=data)
        return res.json()
