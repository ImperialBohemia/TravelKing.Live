import base64
import json
import logging
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import requests

logger = logging.getLogger(__name__)

class GmailClient:
    """Send emails via Gmail API or SMTP."""
    
    # Official Gmail API endpoints
    SEND_URL = "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"
    
    def __init__(self, access_token: str = None, app_password: str = None, email: str = "trendnatures@gmail.com"):
        """
        Initialize with OAuth2 token or App Password.
        """
        self.token = access_token
        self.app_password = app_password
        self.email = email
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        } if self.token else {}
    
    def send(self, to: str, subject: str, body_html: str, from_name: str = "TravelKing") -> dict:
        """
        Send an email via SMTP (preferred) or Gmail API.
        """
        message = MIMEMultipart("alternative")
        message["To"] = to
        message["Subject"] = subject
        message["From"] = f"{from_name} <{self.email}>"
        
        html_part = MIMEText(body_html, "html")
        message.attach(html_part)
        
        # Method 1: SMTP (Bypasses API restrictions, more reliable)
        if self.app_password:
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(self.email, self.app_password)
                    server.send_message(message)
                return {"success": True, "method": "smtp"}
            except Exception as e:
                logger.warning(f"SMTP sending failed: {e}")
                if not self.token:
                    return {"success": False, "error": str(e), "method": "smtp"}
                logger.info("Falling back to Gmail API...")

        # Method 2: API Fallback
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")
        response = requests.post(
            self.SEND_URL,
            headers=self.headers,
            json={"raw": raw}
        )
        
        if response.status_code == 200:
            return {"success": True, "message_id": response.json().get("id"), "method": "api"}
        else:
            return {"success": False, "error": response.json(), "method": "api"}
    
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
