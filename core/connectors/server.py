import requests
import json
import logging
from core.base.connector import BaseConnector

class CPanelConnector(BaseConnector):
    """
    Enterprise cPanel API Connector (OMEGA Architecture).
    Permanent link for hosting and deployment management.
    """
    def __init__(self, vault):
        super().__init__("cPanel", vault.get("cpanel", {}))
        self.host = self.config.get("host")
        self.user = self.config.get("user")
        self.api_token = self.config.get("api_token")

    def test_connection(self) -> bool:
        """Verifies cPanel connection by fetching user stats."""
        res = self.uapi_call("StatsBar", "get_stats", {"display": "diskusage"})
        return isinstance(res, dict) and "status" in res and res["status"] != "failed"

    def uapi_call(self, module, function, params=None):
        """Standardized UAPI caller."""
        url = f"https://{self.host}:2083/execute/{module}/{function}"
        headers = {"Authorization": f"cpanel {self.user}:{self.api_token}"}
        return self.call("GET", url, headers=headers, params=params, verify=False)

class BingConnector(BaseConnector):
    """
    Enterprise Bing Webmaster & IndexNow Connector (OMEGA Architecture).
    Upgraded for Deep Data Extraction (Keyword Research & Search Trends).
    """
    def __init__(self, vault):
        super().__init__("Bing", vault.get("bing", {}))
        self.api_key = self.config.get("api_key")
        self.index_now_key = self.config.get("index_now_key")

    def test_connection(self) -> bool:
        """Verifies Bing connection by fetching site list."""
        url = f"https://ssl.bing.com/webmaster/api.svc/json/GetUserSites?apikey={self.api_key}"
        res = self.call("GET", url)
        return isinstance(res, dict) and "error" not in res

    def get_search_intelligence(self, query: str) -> dict:
        """Extracts search volume and trend data from Bing."""
        self.logger.info(f"📊 BING: Extracting intelligence for '{query}'...")
        # Official Bing Webmaster API for Keyword Research
        endpoint = f"GetKeywordStats?apikey={self.api_key}&query={query}&country=US&language=en-US"
        return self.call("GET", f"https://ssl.bing.com/webmaster/api.svc/json/{endpoint}")

    def api_call(self, endpoint, method="POST", data=None):
        """Standardized Bing API caller with BOM handling."""
        url = f"https://ssl.bing.com/webmaster/api.svc/json/{endpoint}?apikey={self.api_key}"
        try:
            response = self.session.request(method, url, json=data)
            response.raise_for_status()
            # Bing API sometimes returns a BOM (Byte Order Mark)
            return json.loads(response.text.lstrip('\ufeff')) if response.text else {}
        except Exception as e:
            self.logger.error(f"Bing API call failed: {e}")
            return {"error": str(e), "status": "failed"}
