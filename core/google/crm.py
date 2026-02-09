"""
OMEGA Lead CRM
Lightweight Sheets-based CRM for tracking lead phases.

Lead Phases:
1. NEW - Just submitted form
2. PROCESSED - Itinerary generated
3. SENT - Email delivered
4. CLICKED - Affiliate link clicked (via tracking)
5. CONVERTED - Booking completed
"""

from typing import Dict, List, Optional
from .sheets import SheetsClient


class LeadCRM:
    """Manage leads using Google Sheets as backend."""

    PHASES = ["NEW", "PROCESSED", "SENT", "CLICKED", "CONVERTED"]

    def __init__(self, sheets_client: SheetsClient, spreadsheet_id: str):
        """
        Initialize CRM with Sheets backend.

        Args:
            sheets_client: Authenticated SheetsClient instance
            spreadsheet_id: The CRM sheet ID
        """
        self.sheets = sheets_client
        self.sheet_id = spreadsheet_id
        self.data_range = "Leads!A:G"  # Email, Name, Destination, Phase, Created, Updated, Notes

    def get_all_leads(self) -> List[Dict]:
        """Get all leads with their current phase."""
        rows = self.sheets.read_range(self.sheet_id, self.data_range)
        if not rows:
            return []

        headers = rows[0] if rows else ["Email", "Name", "Destination", "Phase", "Created", "Updated", "Notes"]
        leads = []

        for row in rows[1:]:
            lead = {}
            for i, header in enumerate(headers):
                lead[header] = row[i] if i < len(row) else ""
            leads.append(lead)

        return leads

    def get_leads_by_phase(self, phase: str) -> List[Dict]:
        """Get all leads in a specific phase."""
        all_leads = self.get_all_leads()
        return [l for l in all_leads if l.get("Phase", "").upper() == phase.upper()]

    def add_lead(self, email: str, name: str, destination: str, notes: str = "") -> bool:
        """
        Add a new lead to the CRM.

        Args:
            email: Lead's email
            name: Lead's name
            destination: Requested destination
            notes: Optional notes

        Returns:
            bool: Success status
        """
        from datetime import datetime
        now = datetime.now().isoformat()

        return self.sheets.append_row(
            self.sheet_id,
            self.data_range,
            [email, name, destination, "NEW", now, now, notes]
        )

    def update_phase(self, email: str, new_phase: str) -> bool:
        """
        Update a lead's phase.

        Args:
            email: Lead's email (unique identifier)
            new_phase: New phase from PHASES list

        Returns:
            bool: Success status
        """
        if new_phase.upper() not in self.PHASES:
            return False

        # Find lead row and update
        rows = self.sheets.read_range(self.sheet_id, self.data_range)
        for i, row in enumerate(rows):
            if row and row[0] == email:
                from datetime import datetime
                row[3] = new_phase.upper()  # Phase column
                row[5] = datetime.now().isoformat()  # Updated column

                # Write back the row
                return self.sheets.write_range(
                    self.sheet_id,
                    f"Leads!A{i+1}:G{i+1}",
                    [row]
                )

        return False

    def get_stats(self) -> Dict[str, int]:
        """Get lead count by phase."""
        leads = self.get_all_leads()
        stats = {phase: 0 for phase in self.PHASES}

        for lead in leads:
            phase = lead.get("Phase", "NEW").upper()
            if phase in stats:
                stats[phase] += 1

        return stats
