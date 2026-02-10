"""
CRM Engine — Lead pipeline backed by Google Sheets.

Flow: Lead In → Qualify (AI) → Offer (Travelpayouts) → Track
"""
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class CRMEngine:
    """Manages customer leads through a Google Sheets-backed pipeline."""

    PHASES = ["NEW", "CONTACTED", "QUALIFIED", "OFFER_SENT", "WON", "LOST"]

    def __init__(self, google_connector):
        self.google = google_connector
        self.tab = "Leads"
        self._ensure_tab()

    def _ensure_tab(self):
        """Create Leads tab if it doesn't exist."""
        try:
            self.google.sheets_ensure_tab(self.tab)
        except Exception as e:
            logger.warning(f"Could not ensure CRM tab: {e}")

    def add_lead(self, name: str, email: str, source: str = "web",
                 notes: str = "") -> dict:
        """Add a new lead to the pipeline."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [timestamp, name, email, source, "NEW", notes, ""]
        self.google.sheets_append(f"{self.tab}!A:G", [row])
        logger.info(f"Lead added: {name} ({email}) from {source}")
        return {"name": name, "email": email, "phase": "NEW", "timestamp": timestamp}

    def get_leads(self, phase: str = None) -> list:
        """Get all leads, optionally filtered by phase."""
        rows = self.google.sheets_read(f"{self.tab}!A:G")
        if not rows:
            return []
        # Skip header if present
        data = rows[1:] if rows[0][0].lower() in ("timestamp", "date") else rows
        if phase:
            data = [r for r in data if len(r) > 4 and r[4] == phase]
        return data

    def update_phase(self, email: str, new_phase: str) -> bool:
        """Update a lead's phase by email."""
        if new_phase not in self.PHASES:
            logger.error(f"Invalid phase: {new_phase}")
            return False
        rows = self.google.sheets_read(f"{self.tab}!A:G")
        for i, row in enumerate(rows):
            if len(row) > 2 and row[2] == email:
                # Sheets rows are 1-indexed, +1 for header
                cell = f"{self.tab}!E{i + 1}"
                self.google.sheets_write(cell, [[new_phase]])
                logger.info(f"Lead {email} → {new_phase}")
                return True
        logger.warning(f"Lead not found: {email}")
        return False

    def get_stats(self) -> dict:
        """Get lead pipeline statistics."""
        rows = self.google.sheets_read(f"{self.tab}!A:G")
        stats = {phase: 0 for phase in self.PHASES}
        for row in rows:
            if len(row) > 4 and row[4] in self.PHASES:
                stats[row[4]] += 1
        stats["total"] = sum(stats.values())
        return stats
