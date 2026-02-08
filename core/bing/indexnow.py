"""
OMEGA IndexNow Client
Official Docs: https://www.indexnow.org/documentation

Enterprise-grade IndexNow implementation for instant Bing/Yandex/Seznam indexing.
UNLIMITED quota - no rate limits.
"""

import requests
from typing import List


class IndexNowClient:
    """Instant URL indexing via IndexNow protocol."""
    
    # IndexNow endpoints (all accept the same protocol)
    ENDPOINTS = [
        "https://www.bing.com/indexnow",
        "https://yandex.com/indexnow",
        "https://search.seznam.cz/indexnow"
    ]
    
    def __init__(self, api_key: str, host: str = "travelking.live"):
        """
        Initialize IndexNow client.
        
        Args:
            api_key: Your IndexNow API key (also filename at root)
            host: Your domain
        """
        self.api_key = api_key
        self.host = host
        self.key_location = f"https://{host}/{api_key}.txt"
    
    def submit_url(self, url: str) -> dict:
        """
        Submit a single URL to all IndexNow endpoints.
        
        Args:
            url: Full URL to index
            
        Returns:
            dict: Results from each endpoint
        """
        results = {}
        
        for endpoint in self.ENDPOINTS:
            response = requests.get(endpoint, params={
                "url": url,
                "key": self.api_key
            })
            
            engine = endpoint.split("//")[1].split(".")[0]
            results[engine] = response.status_code in [200, 202]
        
        return results
    
    def submit_batch(self, urls: List[str]) -> dict:
        """
        Submit multiple URLs via POST (more efficient).
        
        Args:
            urls: List of URLs to index
            
        Returns:
            dict: Results from each endpoint
        """
        body = {
            "host": self.host,
            "key": self.api_key,
            "keyLocation": self.key_location,
            "urlList": urls
        }
        
        results = {}
        
        for endpoint in self.ENDPOINTS:
            response = requests.post(
                endpoint,
                headers={"Content-Type": "application/json"},
                json=body
            )
            
            engine = endpoint.split("//")[1].split(".")[0]
            results[engine] = response.status_code in [200, 202]
        
        return {"submitted": len(urls), "results": results}
