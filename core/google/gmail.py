"""
OMEGA Gmail Client
Official Docs: https://developers.google.com/gmail/api/reference/rest
Scope: https://www.googleapis.com/auth/gmail.send

Enterprise-grade Gmail API wrapper for sending affiliate itineraries.
"""

import base64
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import requests


class GmailClient:
    """Send emails via Gmail API using OAuth2."""
    
    # Official Gmail API endpoints
    SEND_URL = "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"
    
    def __init__(self, access_token: str):
        """
        Initialize with valid OAuth2 access token.
        
        Args:
            access_token: Bearer token from Google OAuth2 flow
        """
        self.token = access_token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def send(self, to: str, subject: str, body_html: str, from_name: str = "TravelKing") -> dict:
        """
        Send an email via Gmail API.
        
        Args:
            to: Recipient email address
            subject: Email subject line
            body_html: HTML content of the email
            from_name: Display name for sender
            
        Returns:
            dict: API response with message ID on success
        """
        message = MIMEMultipart("alternative")
        message["To"] = to
        message["Subject"] = subject
        message["From"] = f"{from_name} <valachman@gmail.com>"
        
        html_part = MIMEText(body_html, "html")
        message.attach(html_part)
        
        # Gmail API requires base64url encoding
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")
        
        response = requests.post(
            self.SEND_URL,
            headers=self.headers,
            json={"raw": raw}
        )
        
        if response.status_code == 200:
            return {"success": True, "message_id": response.json().get("id")}
        else:
            return {"success": False, "error": response.json()}
    
    def send_itinerary(self, to: str, destination: str, flights: list, hotels: list = None) -> dict:
        """
        Send a formatted travel itinerary with affiliate links.
        
        Args:
            to: Recipient email
            destination: Travel destination name
            flights: List of flight dicts with 'price', 'airline', 'link'
            hotels: Optional list of hotel dicts with 'name', 'price', 'link'
        
        Returns:
            dict: Send result
        """
        flight_rows = ""
        for f in flights[:5]:
            flight_rows += f"""
            <tr>
                <td>{f.get('airline', 'N/A')}</td>
                <td><strong>€{f.get('price', 'N/A')}</strong></td>
                <td><a href="{f.get('link', '#')}" style="color:#0066cc;">Book Now →</a></td>
            </tr>
            """
        
        hotel_section = ""
        if hotels:
            hotel_rows = ""
            for h in hotels[:3]:
                hotel_rows += f"""
                <tr>
                    <td>{h.get('name', 'N/A')}</td>
                    <td><strong>€{h.get('price', 'N/A')}/night</strong></td>
                    <td><a href="{h.get('link', '#')}" style="color:#0066cc;">View →</a></td>
                </tr>
                """
            hotel_section = f"""
            <h3>🏨 Recommended Hotels</h3>
            <table>{hotel_rows}</table>
            """
        
        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <h1>✈️ Your {destination} Flight Plan</h1>
            <p>Hi! Here are the best deals we found for you:</p>
            
            <h3>🛫 Top Flights</h3>
            <table style="width:100%; border-collapse: collapse;">
                <tr style="background:#f5f5f5;">
                    <th>Airline</th>
                    <th>Price</th>
                    <th>Action</th>
                </tr>
                {flight_rows}
            </table>
            
            {hotel_section}
            
            <p style="margin-top:20px; color:#666;">
                Powered by <strong>TravelKing</strong> | Your Personal Travel Concierge
            </p>
        </body>
        </html>
        """
        
        return self.send(to, f"Your {destination} Travel Plan ✈️", html)
