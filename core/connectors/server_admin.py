
import requests
import logging

class CPanelAdmin:
    """Enterprise cPanel Admin bridge covering Files, DNS, and Databases."""
    
    def __init__(self, vault):
        self.cp = vault["cpanel"]
        self.base = f"https://{self.cp['host']}:2083/execute"
        self.headers = {"Authorization": f"cpanel {self.cp['user']}:{self.cp['api_token']}"}
        self.session = requests.Session()

    def call(self, module, function, params=None):
        url = f"{self.base}/{module}/{function}"
        res = self.session.get(url, headers=self.headers, params=params, verify=False)
        return res.json()

class BingAdmin:
    """Direct Bing Webmaster Admin for instant indexing and keyword intel."""
    
    def __init__(self, vault):
        self.api_key = vault["bing"]["api_key"]
        self.session = requests.Session()

    def call(self, endpoint, method="GET", data=None):
        url = f"https://ssl.bing.com/webmaster/api.svc/json/{endpoint}?apikey={self.api_key}"
        res = self.session.request(method, url, json=data)
        return res.json()
