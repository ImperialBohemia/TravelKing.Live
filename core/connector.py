
import json
import os
from core.connectors.google_admin import GoogleAdmin
from core.connectors.facebook_admin import FacebookAdmin
from core.connectors.server_admin import CPanelAdmin, BingAdmin

class UniversalAdminConnector:
    """The master orchestrator for all Admin connections."""
    
    def __init__(self, vault_path="/home/q/Gemini CLI/config/access_vault.json"):
        with open(vault_path, "r") as f:
            vault = json.load(f)
        
        # Modular Admin Initializations
        self.google = GoogleAdmin(vault)
        self.facebook = FacebookAdmin(vault)
        self.cpanel = CPanelAdmin(vault)
        self.bing = BingAdmin(vault)
        
        print("👑 Universal Admin Connector: All systems nominal.")

# Single Global Instance
bridge = UniversalAdminConnector()
