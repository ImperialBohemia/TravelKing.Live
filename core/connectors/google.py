import sys
import json
import requests
import os
import logging
import subprocess

from core.base.connector import BaseConnector

class GoogleConnector(BaseConnector):
    """
    Independent Admin Bridge for all Google Services.
    Upgraded for Deep Data Extraction (Google Trends & Search Grounding).
    """
    def __init__(self, vault):
        super().__init__("Google", vault.get("google", {}))
        self.vault_full = vault
        self.root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.vault_full_path = os.path.join(self.root, 'config', 'access_vault.json')

        self.token = self.config.get('access_token')
        self.refresh_token = self.config.get('refresh_token')
        self.client_id = self.config.get("client_id", "1009428807876-seopbefn13ev9fnot0sdsh1018fp00iu.apps.googleusercontent.com")
        self.client_secret = self.config.get("client_secret", "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")

        # Dynamic SDK Path Detection
        home = os.path.expanduser("~")
        sdk_paths = [
            os.path.join(home, 'SimpleCodeSpace/venv/lib/python3.12/site-packages'),
            os.path.join(home, 'SimpleCodeSpace/.venv/lib/python3.12/site-packages')
        ]
        for path in sdk_paths:
            if os.path.exists(path) and path not in sys.path:
                sys.path.append(path)

    def test_connection(self) -> bool:
        """Verifies Google connection."""
        url = "https://www.googleapis.com/oauth2/v3/tokeninfo"
        try:
            res = self.session.get(url, params={"access_token": self.token})
            if res.status_code == 200:
                return True
            if self.refresh():
                res = self.session.get(url, params={"access_token": self.token})
                return res.status_code == 200
        except Exception as e:
            self.logger.error(f"Connection test failed: {e}")
        return False

    def get_market_trends(self, keyword: str) -> dict:
        """Extracts market interest signals via Google APIs."""
        self.logger.info(f"📊 GOOGLE: Fetching trends for '{keyword}'...")
        # Using Google Search Console or Trends API (Simulation)
        return self.api_call(
            "https://www.googleapis.com/customsearch/v1",
            params={"q": keyword, "num": 5}
        )

    def refresh(self) -> bool:
        """Refreshes the Google access token."""
        url = "https://oauth2.googleapis.com/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token"
        }
        try:
            res = self.session.post(url, data=data).json()
            if "access_token" in res:
                self.token = res["access_token"]
                self.vault_full['google']['access_token'] = self.token
                self._save_vault()
                return True
        except Exception as e:
            self.logger.error(f"Refresh failed: {e}")
        return False

    def _save_vault(self):
        """Internal helper to persist vault changes."""
        with open(self.vault_full_path, 'w') as f:
            json.dump(self.vault_full, f, indent=4)

    def api_call(self, url, method="GET", **kwargs):
        """Authenticated API call to Google Services."""
        if not self.token:
            self.refresh()
        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.token}"
        kwargs["headers"] = headers
        res = self.call(method, url, **kwargs)
        if isinstance(res, dict) and "error" in res:
            if "401" in str(res.get("error")) and self.refresh():
                return self.api_call(url, method, **kwargs)
        return res
