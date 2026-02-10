"""
Travelpayouts API Connector — per official docs.

Docs:
 - Aviasales: https://support.travelpayouts.com/hc/en-us/articles/360057309013
 - Hotellook: https://support.travelpayouts.com/hc/en-us/articles/360021981113
"""
import logging
import requests

from core.settings import load_vault, TRAVELPAYOUTS_BASE_URL

logger = logging.getLogger(__name__)


class TravelpayoutsConnector:
    """Travelpayouts affiliate API bridge."""

    def __init__(self, vault: dict = None):
        self.vault = vault or load_vault()
        tp_cfg = self.vault.get("travelpayouts", {})
        self.token = tp_cfg.get("api_token", "")
        self.marker = tp_cfg.get("marker", "")

    def search_flights(self, origin: str, destination: str,
                       departure_date: str, return_date: str = None,
                       currency: str = "EUR") -> dict:
        """
        Search for cheapest flights.
        Per: Aviasales /v3/prices_for_dates
        """
        url = f"{TRAVELPAYOUTS_BASE_URL}/aviasales/v3/prices_for_dates"
        params = {
            "origin": origin,
            "destination": destination,
            "departure_at": departure_date,
            "currency": currency,
            "sorting": "price",
            "token": self.token,
        }
        if return_date:
            params["return_at"] = return_date

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()

    def get_affiliate_link(self, origin: str, destination: str,
                           departure_date: str) -> str:
        """Build Travelpayouts affiliate link with marker tracking."""
        return (
            f"https://www.aviasales.com/search/"
            f"{origin}{departure_date.replace('-', '')}"
            f"{destination}1?marker={self.marker}"
        )

    def search_hotels(self, location: str, check_in: str,
                      check_out: str, currency: str = "EUR") -> dict:
        """
        Search for hotels.
        Per: Hotellook API
        """
        url = f"{TRAVELPAYOUTS_BASE_URL}/hotellook/v2/cache.json"
        params = {
            "location": location,
            "checkIn": check_in,
            "checkOut": check_out,
            "currency": currency,
            "token": self.token,
        }
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()

    def test_connection(self) -> dict:
        """Test API with a simple flight search."""
        try:
            result = self.search_flights("PRG", "BCN", "2026-06-01")
            if result.get("success"):
                count = len(result.get("data", []))
                return {"status": "OK", "flights_found": count}
            return {"status": "FAIL", "error": "API returned success=false"}
        except Exception as e:
            return {"status": "FAIL", "error": str(e)[:100]}
