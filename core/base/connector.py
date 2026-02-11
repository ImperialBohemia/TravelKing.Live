import requests
import logging
from abc import ABC, abstractmethod

class BaseConnector(ABC):
    """
    Enterprise Base Connector for all OMEGA connections.
    Includes basic logging, error handling, and mandatory interface.
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config or {}
        # Security: Default to True, allow config override
        self.verify_ssl = self.config.get("verify_ssl", True)
        self.logger = logging.getLogger(f"OMEGA.{name}")
        self._setup_logging()

    def _setup_logging(self):
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    @abstractmethod
    def test_connection(self) -> bool:
        """Verify the connection is active."""
        return False

    def call(self, method, url, **kwargs):
        """Unified request handler with logging."""
        # Only add verify to kwargs if it's not the default (True)
        # to avoid breaking legacy tests that expect no verify param.
        if "verify" not in kwargs and self.verify_ssl is not True:
            kwargs["verify"] = self.verify_ssl

        try:
            self.logger.debug(f" {method} call to {url}")
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            self.logger.error(f"Connection error in {self.name}: {str(e)}")
            return {"error": str(e), "status": "failed"}
