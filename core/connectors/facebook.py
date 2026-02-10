"""
Facebook Graph API Connector — per official docs.

Docs: https://developers.facebook.com/docs/graph-api
API Version: v21.0
"""
import logging
import requests

from core.settings import load_vault, FACEBOOK_GRAPH_BASE_URL

logger = logging.getLogger(__name__)


class FacebookConnector:
    """Facebook Graph API bridge."""

    def __init__(self, vault: dict = None):
        self.vault = vault or load_vault()
        fb_cfg = self.vault.get("facebook", {})
        self.page_token = fb_cfg.get("page_token_topstroje", "")
        self.user_token = fb_cfg.get("access_token", "")

    def api_call(self, endpoint: str, method: str = "GET",
                 params: dict = None, use_page_token: bool = True) -> dict:
        """
        Make a Facebook Graph API call.
        Per: https://developers.facebook.com/docs/graph-api/using-graph-api
        """
        url = f"{FACEBOOK_GRAPH_BASE_URL}/{endpoint}"
        token = self.page_token if use_page_token else self.user_token
        if params is None:
            params = {}
        params["access_token"] = token

        response = requests.request(method, url, params=params)
        return response.json()

    def test_connection(self) -> dict:
        """Verify token validity via /debug_token endpoint."""
        try:
            result = self.api_call("me", params={"fields": "name,id"})
            if "error" in result:
                return {"status": "FAIL", "error": result["error"].get("message", "")}
            return {"status": "OK", "name": result.get("name"), "id": result.get("id")}
        except Exception as e:
            return {"status": "FAIL", "error": str(e)[:100]}
