import json
import os
import sys

# Ensure root is in path
ROOT_DIR = '/home/q/TravelKing.Live'
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from loguru import logger
from core.enterprise.crm_engine import CRMEngine
from core.google.gmail import GmailClient

class WorkspaceHub:
    """
    Central Nervous System for TravelKing Enterprise.
    Connects: Forms -> Sheets -> CRM -> Sites -> Gmail
    """
    def __init__(self):
        self.crm = CRMEngine()
        # Initialize Gmail Client (assumes secure token exists or will alert)
        try:
             # Load token from vault
             import json
             with open('/home/q/TravelKing.Live/config/access_vault.json', 'r') as f:
                 vault = json.load(f)
             self.gmail = GmailClient(vault['google']['access_token'])
        except Exception as e:
            logger.warning(f"⚠️ Gmail Client not fully active: {e}")
            self.gmail = None
            
        logger.info("🏢 Workspace Hub Initialized.")

    def synchronize_ecology(self):
        """
        Central Pulse: Syncs all Google Services.
        1. Checks CRM for new leads (Forms)
        2. Checks CRM for pending tech tasks
        3. Syncs Site status (if module active)
        """
        logger.info("🔄 Synchronizing Enterprise Ecology...")
        
        # 1. Process New Leads
        new_leads = self.crm.get_new_leads()
        if new_leads:
            logger.info(f"⚡ Found {len(new_leads)} new leads! Processing...")
            for lead in new_leads:
                self.process_lead(lead)
        else:
            logger.info("📭 No new leads to process.")

        # 2. Tech Tasks
        tasks = self.crm.get_pending_tasks()
        if tasks:
            logger.info(f"🛠️  Pending Tasks: {len(tasks)}")
            # Logic to dispatch tasks would go here
        
        logger.success("✅ Ecology synchronization complete.")

    def process_lead(self, lead):
        """
        Orchestrates the response to a new lead.
        1. Log receipt
        2. (Future) Generate AI Itinerary
        3. (Future) Send via Gmail
        4. Update CRM Status
        """
        logger.info(f"🤖 Processing Lead: {lead['name']} ({lead['email']})")
        
        # Simulation of processing
        # In real scenario: Generate PDF, Draft Email, Send.
        
        self.crm.update_lead_status(lead['row_id'], "PROCESSED_PENDING_EMAIL")

    def handle_form_submission(self, name, email, interest):
        """Processes a new lead from Google Forms."""
        logger.info(f"📩 Handling form submission from {email}")
        
        # 1. Log to CRM
        self.crm.log_lead(name, email, interest)
        
        # 2. Trigger Ecology Actions (e.g. Email)
        if self.gmail:
            try:
                # Simple Welcome Email logic
                subject = "Welcome to TravelKing Private Aviation"
                body = f"Dear {name},\n\nThank you for your interest in intentional travel. Our AI Concierge is reviewing your request regarding '{interest}'.\n\nWe will be in touch shortly.\n\nBest regards,\nTravelKing OMEGA"
                self.gmail.send_email(email, subject, body)
                logger.success(f"📧 Welcome email sent to {email}")
                self.crm.update_lead_status(lead.get('row_id'), "EMAIL_SENT")
            except Exception as e:
                logger.error(f"❌ Failed to send email: {e}")
        else:
            logger.warning("⚠️ Gmail not active. Skipping email dispatch.")
        
        logger.success(f"✅ Lead '{name}' processed successfully.")

    def run_forever(self):
        """Main loop for the OMEGA Daemon."""
        import time
        logger.info("♾️  OMEGA Hub Daemon Started. Monitoring Ecology...")
        
        while True:
            try:
                self.synchronize_ecology()
            except Exception as e:
                logger.error(f"⚠️ Ecosystem Hiccup: {e}")
            
            # Pulse every 60 seconds
            time.sleep(60)

if __name__ == "__main__":
    hub = WorkspaceHub()
    if "--daemon" in sys.argv:
        hub.run_forever()
    else:
        hub.synchronize_ecology()
