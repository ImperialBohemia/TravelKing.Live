
import json
import os
from core.connectors.google import GoogleModule
from core.connectors.facebook import FacebookModule
from core.connectors.server import ServerModule
from core.logic.market import MarketEngine

class OmegaHub:
    """The Maximum Modular Central Hub."""
    def __init__(self):
        # 1. Load Vault
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        vault_path = os.path.join(self.base_dir, "config", "access_vault.json")
        with open(vault_path, "r") as f:
            self.vault = json.load(f)

        # 2. Connectors (Modules)
        self.google = GoogleModule(self.vault)
        self.facebook = FacebookModule(self.vault)
        self.server = ServerModule(self.vault)

        # 3. Logic (Engines)
        self.market = MarketEngine(self.google, self.server)
        
        print("💎 OMEGA HUB: Maximum Modular Logic Active.")

hub = OmegaHub()
