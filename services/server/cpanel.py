import requests
import json
import os
import logging
import urllib3

class CPanelConnector:
    """Modular Service Layer for cPanel UAPI & API2 Interaction."""

    def __init__(self, config_file="data/config/cpanel.json"):
        self.config_file = config_file
        self._load_config()

    def _load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                self.cfg = json.load(f)
            self.base = f"https://{self.cfg['host']}:{self.cfg.get('port', '2083')}"
            self.auth = {
                "Authorization": f"cpanel {self.cfg['user']}:{self.cfg['api_token']}"
            }
            # Security: Default to True, allow config override
            self.verify_ssl = self.cfg.get("verify_ssl", True)
            if not self.verify_ssl:
                # Disable warnings only if user explicitly opted out of SSL verification
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        else:
            self.cfg = None
            self.verify_ssl = True

    def call_uapi(self, module, func, params=None):
        """Execute modern UAPI functions."""
        if not self.cfg:
            return None
        url = f"{self.base}/execute/{module}/{func}"
        try:
            res = requests.get(url, params=params, headers=self.auth, verify=self.verify_ssl, timeout=30)
            return res.json()
        except Exception as e:
            logging.error(f"UAPI error: {e}")
            return None

    def call_api2(self, module, func, params=None):
        """Execute legacy API2 functions."""
        if not self.cfg:
            return None
        url = f"{self.base}/json-api/cpanel"
        payload = {
            "cpanel_jsonapi_apiversion": "2",
            "cpanel_jsonapi_module": module,
            "cpanel_jsonapi_func": func,
            **(params or {}),
        }
        try:
            res = requests.get(url, params=payload, headers=self.auth, verify=self.verify_ssl, timeout=30)
            return res.json()
        except Exception as e:
            logging.error(f"API2 error: {e}")
            return None
