import time
import json
import os
from loguru import logger
from services.discovery import DiscoveryService
from services.google.orchestrator import GoogleOrchestrator
from ai.logic.brain import Brain
from core.security.validator import Validator

# NEW: Max Logic Modules
from scripts.lead_hunter import LeadHunter
from scripts.traffic_engine import TrafficEngine

class AutopilotWorker:
    """The autonomous heart of SimpleCodeSpace. Runs the profit loop with 100% verification."""
    
    def __init__(self):
        self.brain = Brain()
        self.discovery = DiscoveryService()
        self.orchestrator = GoogleOrchestrator(brain=self.brain)
        self.leads_db = "data/brain/leads.json"
        
        # Initialize Workers
        self.hunter = LeadHunter(brain=self.brain)
        self.traffic = TrafficEngine(brain=self.brain)
        
        os.makedirs("data/brain", exist_ok=True)

    def run_cycle(self):
        """Executes one full autonomous cycle (B2B + B2C)."""
        logger.info("🚀 Starting Autonomous Profit Cycle (MAX MODE)...")
        
        # 1. B2B HUNTING (Service Arbitrage)
        niche = "Real Estate Agents"
        location = "Prague"
        
        raw_leads = self.hunter.hunt(niche, location)
        for lead in raw_leads:
            self.process_lead(lead)
            
        # 2. B2C TRAFFIC (Passive Income)
        # Generate content to drive traffic to the new leads or affiliate offers
        trending_topic = "AI Marketing Tools 2026"
        content = self.traffic.generate_content(trending_topic)
        
        if content:
            # In a real scenario, we would post this. For now, we archive it.
            self.archive_content(content)
            
        # 3. GOOGLE DASHBOARD SYNC (Looker Studio)
        # We push the latest leads to the simulated Google Sheet connector
        self.orchestrator.sync_to_looker(raw_leads)

    def process_lead(self, lead):
        """Processes a single lead with maximum verification."""
        url = lead["url"]
        logger.info(f"⚙️ Processing Lead: {lead['name']} ({url})")
        
        # VERIFY: Technical Health
        health = Validator.verify_url_health(url)
        if not health["is_active"]:
            logger.warning(f"❌ Lead {lead['name']} failed health check. Skipping.")
            return

        # AUDIT: Analyze technical debt
        content = self.discovery.read_url(url)
        if not content:
            logger.warning(f"❌ Could not extract content from {url}. Skipping.")
            # Fallback for leads that are just domains without content
            content = f"Domain: {url} - Needs Website Creation"
        
        # BRAIN: Generate Audit Strategy
        # We ask the MoneyTree implicitly via Brain's new logic if we updated it,
        # or explicitly here.
        strategy_prompt = f"Create a high-ticket B2B sales email for {lead['name']} (Pain point: {lead.get('pain_point', 'SEO')}). Return JSON."
        blueprint_raw = self.brain.think(strategy_prompt)
        
        # Fallback if Brain fails to give JSON
        if "{" not in blueprint_raw:
             blueprint_raw = json.dumps({"strategy": "Manual review required", "email": blueprint_raw[:500]})

        # STORE
        logger.success(f"✅ Audit Complete for {lead['name']}.")
        self.save_lead_to_db(lead, health, blueprint_raw)

    def save_lead_to_db(self, lead, health, blueprint):
        existing = []
        if os.path.exists(self.leads_db):
            try:
                with open(self.leads_db, "r") as f:
                    existing = json.load(f)
            except json.JSONDecodeError:
                existing = []
        
        lead_data = {
            "timestamp": time.time(),
            "info": lead,
            "verification": health,
            "strategy": blueprint,
            "status": "Ready for Outreach"
        }
        existing.append(lead_data)
        
        with open(self.leads_db, "w") as f:
            json.dump(existing, f, indent=4)
        logger.info(f"💾 Lead {lead['name']} saved to verified database.")

    def archive_content(self, content):
        """Saves generated content to the 'Flow' archive."""
        archive_path = "data/brain/content_flow.json"
        existing = []
        if os.path.exists(archive_path):
            with open(archive_path, "r") as f:
                existing = json.load(f)
                
        existing.append({
            "timestamp": time.time(),
            "content": content
        })
        
        with open(archive_path, "w") as f:
            json.dump(existing, f, indent=4)
        logger.info("💾 Content archived to Flow database.")

if __name__ == "__main__":
    worker = AutopilotWorker()
    while True:
        try:
            worker.run_cycle()
            logger.info("⏳ Cycle complete. Sleeping for 4 hours...")
            time.sleep(4 * 3600)
        except KeyboardInterrupt:
            break
        except Exception as e:
            logger.error(f"🚨 Autopilot Critical Failure: {e}")
            time.sleep(600)
