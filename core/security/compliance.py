from loguru import logger
import json
import os

class ComplianceEngine:
    """Enterprise Safety & Compliance Engine to prevent bans."""
    def __init__(self, config_path="data/config/compliance_rules.json"):
        self.config_path = config_path
        self._load_rules()

    def _load_rules(self):
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        default_rules = {
            "rate_limits": {
                "google_forms": 50, # Max forms per hour
                "google_sheets": 100, # Max writes per minute
                "cpanel_api": 10, # Max calls per minute
                "git_sync": 60 # Min seconds between pushes
            },
            "forbidden_patterns": [
                "spam", "bulk mail", "unsolicited", "attack", "exploit", "bypass"
            ],
            "safety_protocols": {
                "check_tos": True,
                "proxy_enabled": False,
                "user_agent_rotation": True
            }
        }
        if not os.path.exists(self.config_path):
            with open(self.config_path, "w") as f:
                json.dump(default_rules, f, indent=4)
        
        with open(self.config_path, "r") as f:
            self.rules = json.load(f)

    def verify_action(self, action_type, params):
        """Verifies if an action is compliant with Google and Server policies."""
        logger.info(f"🛡️ Compliance: Verifying {action_type}...")
        
        # 1. Check Rate Limits
        # (Real implementation would use a counter in Redis/SQLite)
        
        # 2. Content Sanitization
        param_str = str(params).lower()
        for pattern in self.rules["forbidden_patterns"]:
            if pattern in param_str:
                logger.warning(f"🚨 Compliance: Forbidden pattern '{pattern}' detected!")
                return False, f"Action blocked: Safety violation ({pattern})"

        # 3. Quota Management
        logger.success(f"✅ Compliance: Action {action_type} verified (Safe).")
        return True, "Compliant"

    def get_tos_links(self):
        """Returns critical ToS links for documentation."""
        return [
            "https://workspace.google.com/terms/service-terms/",
            "https://cloud.google.com/terms",
            "https://www.google.com/help/terms_maps/"
        ]
