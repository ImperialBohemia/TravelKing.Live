import requests
import logging

class CPanelAdmin:
    """Enterprise cPanel Admin bridge covering Files, DNS, and Databases."""
    
    def __init__(self, vault):
        self.cp = vault.get("cpanel", {})
        self.base = f"https://{self.cp.get('host')}:2083/execute"
        self.headers = {"Authorization": f"cpanel {self.cp.get('user')}:{self.cp.get('api_token')}"}
        # Security: Default to True, allow config override
        self.verify_ssl = self.cp.get("verify_ssl", True)

    def call(self, module, function, params=None):
        url = f"{self.base}/{module}/{function}"
        res = requests.get(url, headers=self.headers, params=params, verify=self.verify_ssl)
        return res.json()

class BingAdmin:
    """Direct Bing Webmaster Admin for instant indexing and keyword intel."""
    
    def __init__(self, vault):
        self.bing = vault.get("bing", {})
        self.api_key = self.bing.get("api_key")

    def call(self, endpoint, method="GET", data=None):
        url = f"https://ssl.bing.com/webmaster/api.svc/json/{endpoint}?apikey={self.api_key}"
        res = requests.request(method, url, json=data)
        return res.json()
