"""
cPanel UAPI Connector — per official docs.

Docs: https://api.docs.cpanel.net/cpanel/introduction/
Auth: cPanel API Token
"""
import logging
import requests
import urllib3

from core.settings import load_vault

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)


class CPanelConnector:
    """cPanel UAPI bridge."""

    def __init__(self, vault: dict = None):
        self.vault = vault or load_vault()
        cp_cfg = self.vault.get("cpanel", {})
        self.host = cp_cfg.get("host", "")
        self.user = cp_cfg.get("user", "")
        self.api_token = cp_cfg.get("api_token", "")
        self.base_url = f"https://{self.host}:2083/execute"
        self.headers = {"Authorization": f"cpanel {self.user}:{self.api_token}"}

    def uapi_call(self, module: str, function: str, params: dict = None) -> dict:
        """
        Call a cPanel UAPI endpoint.
        Per: https://api.docs.cpanel.net/cpanel/introduction/
        """
        url = f"{self.base_url}/{module}/{function}"
        response = requests.get(
            url, headers=self.headers, params=params or {},
            verify=False, timeout=15
        )
        response.raise_for_status()
        return response.json()

    def api2_call(self, module: str, function: str, params: dict = None) -> dict:
        """
        Call a cPanel API2 endpoint (for functions not in UAPI).
        Per: cPanel API2 docs
        """
        url = (
            f"https://{self.host}:2083/json-api/cpanel"
            f"?cpanel_jsonapi_version=2"
            f"&cpanel_jsonapi_module={module}"
            f"&cpanel_jsonapi_func={function}"
        )
        response = requests.get(
            url, headers=self.headers, params=params or {},
            verify=False, timeout=15
        )
        response.raise_for_status()
        return response.json()

    def list_files(self, directory: str) -> list:
        """List files in a cPanel directory."""
        result = self.uapi_call("Fileman", "list_files", {"dir": directory})
        return result.get("data", []) or []

    def get_file_content(self, directory: str, filename: str) -> str:
        """Read file content from cPanel."""
        result = self.uapi_call("Fileman", "get_file_content", {
            "dir": directory, "file": filename
        })
        return result.get("data", {}).get("content", "")

    def save_file(self, directory: str, filename: str, content: str) -> dict:
        """Write file content to cPanel."""
        return requests.post(
            f"{self.base_url}/Fileman/save_file_content",
            headers=self.headers,
            data={
                "dir": directory,
                "file": filename,
                "content": content,
                "from_charset": "utf-8",
            },
            verify=False, timeout=15,
        ).json()

    def mkdir(self, parent: str, name: str) -> dict:
        """Create a directory on cPanel (uses API2)."""
        return self.api2_call("Fileman", "mkdir", {
            "dir": parent, "name": name
        })

    def get_domains(self) -> dict:
        """Get domain information."""
        return self.uapi_call("DomainInfo", "domains_data")

    def test_connection(self) -> dict:
        """Test cPanel connection by fetching domain info."""
        try:
            result = self.get_domains()
            if result.get("status") == 1:
                domain = result["data"]["main_domain"]["domain"]
                return {"status": "OK", "domain": domain}
            return {"status": "FAIL", "errors": result.get("errors")}
        except Exception as e:
            return {"status": "FAIL", "error": str(e)[:100]}
