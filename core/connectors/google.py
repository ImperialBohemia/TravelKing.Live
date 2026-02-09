import sys
import json
import requests
import os
import logging
import subprocess

from core.base.connector import BaseConnector

class GoogleConnector(BaseConnector):
    """Independent Admin Bridge for all Google Services."""
    def __init__(self, vault):
        super().__init__("Google", vault.get("google", {}))
        self.vault_full = vault
        # Dynamic project root
        self.root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.vault_full_path = os.path.join(self.root, 'config', 'access_vault.json')

        self.token = self.config.get('access_token')
        self.refresh_token = self.config.get('refresh_token')

        # Official Project OAuth Client ID (TravelKing OMEGA)
        self.client_id = self.config.get("client_id", "1009428807876-seopbefn13ev9fnot0sdsh1018fp00iu.apps.googleusercontent.com")
        self.client_secret = self.config.get("client_secret", "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")

        # Permanent Brain Link (ADC)
        self.use_adc = False
        try:
            import google.auth
            creds, project = google.auth.default()
            if creds:
                self.logger.info(f"🧠 Permanent Brain Access detected (Project: {project})")
                self.use_adc = True
                self.adc_creds = creds
        except:
            pass

    def test_connection(self) -> bool:
        """Verifies Google connection by calling tokeninfo or using ADC."""
        if self.use_adc:
            return True # Assume ADC is handled by SDK transitively

        url = "https://www.googleapis.com/oauth2/v3/tokeninfo"
        try:
            res = self.session.get(url, params={"access_token": self.token})
            if res.status_code == 200:
                return True
            if self.refresh():
                res = self.session.get(url, params={"access_token": self.token})
                return res.status_code == 200
        except Exception as e:
            self.logger.error(f"Connection test failed: {e}")
        return False

    def refresh(self) -> bool:
        """Refreshes the Google access token using SDK, Environment Sync, or ADC."""
        # 1. Environment Sync (Agent Supremacy)
        try:
            home = os.path.expanduser("~")
            env_creds_path = os.path.join(home, ".gemini/oauth_creds.json")
            if os.path.exists(env_creds_path):
                with open(env_creds_path, 'r') as f:
                    env_data = json.load(f)
                    if env_data.get("access_token") and env_data.get("access_token") != self.token:
                        self.logger.info("⚡ Environment Sync: Regenerating Google link from Brain...")
                        self.token = env_data["access_token"]
                        self.vault_full['google']['access_token'] = self.token
                        self._save_vault()
                        return True
        except Exception as e:
            self.logger.debug(f"Environment Sync failed: {e}")

        # 2. ADC Fallback
        if self.use_adc:
            try:
                from google.auth.transport.requests import Request
                self.adc_creds.refresh(Request())
                self.token = self.adc_creds.token
                return True
            except:
                pass

        # 3. Direct GCloud CLI Fallback (The "Hammer" Method)
        if self._refresh_via_gcloud_cli():
            return True

        # 4. Standard SDK Refresh
        return self._refresh_via_sdk()

    def _refresh_via_sdk(self) -> bool:
        """Standard OAuth2 Refresh using SDK or requests."""
        try:
            from google.oauth2.credentials import Credentials
            from google.auth.transport.requests import Request

            creds = Credentials(
                token=self.token,
                refresh_token=self.refresh_token,
                client_id=self.client_id,
                client_secret=self.client_secret,
                token_uri="https://oauth2.googleapis.com/token"
            )

            creds.refresh(Request())

            if creds.token:
                self.token = creds.token
                self.vault_full['google']['access_token'] = self.token
                self._save_vault()
                return True
        except Exception as e:
            self.logger.error(f"Google SDK Refresh failed: {e}")
            # Fallback to manual requests if SDK fails
            url = "https://oauth2.googleapis.com/token"
            data = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "refresh_token": self.refresh_token,
                "grant_type": "refresh_token"
            }
            res = requests.post(url, data=data).json()
            if "access_token" in res:
                self.token = res["access_token"]
                self.vault_full['google']['access_token'] = self.token
                self._save_vault()
                return True
        return False

    def _refresh_via_gcloud_cli(self) -> bool:
        """Attempts to get a fresh token directly from gcloud CLI."""
        try:
            home = os.path.expanduser("~")
            gcloud_cmds = ["gcloud", os.path.join(home, "SimpleCodeSpace/0/google-cloud-sdk/bin/gcloud")]

            for cmd in gcloud_cmds:
                try:
                    token = subprocess.check_output(
                        [cmd, "auth", "print-access-token"],
                        stderr=subprocess.DEVNULL,
                        timeout=5
                    ).decode('utf-8').strip()

                    if token and " " not in token:
                        self.logger.info(f"⚡ GCloud CLI: Extracted fresh token using {cmd}")
                        self.token = token
                        self.vault_full['google']['access_token'] = self.token
                        self._save_vault()
                        return True
                except:
                    continue
        except Exception as e:
            self.logger.debug(f"GCloud CLI refresh failed: {e}")

        return False

    def _save_vault(self):
        """Internal helper to persist vault changes."""
        with open(self.vault_full_path, 'w') as f:
            json.dump(self.vault_full, f, indent=4)

    def api_call(self, url, method="GET", **kwargs):
        """Authenticated API call to Google Services."""
        if not self.token:
            self.refresh()

        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.token}"
        kwargs["headers"] = headers

        if "googleads" in url:
            headers["developer-token"] = self.config.get("developer_token", "")
            headers["login-customer-id"] = self.config.get("customer_id", "")

        res = self.call(method, url, **kwargs)

        if isinstance(res, dict) and "error" in res:
            error_str = str(res.get("error")).lower()
            if "unauthorized" in error_str or "401" in error_str:
                if self.refresh():
                    return self.api_call(url, method, **kwargs)

        return res
