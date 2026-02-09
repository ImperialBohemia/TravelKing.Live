import base64
import json
import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

class GmailClient:
    """
    Gold Standard Gmail Client.
    Supports official API with OAuth2 and SMTP with App Passwords.
    Aligns with: https://developers.google.com/gmail/api/guides/sending
    """

    SEND_URL = "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"

    def __init__(self, access_token: str = None, app_password: str = None, email: str = "trendnatures@gmail.com"):
        self.token = access_token
        self.app_password = app_password
        self.email = email
        self.logger = logging.getLogger("OMEGA.Gmail")

    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        } if self.token else {}

    def send(self, to: str, subject: str, body_html: str, from_name: str = "TravelKing") -> dict:
        """Sends an email using the best available method (SMTP vs API)."""

        message = MIMEMultipart("alternative")
        message["To"] = to
        message["Subject"] = subject
        message["From"] = f"{from_name} <{self.email}>"
        message.attach(MIMEText(body_html, "html"))

        # Method 1: SMTP (Preferred for long-running bots, bypasses API quotas)
        if self.app_password:
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(self.email, self.app_password)
                    server.send_message(message)
                self.logger.info(f"GmailClient: Email sent to {to} via SMTP.")
                return {"success": True, "method": "smtp"}
            except Exception as e:
                self.logger.error(f"SMTP Send failed: {e}")
                # Fall through to API if token available

        # Method 2: Official API
        if self.token:
            try:
                raw = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")
                res = requests.post(self.SEND_URL, headers=self.headers, json={"raw": raw})
                if res.status_code == 200:
                    self.logger.info(f"GmailClient: Email sent to {to} via API.")
                    return {"success": True, "message_id": res.json().get("id"), "method": "api"}
                else:
                    self.logger.error(f"API Send failed: {res.text}")
            except Exception as e:
                self.logger.error(f"API Send exception: {e}")

        return {"success": False, "error": "No valid authentication method succeeded."}
