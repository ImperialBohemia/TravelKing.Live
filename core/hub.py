import json
import os
from core.connectors.google import GoogleConnector
from core.connectors.facebook import FacebookConnector
from core.connectors.server import CPanelConnector, BingConnector
from core.connectors.travelpayouts import TravelpayoutsConnector
from core.services.market_intel import MarketIntelService
from core.services.deployment import DeploymentService

class OmegaHub:
    """
    OMEGA HUB: The Enterprise Orchestrator.
    Manages all permanent connections and modular services.
    """
    def __init__(self):
        # 1. Load Vault (Permanent Credentials)
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        vault_path = os.path.join(self.base_dir, "config", "access_vault.json")
        with open(vault_path, "r") as f:
            self.vault = json.load(f)

        # 2. Initialize Connectors (Raw API Bridges)
        self.google = GoogleConnector(self.vault)
        self.facebook = FacebookConnector(self.vault)
        self.cpanel = CPanelConnector(self.vault)
        self.bing = BingConnector(self.vault)
        self.travelpayouts = TravelpayoutsConnector(self.vault)

        # 3. Initialize Services (Strategic Business Logic)
        self.market = MarketIntelService(self.google, self.bing)
        self.deployer = DeploymentService(self.cpanel, self.bing)
        
        print("💎 OMEGA HUB: Enterprise Modular Logic Active.")

    def status_check(self) -> dict:
        """Performs a comprehensive health check on all permanent connections."""
        print("🔍 OMEGA: Initiating Global Connection Audit...")
        return {
            "Google": "ACTIVE 🟢" if self.google.test_connection() else "OFFLINE 🔴",
            "Facebook": "ACTIVE 🟢" if self.facebook.test_connection() else "OFFLINE 🔴",
            "cPanel": "ACTIVE 🟢" if self.cpanel.test_connection() else "OFFLINE 🔴",
            "Bing": "ACTIVE 🟢" if self.bing.test_connection() else "OFFLINE 🔴",
            "Travelpayouts": "ACTIVE 🟢" if self.travelpayouts.test_connection() else "OFFLINE 🔴"
        }

hub = OmegaHub()
