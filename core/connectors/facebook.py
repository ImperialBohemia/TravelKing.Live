import requests
from core.base.connector import BaseConnector

class FacebookConnector(BaseConnector):
    """
    Enterprise Facebook Graphics & Ads Connector (OMEGA Architecture).
    Permanent link using long-lived Page Access Tokens.
    """
    def __init__(self, vault):
        super().__init__("Facebook", vault.get("facebook", {}))
        self.page_token = self.config.get("page_token_topstroje")
        self.user_token = self.config.get("access_token")
        self.version = "v21.0"

    def test_connection(self) -> bool:
        """Verifies Facebook connection by fetching page details."""
        res = self.api_call("me")
        return isinstance(res, dict) and "error" not in res

    def api_call(self, endpoint, method="GET", params=None, use_page_token=True):
        """Standardized Facebook Graph API caller."""
        token = self.page_token if use_page_token else self.user_token
        url = f"https://graph.facebook.com/{self.version}/{endpoint}"
        p = params or {}
        p["access_token"] = token
        # self.call uses the session from BaseConnector
        return self.call(method, url, params=p)
