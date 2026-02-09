import json
import os
import sys

# Ensure root is in path
ROOT_DIR = '/home/q/TravelKing.Live'
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from loguru import logger
from core.enterprise.crm_engine import CRMEngine

class WorkspaceHub:
    def __init__(self):
        self.crm = CRMEngine()
        logger.info("🏢 Workspace Hub Initialized.")

    def synchronize_ecology(self):
        """Orchestrates logical connections across Workspace tools."""
        logger.info("🔄 Synchronizing Enterprise Ecology...")
        
        # Test synchronization
        tasks = self.crm.get_pending_tasks()
        logger.info(f"📊 Current Tasks fetched from CRM: {len(tasks)}")
        
        logger.success("✅ Ecology synchronization complete.")

    def handle_form_submission(self, name, email, interest):
        """Processes a new lead from Google Forms."""
        logger.info(f"📩 Handling form submission from {email}")
        self.crm.log_lead(name, email, interest, source="Google Forms")
        
if __name__ == "__main__":
    hub = WorkspaceHub()
    hub.synchronize_ecology()
