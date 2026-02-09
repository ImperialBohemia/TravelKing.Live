import requests
from loguru import logger
from abc import ABC, abstractmethod
import sys

# Configure Loguru for Enterprise Observability
logger.remove()
logger.add(sys.stderr, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>", colorize=True)
logger.add("logs/enterprise.log", rotation="10 MB", retention="10 days", compression="zip")

class BaseConnector(ABC):
    """
    Enterprise Base Connector for all OMEGA connections.
    Includes structured logging via loguru and session reuse.
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.logger = logger.bind(module=name)
        self.session = requests.Session()
        self.logger.info(f"Connector {name} initialized.")

    @abstractmethod
    def test_connection(self) -> bool:
        """Verify the connection is active."""
        return False

    def call(self, method, url, **kwargs):
        """Unified request handler with structured logging."""
        try:
            self.logger.debug(f"{method} call to {url}")
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            self.logger.error(f"Connection error in {self.name}: {str(e)}")
            return {"error": str(e), "status": "failed"}
