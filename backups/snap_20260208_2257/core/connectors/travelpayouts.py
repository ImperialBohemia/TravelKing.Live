
import requests
import logging
from core.base.connector import BaseConnector

class TravelpayoutsConnector(BaseConnector):
    """
    Enterprise Travelpayouts Connector (OMEGA Architecture).
    Permanent link for flights, hotels, and partner statistics.
    """
    def __init__(self, vault):
        super().__init__("Travelpayouts", vault.get("travelpayouts", {}))
        self.api_token = self.config.get("api_token")
        self.marker = self.config.get("marker")
        self.base_url = "https://api.travelpayouts.com"

    def test_connection(self) -> bool:
        """Verifies API Token by fetching partner information."""
        # Current statistics API endpoint
        url = f"{self.base_url}/statistics/v1/get_fields_list"
        res = self.api_call(url)
        return isinstance(res, dict) and "error" not in res

    def api_call(self, url, method="GET", data=None, params=None):
        """Standardized Travelpayouts API caller with permanent token handling."""
        headers = {
            "X-Access-Token": self.api_token,
            "Content-Type": "application/json"
        }
        
        # Ensure marker is included in params if not present
        p = params or {}
        if "marker" not in p:
            p["marker"] = self.marker
            
        return self.call(method, url, headers=headers, json=data, params=p)

    def get_flight_disruption_data(self, origin, destination):
        """Specific helper for finding high-value disruption targets."""
        # This is a placeholder for actual flight search/stats integration
        endpoint = f"{self.base_url}/aviasales/v3/prices_for_dates"
        params = {
            "origin": origin,
            "destination": destination,
            "unique": "false",
            "sorting": "price",
            "direct": "false",
            "currency": "eur",
            "limit": 10
        }
        return self.api_call(endpoint, params=params)
