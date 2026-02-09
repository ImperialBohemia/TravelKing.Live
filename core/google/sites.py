"""
OMEGA Google Sites Client via Drive API
Official Docs: https://developers.google.com/drive/api/v3/reference
Scope: https://www.googleapis.com/auth/drive

Enterprise-grade Google Sites management through Drive API.
"""

import requests
from typing import Optional, List


class SitesClient:
    """Manage Google Sites via Drive API."""
    
    BASE_URL = "https://www.googleapis.com/drive/v3"
    SITES_MIME_TYPE = "application/vnd.google-apps.site"
    
    def __init__(self, access_token: str):
        self.token = access_token
        self.headers = {"Authorization": f"Bearer {self.token}"}
    
    def list_sites(self, limit: int = 100) -> list:
        """
        List all Google Sites accessible to the user.
        
        Args:
            limit: Max sites to return
            
        Returns:
            list: List of site metadata dicts
        """
        url = f"{self.BASE_URL}/files"
        params = {
            "pageSize": limit,
            "q": f"mimeType='{self.SITES_MIME_TYPE}'",
            "fields": "files(id,name,webViewLink,createdTime,modifiedTime)"
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code == 200:
            return response.json().get("files", [])
        return []
    
    def create_site(self, name: str) -> dict:
        """
        Create a new Google Site.
        
        Args:
            name: Name for the new site
            
        Returns:
            dict: Site metadata including ID and URL
        """
        url = f"{self.BASE_URL}/files"
        metadata = {
            "name": name,
            "mimeType": self.SITES_MIME_TYPE
        }
        
        response = requests.post(
            url,
            headers={**self.headers, "Content-Type": "application/json"},
            json=metadata
        )
        
        if response.status_code == 200:
            return {"success": True, **response.json()}
        return {"success": False, "error": response.json()}
    
    def share_site(self, site_id: str, email: str, role: str = "reader") -> dict:
        """
        Share a Google Site with a user.
        
        Args:
            site_id: The Drive file ID of the site
            email: Email address to share with
            role: 'reader', 'writer', or 'owner'
            
        Returns:
            dict: Permission metadata
        """
        url = f"{self.BASE_URL}/files/{site_id}/permissions"
        permission = {
            "type": "user",
            "role": role,
            "emailAddress": email
        }
        
        response = requests.post(
            url,
            headers={**self.headers, "Content-Type": "application/json"},
            json=permission
        )
        
        if response.status_code == 200:
            return {"success": True, **response.json()}
        return {"success": False, "error": response.json()}
    
    def make_public(self, site_id: str) -> str:
        """
        Make a Google Site publicly accessible.
        
        Args:
            site_id: The Drive file ID of the site
            
        Returns:
            str: Public URL
        """
        url = f"{self.BASE_URL}/files/{site_id}/permissions"
        permission = {"role": "reader", "type": "anyone"}
        
        response = requests.post(
            url,
            headers={**self.headers, "Content-Type": "application/json"},
            json=permission
        )
        
        if response.status_code == 200:
            # Get the site URL
            site_url = self.get_site_url(site_id)
            return site_url
        return None
    
    def get_site_url(self, site_id: str) -> str:
        """
        Get the web URL for a Google Site.
        
        Args:
            site_id: The Drive file ID of the site
            
        Returns:
            str: Site URL
        """
        url = f"{self.BASE_URL}/files/{site_id}"
        params = {"fields": "webViewLink"}
        
        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code == 200:
            return response.json().get("webViewLink", "")
        return ""
    
    def delete_site(self, site_id: str) -> bool:
        """
        Delete a Google Site.
        
        Args:
            site_id: The Drive file ID of the site
            
        Returns:
            bool: Success status
        """
        url = f"{self.BASE_URL}/files/{site_id}"
        response = requests.delete(url, headers=self.headers)
        return response.status_code == 204
