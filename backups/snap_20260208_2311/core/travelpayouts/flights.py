"""
OMEGA Flights Client (Travelpayouts/Aviasales)
Official Docs: https://support.travelpayouts.com/hc/en-us/categories/200358578

Enterprise-grade flight data API for affiliate deep links.
"""

import requests
from typing import Dict, List, Optional


class FlightsClient:
    """Get flight prices and generate affiliate links."""
    
    BASE_URL = "https://api.travelpayouts.com/v2"
    PRICES_URL = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
    
    def __init__(self, api_token: str, marker: str = "travelking"):
        """
        Initialize Flights client.
        
        Args:
            api_token: Travelpayouts API token
            marker: Your affiliate marker for tracking
        """
        self.token = api_token
        self.marker = marker
    
    def search_prices(self, origin: str, destination: str, 
                      depart_date: Optional[str] = None,
                      return_date: Optional[str] = None,
                      limit: int = 10) -> List[Dict]:
        """
        Search for flight prices.
        
        Args:
            origin: IATA code (e.g., 'PRG')
            destination: IATA code (e.g., 'LON')
            depart_date: Optional date 'YYYY-MM-DD'
            return_date: Optional return date
            limit: Max results
            
        Returns:
            List of flight price dicts
        """
        params = {
            "origin": origin,
            "destination": destination,
            "token": self.token,
            "limit": limit,
            "sorting": "price"
        }
        
        if depart_date:
            params["departure_at"] = depart_date
        if return_date:
            params["return_at"] = return_date
        
        response = requests.get(self.PRICES_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("data", [])
        return []
    
    def get_calendar(self, origin: str, destination: str, month: str) -> List[Dict]:
        """
        Get cheapest prices calendar for a month.
        
        Args:
            origin: IATA code
            destination: IATA code
            month: Format 'YYYY-MM'
            
        Returns:
            List of daily prices
        """
        url = f"{self.BASE_URL}/prices/month-matrix"
        params = {
            "origin": origin,
            "destination": destination,
            "month": month,
            "token": self.token
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            return response.json().get("data", [])
        return []
    
    def generate_deep_link(self, origin: str, destination: str, 
                           depart_date: str, return_date: Optional[str] = None) -> str:
        """
        Generate an affiliate tracking link.
        
        Args:
            origin: IATA code
            destination: IATA code
            depart_date: 'YYYY-MM-DD'
            return_date: Optional return date
            
        Returns:
            str: Affiliate deep link URL
        """
        base = "https://www.aviasales.com/search"
        
        # Format: OriginDDMM[DestinationDDMM]
        dep_parts = depart_date.split("-")
        route = f"{origin}{dep_parts[2]}{dep_parts[1]}{destination}"
        
        if return_date:
            ret_parts = return_date.split("-")
            route += f"{ret_parts[2]}{ret_parts[1]}"
        
        return f"{base}/{route}1?marker={self.marker}"
    
    def get_deals_with_links(self, origin: str, destination: str, limit: int = 5) -> List[Dict]:
        """
        Get flight deals with affiliate links attached.
        
        Args:
            origin: IATA code
            destination: IATA code
            limit: Number of deals
            
        Returns:
            List of deals with 'link' field added
        """
        prices = self.search_prices(origin, destination, limit=limit)
        
        for price in prices:
            price["link"] = self.generate_deep_link(
                origin,
                destination,
                price.get("departure_at", "")[:10],
                price.get("return_at", "")[:10] if price.get("return_at") else None
            )
        
        return prices
