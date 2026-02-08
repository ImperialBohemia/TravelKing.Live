
import requests
import json

class ServerModule:
    """Independent Admin Bridge for cPanel and Bing Search."""
    def __init__(self, vault):
        self.cp = vault['cpanel']
        self.bing_key = vault['bing']['api_key']
        self.index_now_key = vault['bing']['index_now_key']
        self.session = requests.Session()

    def cpanel_call(self, module, function, params=None):
        url = f"https://{self.cp['host']}:2083/execute/{module}/{function}"
        headers = {"Authorization": f"cpanel {self.cp['user']}:{self.cp['api_token']}"}
        return self.session.get(url, headers=headers, params=params, verify=False).json()

    def bing_call(self, endpoint, method="GET", data=None):
        url = f"https://ssl.bing.com/webmaster/api.svc/json/{endpoint}?apikey={self.bing_key}"
        res = self.session.request(method, url, json=data)
        return json.loads(res.text.lstrip('\ufeff')) if res.text else {}
