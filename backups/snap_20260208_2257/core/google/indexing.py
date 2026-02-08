"""
OMEGA Indexing Client
Official Docs: https://developers.google.com/search/apis/indexing-api/v3/reference
Scope: https://www.googleapis.com/auth/indexing

Enterprise-grade Google Indexing API for instant URL submission.
"""

import requests
from typing import List


class IndexingClient:
    """Push URLs to Google Search instantly."""
    
    API_URL = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    BATCH_URL = "https://indexing.googleapis.com/batch"
    
    def __init__(self, access_token: str):
        self.token = access_token
        self.headers = {"Authorization": f"Bearer {self.token}"}
    
    def submit_url(self, url: str, action: str = "URL_UPDATED") -> dict:
        """
        Submit a single URL for indexing.
        
        Args:
            url: Full URL to index
            action: 'URL_UPDATED' or 'URL_DELETED'
            
        Returns:
            dict: API response
        """
        body = {"url": url, "type": action}
        
        response = requests.post(
            self.API_URL,
            headers={**self.headers, "Content-Type": "application/json"},
            json=body
        )
        
        if response.status_code == 200:
            return {"success": True, **response.json()}
        return {"success": False, "error": response.json()}
    
    def submit_batch(self, urls: List[str], action: str = "URL_UPDATED") -> dict:
        """
        Submit multiple URLs in a single batch request.
        
        Args:
            urls: List of URLs to index (max 100)
            action: 'URL_UPDATED' or 'URL_DELETED'
            
        Returns:
            dict: Batch response summary
        """
        # Build multipart batch request
        boundary = "===OMEGA_BATCH==="
        body_parts = []
        
        for i, url in enumerate(urls[:100]):
            part = f"""--{boundary}
Content-Type: application/http
Content-ID: <item{i}>

POST /v3/urlNotifications:publish HTTP/1.1
Content-Type: application/json

{{"url": "{url}", "type": "{action}"}}
"""
            body_parts.append(part)
        
        body_parts.append(f"--{boundary}--")
        body = "\n".join(body_parts)
        
        response = requests.post(
            self.BATCH_URL,
            headers={
                **self.headers,
                "Content-Type": f"multipart/mixed; boundary={boundary}"
            },
            data=body
        )
        
        return {
            "success": response.status_code == 200,
            "submitted": len(urls),
            "raw_response": response.text[:500]
        }
