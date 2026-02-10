"""
TravelKing Concierge Bot - CLEAN REBUILD
Processes leads from Google Form → Travelpayouts → Gmail

Flow:
1. Read new leads from Google Sheet
2. Search flights via Travelpayouts
3. Generate personalized email with affiliate links
4. Send via Gmail API
5. Mark lead as processed
"""

import json
import logging
import sys
import os
from typing import Dict, List
from datetime import datetime

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.connectors.google import GoogleConnector
from core.google.sheets import SheetsClient
from core.google.gmail import GmailClient
from core.travelpayouts.flights import FlightsClient
from core.utils.notifications import Notifier

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/omega_bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('ConciergeBot')


class ConciergeBot:
    """Main lead processing engine for TravelKing (Enterprise Edition)."""
    
    def __init__(self, vault_path: str = 'config/access_vault.json', sa_path: str = 'config/service_account.json'):
        """Initialize bot with credentials from vault."""
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        
        with open(vault_path) as f:
            self.vault = json.load(f)
        self.sa_path = sa_path
        
        # Lazy-load clients
        self._google_connector = None
        self._sheets = None
        self._gmail = None
        self._flights = None
        self._notifier = None
        
        # Configuration
        self.sheet_id = self.vault['travelking']['sheet_id']
        self.processed_emails = set()
        
        logger.info("🤖 OMEGA Concierge Bot (Enterprise) initialized")

    @property
    def notifier(self):
        """Lazy-load Notifier."""
        if not self._notifier:
            self._notifier = Notifier()
        return self._notifier
    
    @property
    def google_connector(self):
        """Lazy-load Google connector."""
        if not self._google_connector:
            self._google_connector = GoogleConnector(self.vault)
        return self._google_connector
    
    @property
    def sheets(self):
        """Lazy-load Sheets client using Service Account (Permanent)."""
        if not self._sheets:
            # Use Service Account for Sheets if available, fallback to OAuth
            if os.path.exists(self.sa_path):
                from google.oauth2 import service_account
                creds = service_account.Credentials.from_service_account_file(
                    self.sa_path, 
                    scopes=['https://www.googleapis.com/auth/spreadsheets']
                )
                from googleapiclient.discovery import build
                service = build('sheets', 'v4', credentials=creds)
                
                # We wrap the service in a compatible client or update SheetsClient
                # For now, let's keep it simple and update the SheetsClient to handle creds
                self._sheets = SheetsClient(token=None, service_account_path=self.sa_path)
            else:
                token = self.google_connector.token
                self._sheets = SheetsClient(token)
        return self._sheets
    
    @property
    def gmail(self):
        """Lazy-load Gmail client using App Password (Non-expiring)."""
        if not self._gmail:
            app_pw = self.vault['google'].get('app_password')
            email = self.vault['google'].get('account_email', 'trendnatures@gmail.com')
            # Fallback to token if app_pw not found
            token = self.google_connector.token if not app_pw else None
            self._gmail = GmailClient(access_token=token, app_password=app_pw, email=email)
        return self._gmail
    
    @property
    def flights(self):
        """Lazy-load Flights client."""
        if not self._flights:
            self._flights = FlightsClient(
                token=self.vault['travelpayouts']['token'],
                marker=self.vault['travelpayouts']['marker']
            )
        return self._flights
    
    def get_new_leads(self) -> List[Dict]:
        """
        Fetch new leads from Google Sheet.
        Returns list of lead dicts with keys: Email, Name, Destination, etc.
        """
        logger.info(f"📊 Reading leads from Sheet: {self.sheet_id}")
        
        try:
            # Read all form responses
            data = self.sheets.read_range(self.sheet_id, "A:Z")
            
            if not data or len(data) < 2:
                logger.info("No leads found in sheet")
                return []
            
            # Parse headers and rows
            headers = data[0]
            leads = []
            
            for row in data[1:]:
                # Create lead dict
                lead = {}
                for i, header in enumerate(headers):
                    lead[header] = row[i] if i < len(row) else ""
                
                # Skip if already processed
                email = lead.get('Email', '').strip()
                if email and email not in self.processed_emails:
                    leads.append(lead)
                    self.processed_emails.add(email)
            
            logger.info(f"✅ Found {len(leads)} new leads")
            return leads
            
        except Exception as e:
            logger.error(f"❌ Error reading sheet: {e}")
            return []
    
    def search_flights(self, origin: str, destination: str, limit: int = 5) -> List[Dict]:
        """Search for flights and return deals with affiliate links."""
        logger.info(f"✈️ Searching flights: {origin} → {destination}")
        
        try:
            deals = self.flights.get_deals_with_links(origin, destination, limit=limit)
            logger.info(f"✅ Found {len(deals)} flight deals")
            return deals
        except Exception as e:
            logger.error(f"❌ Flight search error: {e}")
            return []
    
    def compose_email(self, lead: Dict, flights: List[Dict]) -> str:
        """
        Compose personalized HTML email with flight deals.
        
        Args:
            lead: Lead dict with Name, Destination, etc.
            flights: List of flight deals with prices and links
            
        Returns:
            HTML email body
        """
        name = lead.get('Name', 'Traveler')
        destination = lead.get('Destination', 'your destination')
        
        # Build flight list HTML
        flight_html = ""
        for i, flight in enumerate(flights[:5], 1):
            price = flight.get('price', 'N/A')
            airline = flight.get('airline', 'Airline')
            link = flight.get('link', '#')
            departure = flight.get('departure_at', '')[:10]
            
            flight_html += f"""
            <div style="border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 8px;">
                <h3 style="margin: 0 0 10px 0; color: #2563eb;">Option {i}: ${price}</h3>
                <p style="margin: 5px 0;"><strong>Airline:</strong> {airline}</p>
                <p style="margin: 5px 0;"><strong>Departure:</strong> {departure}</p>
                <a href="{link}" style="display: inline-block; margin-top: 10px; padding: 10px 20px; background: #2563eb; color: white; text-decoration: none; border-radius: 5px;">View Details →</a>
            </div>
            """
        
        # Full email template
        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
            <h1 style="color: #1e40af;">Hi {name}! ✈️</h1>
            <p style="font-size: 16px; line-height: 1.6;">
                We found some amazing flight deals to <strong>{destination}</strong> just for you!
            </p>
            
            <div style="margin: 30px 0;">
                {flight_html}
            </div>
            
            <p style="font-size: 14px; color: #666; margin-top: 30px;">
                These prices are updated in real-time and may change. Book now to lock in the best deal!
            </p>
            
            <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
            
            <p style="font-size: 12px; color: #999;">
                You're receiving this because you requested travel deals from TravelKing.
                <br>Questions? Reply to this email anytime.
            </p>
        </body>
        </html>
        """
        
        return html
    
    def process_lead(self, lead: Dict) -> bool:
        """
        Process a single lead through the full funnel.
        
        Args:
            lead: Lead dict with Email, Name, Destination
            
        Returns:
            bool: Success status
        """
        email = lead.get('Email', '').strip()
        name = lead.get('Name', 'Traveler')
        destination = lead.get('Destination', '').strip()
        
        if not email or not destination:
            logger.warning(f"⚠️ Skipping incomplete lead: {lead}")
            return False
        
        logger.info(f"📧 Processing lead: {email} → {destination}")
        
        # Search flights (now dynamic from lead form)
        origin = (lead.get('Origin') or lead.get('Origin Port') or "PRG").strip().upper()[:3]
        flights = self.search_flights(origin, destination[:3].upper())
        
        if not flights:
            logger.warning(f"⚠️ No flights found for {destination}")
            return False
        
        # Compose email
        email_body = self.compose_email(lead, flights)
        subject = f"✈️ Your {destination} Flight Deals Are Here!"
        
        # Send email
        try:
            result = self.gmail.send(
                to=email,
                subject=subject,
                body_html=email_body,
                from_name="TravelKing"
            )
            
            if result.get('success'):
                logger.info(f"✅ Email sent to {email}")
                return True
            else:
                logger.error(f"❌ Email failed: {result.get('error')}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Send error: {e}")
            return False
    
    def run(self, max_leads: int = 10):
        """
        Main bot loop: fetch leads and process them.
        
        Args:
            max_leads: Maximum number of leads to process in one run
        """
        logger.info("🚀 Starting Concierge Bot run...")
        
        # Get new leads
        leads = self.get_new_leads()
        
        if not leads:
            logger.info("No new leads to process")
            return
        
        # Process each lead
        processed = 0
        for lead in leads[:max_leads]:
            if self.process_lead(lead):
                processed += 1
        
        logger.info(f"✅ Bot run complete: {processed}/{len(leads)} leads processed")


if __name__ == "__main__":
    # Run bot
    bot = ConciergeBot()
    bot.run()
