import base64
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from typing import Optional
from core.google.factory import GoogleServiceFactory
from core.utils.backoff import google_api_backoff

class GmailClient:
    """
    Gold Standard Gmail Client with official API support and retries.
    """
    def __init__(self, factory: Optional[GoogleServiceFactory] = None,
                 app_password: Optional[str] = None,
                 email: str = "trendnatures@gmail.com"):
        self.factory = factory or GoogleServiceFactory()
        self.service = self.factory.get_gmail()
        self.app_password = app_password
        self.email = email
        self.logger = logging.getLogger("OMEGA.Gmail")

    @google_api_backoff()
    def send(self, to: str, subject: str, body_html: str, from_name: str = "TravelKing") -> dict:
        """Sends email via official API with automatic retries."""
        message = MIMEMultipart("alternative")
        message["To"] = to
        message["Subject"] = subject
        message["From"] = f"{from_name} <{self.email}>"
        message.attach(MIMEText(body_html, "html"))

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")
        res = self.service.users().messages().send(userId='me', body={'raw': raw}).execute()

        self.logger.info(f"GmailClient: Message sent. ID: {res.get('id')}")
        return {"success": True, "message_id": res.get("id"), "method": "api"}
