"""
OMEGA Indexing Client - Gold Standard
Official Docs: https://developers.google.com/search/apis/indexing-api/v3/reference
"""

import requests
import logging
from typing import List

class IndexingClient:
    """Push URLs to Google Search instantly with Batch support."""

    API_URL = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    BATCH_URL = "https://indexing.googleapis.com/batch"

    def __init__(self, access_token: str):
        self.token = access_token
        self.logger = logging.getLogger("OMEGA.Indexing")

    @property
    def headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def submit_url(self, url: str, action: str = "URL_UPDATED") -> dict:
        """Submit a single URL."""
        body = {"url": url, "type": action}
        res = requests.post(
            self.API_URL,
            headers={**self.headers, "Content-Type": "application/json"},
            json=body
        )
        if res.status_code == 200:
            self.logger.info(f"IndexingClient: URL submitted: {url}")
            return {"success": True, **res.json()}
        return {"success": False, "error": res.json()}

    def submit_batch(self, urls: List[str], action: str = "URL_UPDATED") -> dict:
        """Submit up to 100 URLs in a single multipart batch."""
        boundary = "===OMEGA_BATCH==="
        body_parts = []

        for i, url in enumerate(urls[:100]):
            part = f"--{boundary}\n"                    f"Content-Type: application/http\n"                    f"Content-ID: <item{i}>\n\n"                    f"POST /v3/urlNotifications:publish HTTP/1.1\n"                    f"Content-Type: application/json\n\n"                    f'{{"url": "{url}", "type": "{action}"}}\n'
            body_parts.append(part)

        body_parts.append(f"--{boundary}--")
        body = "".join(body_parts)

        res = requests.post(
            self.BATCH_URL,
            headers={
                **self.headers,
                "Content-Type": f"multipart/mixed; boundary={boundary}"
            },
            data=body
        )

        if res.status_code == 200:
            self.logger.info(f"IndexingClient: Batch of {len(urls[:100])} URLs submitted.")
            return {"success": True, "count": len(urls[:100])}
        return {"success": False, "error": res.text}
