import json
import logging
import sys
import os
import uuid
from typing import Dict, List
from datetime import datetime

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.hub import hub
from core.google.sheets import SheetsClient
from core.google.gmail import GmailClient
from core.google.drive import DriveClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/concierge_bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('ConciergeBot')

class ConciergeBot:
    """
    Enterprise Concierge Bot:
    Delivers the World's Best Lead Magnet (Premium Protection Report).
    Integrated with Google Drive for asset permanence.
    """
    def __init__(self):
        self.hub = hub
        self.sheet_id = self.hub.vault['travelking']['sheet_id']
        self.template_path = 'templates/premium_report.html'
        logger.info("🛡️ OMEGA Concierge Bot (Asset-Integrated) initialized.")

    def run_cycle(self):
        """Processes all leads with status '0_NEW'."""
        logger.info("🔍 Checking for new leads in CRM...")
        sheets = SheetsClient(token=self.hub.google.token)
        leads = sheets.get_form_responses(self.sheet_id)

        for i, lead in enumerate(leads):
            if lead.get('STATUS') == '0_NEW':
                self.process_premium_lead(lead, i + 2)

    def process_premium_lead(self, lead: Dict, row_index: int):
        email = lead.get('EMAIL')
        name = lead.get('FULL NAME', 'Valued Traveler')
        destination = lead.get('DESTINATION', 'your destination')

        logger.info(f"📧 Generating Premium Report for {email}...")

        # 1. Fetch Deals
        deals = self.hub.travelpayouts.get_flight_disruption_data("PRG", destination[:3].upper())
        flight_html = ""
        if isinstance(deals, dict) and "data" in deals:
            for deal in list(deals["data"].values())[:3]:
                flight_html += f"<p>• <strong>{deal.get('destination')}</strong>: €{deal.get('price')} <a href='https://travelking.live'>[View]</a></p>"

        # 2. Load & Inject Template
        with open(self.template_path, 'r') as f:
            template = f.read()

        cert_id = f"TK-{uuid.uuid4().hex[:8].upper()}"
        html = template.replace('{{NAME}}', name)                       .replace('{{DESTINATION}}', destination)                       .replace('{{CERTIFICATE_ID}}', cert_id)                       .replace('{{FLIGHT_LIST}}', flight_html)                       .replace('{{AIRHELP_LINK}}', 'https://www.airhelp.com/en/?aid=11089')

        # 3. Save to Google Drive (Asset Management)
        # Create a local temp file
        temp_file = f"report_{cert_id}.html"
        with open(temp_file, "w") as f:
            f.write(html)

        drive = DriveClient(access_token=self.hub.google.token)
        upload_res = drive.upload_file(temp_file, f"Protection_Report_{cert_id}.html", mime_type="text/html")

        report_url = "N/A"
        if upload_res.get("success"):
            file_id = upload_res.get("id")
            report_url = drive.make_public(file_id)
            logger.info(f"📂 Report stored on Drive: {report_url}")
            os.remove(temp_file) # Cleanup local

        # 4. Send via Gmail
        gmail = GmailClient(access_token=self.hub.google.token, app_password=self.hub.vault['google'].get('app_password'))
        # Include link to the hosted version
        email_body = html + f"<p style='text-align:center;'><a href='{report_url}'>View Web Version of your Report</a></p>"

        gmail.send(
            to=email,
            subject=f"🛡️ Your Premium Protection Report: {destination}",
            body_html=email_body
        )

        # 5. Update Sheet Status
        sheets = SheetsClient(token=self.hub.google.token)
        # Update row with status, link, etc.
        sheets.write_range(self.sheet_id, f"F{row_index}:K{row_index}", [["1_CONTACTED", "⚡ MEDIUM", "0.00", "FOLLOW_UP", datetime.now().strftime("%Y-%m-%d"), "OMEGA_BOT"]])

        logger.info(f"✅ Lead {email} processed successfully with Drive link.")

if __name__ == "__main__":
    bot = ConciergeBot()
    # bot.run_cycle()
    print("ConciergeBot Assets Automated.")
