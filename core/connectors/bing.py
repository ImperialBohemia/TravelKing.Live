"""
Bing IndexNow Connector — per official protocol spec.

Docs: https://www.indexnow.org/documentation
Supports: Bing, Seznam, and generic IndexNow endpoints.
"""
import logging
import requests

from core.settings import load_vault, INDEXNOW_ENGINES

logger = logging.getLogger(__name__)


class BingConnector:
    """IndexNow protocol implementation for Bing, Seznam, etc."""

    def __init__(self, vault: dict = None):
        self.vault = vault or load_vault()
        bing_cfg = self.vault.get("bing", {})
        self.api_key = bing_cfg.get("index_now_key", "")
        self.host = "travelking.live"

    def submit_url(self, url: str) -> dict:
        """
        Submit a single URL via IndexNow GET request.
        Per: https://www.indexnow.org/documentation
        """
        results = {}
        for engine in INDEXNOW_ENGINES:
            try:
                params = {
                    "url": url,
                    "key": self.api_key,
                }
                response = requests.get(engine, params=params, timeout=10)
                results[engine] = {
                    "status": response.status_code,
                    "ok": response.status_code in (200, 202),
                }
            except Exception as e:
                results[engine] = {"status": "ERROR", "error": str(e)[:80]}
        return results

    def submit_batch(self, urls: list) -> dict:
        """
        Submit multiple URLs via IndexNow POST request.
        Per: https://www.indexnow.org/documentation (batch endpoint)
        """
        payload = {
            "host": self.host,
            "key": self.api_key,
            "urlList": urls,
        }
        results = {}
        for engine in INDEXNOW_ENGINES:
            try:
                response = requests.post(
                    engine, json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=10,
                )
                results[engine] = {
                    "status": response.status_code,
                    "ok": response.status_code in (200, 202),
                }
            except Exception as e:
                results[engine] = {"status": "ERROR", "error": str(e)[:80]}
        return results

    def test_connection(self) -> dict:
        """Verify IndexNow key file is accessible on domain."""
        try:
            url = f"https://{self.host}/{self.api_key}.txt"
            response = requests.get(url, timeout=10)
            if response.status_code == 200 and self.api_key in response.text:
                return {"status": "OK", "key_verified": True}
            return {"status": "FAIL", "http_code": response.status_code}
        except Exception as e:
            return {"status": "FAIL", "error": str(e)[:100]}
