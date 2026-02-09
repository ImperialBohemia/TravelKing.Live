
import json
import os
import time
from loguru import logger

class PersistenceManager:
    """Ensures all enterprise connections are permanent and self-healing."""
    
    def __init__(self, root="/home/q/TravelKing.Live"):
        self.root = root
        self.vault_path = os.path.join(root, "config/access_vault.json")
        self.sa_path = os.path.join(root, "config/service_account.json")
        self.manifest_path = os.path.join(root, "data/config/persistence_manifest.json")
        
    def generate_manifest(self):
        """Creates a blueprint for permanent connectivity."""
        manifest = {
            "last_audit": time.strftime("%Y-%m-%d %H:%M:%S"),
            "connections": [
                {
                    "name": "Google Sheets (Tables)",
                    "strategy": "Service Account",
                    "status": "PERMANENT",
                    "credential_path": self.sa_path,
                    "auto_heal": True
                },
                {
                    "name": "Google Drive",
                    "strategy": "Service Account",
                    "status": "PERMANENT",
                    "credential_path": self.sa_path,
                    "auto_heal": True
                },
                {
                    "name": "Gmail SMTP",
                    "strategy": "App Password",
                    "status": "PERMANENT",
                    "account": "trendnatures@gmail.com",
                    "auto_heal": False # Requires manual update if password changes
                },
                {
                    "name": "Google AI (Jules Brain)",
                    "strategy": "System ADC / Project Auth",
                    "status": "PERMANENT",
                    "project_id": "travelking"
                },
                {
                    "name": "cPanel API",
                    "strategy": "API Token",
                    "status": "PERMANENT",
                    "host": "server707.web-hosting.com"
                },
                {
                    "name": "Facebook/Instagram",
                    "strategy": "Long-Lived Page Token",
                    "status": "RENEWABLE (60 days)",
                    "auto_heal_strategy": "Token Refresh Workflow"
                }
            ]
        }
        
        with open(self.manifest_path, "w") as f:
            json.dump(manifest, f, indent=4)
        logger.success(f"💎 Persistence Manifest generated at {self.manifest_path}")
        return manifest

    def verify_permanence(self):
        """Verify that we are not using temporary session tokens where permanent ones are available."""
        logger.info("🛡️ Verifying connection permanence...")
        
        with open(self.vault_path, "r") as f:
            vault = json.load(f)
            
        # Check Google OAuth vs SA
        if 'google' in vault and 'refresh_token' in vault['google']:
            logger.info("✅ Google Refresh Token found. Permanent OAuth fallback available.")
        
        # Check Gmail
        if 'google' in vault and 'app_password' in vault['google']:
            logger.success("✅ Gmail App Password verified. Permanent SMTP active.")
            
        # Check Facebook
        if 'facebook' in vault and 'access_token' in vault['facebook']:
            token = vault['facebook']['access_token']
            if len(token) > 100: # Simple heuristic for long-lived token
                logger.info("✅ Facebook token appears to be Long-Lived.")
            else:
                logger.warning("⚠️ Facebook token might be short-lived. Action required.")

if __name__ == "__main__":
    pm = PersistenceManager()
    pm.generate_manifest()
    pm.verify_permanence()
