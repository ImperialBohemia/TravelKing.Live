"""
OMEGA Concierge Bot
The main form-processing engine that converts leads into affiliate revenue.

Flow:
1. Read new form submissions from Google Sheets
2. Search Travelpayouts for matching flights/hotels
3. Compose personalized itinerary email
4. Send via Gmail API
5. Update CRM with lead status
"""

import json
import os
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - CONCIERGE - %(message)s')
logger = logging.getLogger(__name__)


class ConciergeBot:
    """Automated lead processing engine."""
    
    def __init__(self, config_path: str = "config/access_vault.json"):
        """
        Initialize bot with credentials from vault.
        
        Args:
            config_path: Path to credentials file
        """
        self.config_path = config_path
        self.vault = self._load_vault()
        
        # Initialize clients lazily
        self._sheets = None
        self._gmail = None
        self._flights = None
        self._hotels = None
        self._crm = None
    
    def _load_vault(self) -> Dict:
        """Load credentials from vault."""
        if os.path.exists(self.config_path):
            with open(self.config_path) as f:
                return json.load(f)
        return {}
    
    @property
    def sheets(self):
        """Lazy-load Sheets client."""
        if not self._sheets:
            from core.google.sheets import SheetsClient
            self._sheets = SheetsClient(self.vault.get('google', {}).get('access_token'))
        return self._sheets
    
    @property
    def gmail(self):
        """Lazy-load Gmail client."""
        if not self._gmail:
            from core.google.gmail import GmailClient
            self._gmail = GmailClient(self.vault.get('google', {}).get('access_token'))
        return self._gmail
    
    @property
    def flights(self):
        """Lazy-load Flights client."""
        if not self._flights:
            from core.travelpayouts.flights import FlightsClient
            tp = self.vault.get('travelpayouts', {})
            self._flights = FlightsClient(tp.get('api_token'), tp.get('marker', 'travelking'))
        return self._flights
    
    @property
    def crm(self):
        """Lazy-load CRM."""
        if not self._crm:
            from core.google.crm import LeadCRM
            crm_sheet_id = self.vault.get('google', {}).get('crm_sheet_id', '')
            self._crm = LeadCRM(self.sheets, crm_sheet_id)
        return self._crm
    
    def process_new_leads(self, form_sheet_id: str) -> Dict:
        """
        Process all new leads from a form responses sheet.
        
        Args:
            form_sheet_id: ID of the Google Sheet linked to Form
            
        Returns:
            dict: Processing summary
        """
        logger.info("🔍 Scanning for new leads...")
        
        # Get unprocessed leads (Phase = NEW)
        new_leads = self.crm.get_leads_by_phase("NEW")
        
        if not new_leads:
            logger.info("No new leads to process")
            return {"processed": 0}
        
        processed = 0
        errors = []
        
        for lead in new_leads:
            try:
                result = self.process_single_lead(lead)
                if result.get("success"):
                    processed += 1
                else:
                    errors.append({"email": lead.get("Email"), "error": result.get("error")})
            except Exception as e:
                errors.append({"email": lead.get("Email"), "error": str(e)})
        
        summary = {
            "processed": processed,
            "errors": len(errors),
            "error_details": errors
        }
        
        logger.info(f"✅ Processed {processed} leads, {len(errors)} errors")
        return summary
    
    def process_single_lead(self, lead: Dict) -> Dict:
        """
        Process a single lead through the full funnel.
        
        Args:
            lead: Lead dict with Email, Name, Destination
            
        Returns:
            dict: Processing result
        """
        email = lead.get("Email")
        name = lead.get("Name", "Traveler")
        destination = lead.get("Destination", "")
        
        logger.info(f"📧 Processing lead: {email} -> {destination}")
        
        # Update phase to PROCESSED
        self.crm.update_phase(email, "PROCESSED")
        
        # Search for flights (assume origin is Prague for now)
        origin = "PRG"  # Could be dynamic based on form
        flights = self.flights.get_deals_with_links(origin, destination[:3].upper(), limit=5)
        
        if not flights:
            return {"success": False, "error": "No flights found"}
        
        # Compose and send email
        send_result = self.gmail.send_itinerary(
            to=email,
            destination=destination,
            flights=self._format_flights(flights)
        )
        
        if send_result.get("success"):
            self.crm.update_phase(email, "SENT")
            logger.info(f"✈️ Sent itinerary to {email}")
            return {"success": True, "message_id": send_result.get("message_id")}
        else:
            return {"success": False, "error": send_result.get("error")}
    
    def _format_flights(self, flights: List[Dict]) -> List[Dict]:
        """Format Travelpayouts data for email template."""
        formatted = []
        for f in flights:
            formatted.append({
                "airline": f.get("airline", "Various"),
                "price": f.get("price", "N/A"),
                "link": f.get("link", "#")
            })
        return formatted
    
    def run_once(self, form_sheet_id: str) -> Dict:
        """Run one processing cycle."""
        return self.process_new_leads(form_sheet_id)


if __name__ == "__main__":
    # Quick test run
    bot = ConciergeBot()
    # bot.run_once("YOUR_FORM_SHEET_ID")
    print("ConciergeBot ready. Set form_sheet_id to start processing.")
