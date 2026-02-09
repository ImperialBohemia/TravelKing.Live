import logging
from core.google.gmail import GmailClient
import json

class Notifier:
    def __init__(self, vault_path='config/access_vault.json'):
        try:
            with open(vault_path) as f:
                self.vault = json.load(f)
            self.email = self.vault['google'].get('account_email')
            self.app_password = self.vault['google'].get('app_password')
            self.client = GmailClient(app_password=self.app_password, email=self.email)
        except Exception as e:
            logging.error(f"Failed to initialize Notifier: {e}")
            self.client = None

    def alert(self, subject, message):
        if not self.client:
            return False

        # Send alert to the admin
        admin_email = self.vault['google'].get('account_email', 'valachman@gmail.com')
        result = self.client.send(
            to=admin_email,
            subject=f"🚨 OMEGA ALERT: {subject}",
            body_html=f"<h3>Critical System Alert</h3><p>{message}</p><hr><p>Sent by OMEGA Autonomous Engine</p>",
            from_name="OMEGA SYSTEM"
        )
        return result.get('success', False)
