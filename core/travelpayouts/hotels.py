"""
OMEGA Hotels Client (Travelpayouts/Hotellook)
Official Docs: https://support.travelpayouts.com/hc/en-us/articles/115000343268

Enterprise-grade hotel data API for affiliate deep links.
"""

import requests
from typing import Dict, List, Optional


class HotelsClient:
    """Get hotel prices and generate affiliate links."""

    BASE_URL = "https://engine.hotellook.com/api/v2"

    def __init__(self, api_token: str, marker: str = "travelking"):
        """
        Initialize Hotels client.

        Args:
            api_token: Travelpayouts API token
            marker: Your affiliate marker
        """
        self.token = api_token
        self.marker = marker

    def search_hotels(self, location: str, check_in: str, check_out: str,
                      adults: int = 2, limit: int = 10) -> List[Dict]:
        """
        Search for hotels in a location.

        Args:
            location: City name or IATA code
            check_in: Date 'YYYY-MM-DD'
            check_out: Date 'YYYY-MM-DD'
            adults: Number of guests
            limit: Max results

        Returns:
            List of hotel dicts
        """
        url = f"{self.BASE_URL}/search/start"
        params = {
            "location": location,
            "checkIn": check_in,
            "checkOut": check_out,
            "adults": adults,
            "limit": limit,
            "token": self.token,
            "marker": self.marker
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json().get("hotels", [])
        return []

    def get_hotel_prices(self, hotel_id: int, check_in: str, check_out: str) -> Dict:
        """
        Get prices for a specific hotel.

        Args:
            hotel_id: Hotellook hotel ID
            check_in: Date 'YYYY-MM-DD'
            check_out: Date 'YYYY-MM-DD'

        Returns:
            dict: Hotel with price info
        """
        url = f"{self.BASE_URL}/lookup.json"
        params = {
            "id": hotel_id,
            "checkIn": check_in,
            "checkOut": check_out,
            "token": self.token
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        return {}

    def generate_deep_link(self, hotel_id: int, check_in: str, check_out: str) -> str:
        """
        Generate affiliate link for a hotel.

        Args:
            hotel_id: Hotellook hotel ID
            check_in: Date 'YYYY-MM-DD'
            check_out: Date 'YYYY-MM-DD'

        Returns:
            str: Affiliate deep link
        """
        return (
            f"https://search.hotellook.com/hotels?hotelId={hotel_id}"
            f"&checkIn={check_in}&checkOut={check_out}&marker={self.marker}"
        )
