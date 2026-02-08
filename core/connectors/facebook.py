
import requests

class FacebookModule:
    """Independent Admin Bridge for Facebook Marketing & Pages."""
    def __init__(self, vault):
        self.token = vault['facebook']['page_token_topstroje']
        self.user_token = vault['facebook']['access_token']

    def call(self, endpoint, method="GET", params=None, use_page_token=True):
        token = self.token if use_page_token else self.user_token
        url = f"https://graph.facebook.com/v21.0/{endpoint}"
        p = params or {}
        p["access_token"] = token
        return requests.request(method, url, params=p).json()
