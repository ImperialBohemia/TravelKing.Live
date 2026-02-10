
import json
import os
import requests
import sys
import time
import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime
from loguru import logger

class Guardian:
    """Enterprise-grade monitor & self-healing service for TravelKing.Live."""
    
    def __init__(self, root_dir="/home/q/TravelKing.Live"):
        self.root = root_dir
        if self.root not in sys.path:
            sys.path.append(self.root)
        self.config_dir = os.path.join(self.root, "data/config")
        self.vault_path = os.path.join(self.root, "config/access_vault.json")
        self.google_auth_path = os.path.join(self.config_dir, "google_auth.json")
        self.status_path = os.path.join(self.root, "data/logs/guardian_status.json")

    def perform_health_check(self):
        """Deep Audit of ALL enterprise connections via Connection Fortress."""
        logger.info("🛡️ Guardian: Initiating OMEGA AUDIT via Connection Fortress...")
        
        try:
            from core.fortress.daemon import ConnectionFortress
            fortress = ConnectionFortress()
            fortress_results = fortress.run_full_check()
            
            # Guardian results format (legacy compatibility)
            results = {
                "timestamp": fortress_results["timestamp"],
                "services": {}
            }
            
            # Map fortress services to guardian keys
            services = fortress_results["services"]
            
            # Google mapping
            google_status = "PERFECT" if services.get("google_service_account", {}).get("status") == "PERMANENT" else "FAILED"
            results["services"]["google_sheets"] = {"status": google_status, "details": services.get("google_service_account", {}).get("detail")}
            results["services"]["google_drive"] = {"status": google_status, "details": services.get("google_drive", {}).get("detail")}
            
            gmail_data = services.get("google_gmail_smtp", {})
            results["services"]["gmail"] = {"status": "PERFECT" if gmail_data.get("status") == "PERMANENT" else "FAILED", "details": gmail_data.get("detail")}
            
            # Facebook
            fb_data = services.get("facebook", {})
            results["services"]["facebook"] = {"status": "PERFECT" if fb_data.get("status") == "ACTIVE" else "FAILED", "details": fb_data.get("detail")}
            
            # cPanel
            cp_data = services.get("cpanel", {})
            results["services"]["cpanel"] = {"status": "PERFECT" if cp_data.get("status") == "PERMANENT" else "FAILED", "details": cp_data.get("detail")}
            
            # Travelpayouts
            tp_data = services.get("travelpayouts", {})
            results["services"]["travelpayouts"] = {"status": "PERFECT" if tp_data.get("status") == "PERMANENT" else "FAILED", "details": tp_data.get("detail")}
            
            # GitHub
            gh_data = services.get("github", {})
            results["services"]["github"] = {"status": "PERFECT" if gh_data.get("status") == "ACTIVE" else "FAILED", "details": gh_data.get("detail")}
            
            # Bing
            bi_data = services.get("bing", {})
            results["services"]["bing"] = {"status": "PERFECT" if bi_data.get("status") == "PERMANENT" else "FAILED", "details": bi_data.get("detail")}

            # AI check still needs its own logic if not in fortress
            results["services"]["google_ai"] = self._check_google_ai()

            # Save status for Dashboard integration
            with open(self.status_path, "w") as f:
                json.dump(results, f, indent=4)
                
            logger.success("🛡️ Guardian: Full System Audit Complete (Sync with Fortress).")
            return results
            
        except Exception as e:
            logger.error(f"Guardian audit failed: {e}")
            return {"error": str(e)}

    def update_dashboard(self, results):
        """Dashboard update is now part of ConnectionFortress.run_full_check()."""
        pass

    def _check_google_ai(self):
        """Checks Gemini AI connectivity."""
        try:
            # Simple check for Brain module
            from ai.logic.brain import Brain
            brain = Brain()
            if brain.mode != "Dumb":
                return {"status": "PERFECT", "details": f"Connected ({brain.mode})"}
            return {"status": "FAILED", "error": "Auth Failed"}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

if __name__ == "__main__":
    g = Guardian()
    print(json.dumps(g.perform_health_check(), indent=2))
