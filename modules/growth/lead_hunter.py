import os
import json
from loguru import logger
from services.discovery import DiscoveryService
from core.security.memory import Memory

class LeadHunter:
    """Enterprise engine to find and analyze high-value business leads."""
    
    def __init__(self):
        self.discovery = DiscoveryService()
        self.memory = Memory()
        self.leads_db = "data/brain/leads.json"
        os.makedirs("data/brain", exist_ok=True)

    def search_niche(self, niche, location):
        """Searches for businesses in a specific niche and location."""
        query = f"{niche} in {location}"
        logger.info(f"🔍 Hunting for leads: {query}")
        
        # In a real scenario, we would use a Search API or Scraper
        # For now, we simulate finding targets that need SEO/Web help
        targets = [
            {"name": "Alpha Plumbing", "url": "http://example-plumbing.cz", "issue": "No SSL, Slow mobile speed"},
            {"name": "Beta Law Firm", "url": "http://beta-law.com", "issue": "Poor SEO, missing meta tags"},
        ]
        
        self.save_leads(targets)
        return targets

    def save_leads(self, new_leads):
        existing = []
        if os.path.exists(self.leads_db):
            with open(self.leads_db, "r") as f:
                existing = json.load(f)
        
        existing.extend(new_leads)
        with open(self.leads_db, "w") as f:
            json.dump(existing, f, indent=4)
        logger.success(f"📈 Saved {len(new_leads)} new leads to {self.leads_db}")

if __name__ == "__main__":
    hunter = LeadHunter()
    hunter.search_niche("Architects", "Prague")
