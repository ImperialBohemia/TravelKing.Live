import logging
from google.cloud import secretmanager
from google.api_core import exceptions
import google.auth
from typing import Optional

class SecretManagerClient:
    """
    Enterprise-grade Secret Manager Client.
    Aligned with: https://cloud.google.com/secret-manager/docs/access-secret-version
    Includes fail-safe logic for local development.
    """
    def __init__(self, project_id: str = "1009428807876"):
        self.project_id = project_id
        self.client = None
        self.logger = logging.getLogger("OMEGA.SecretManager")

        try:
            # Check for credentials before initializing
            _, _ = google.auth.default()
            self.client = secretmanager.SecretManagerServiceClient()
            self.logger.info("SecretManager: Official client initialized.")
        except Exception as e:
            self.logger.warning(f"SecretManager: ADC not found, cloud secrets unavailable. ({e})")

    def get_secret(self, secret_id: str, version_id: str = "latest") -> Optional[str]:
        """
        Accesses a secret version. Falls back to None if client not initialized.
        """
        if not self.client:
            return None

        name = f"projects/{self.project_id}/secrets/{secret_id}/versions/{version_id}"

        try:
            response = self.client.access_secret_version(request={"name": name})
            payload = response.payload.data.decode("UTF-8")
            self.logger.info(f"Secret {secret_id} retrieved successfully from cloud.")
            return payload
        except exceptions.PermissionDenied:
            self.logger.error(f"Permission denied for secret {secret_id}. Check IAM roles.")
        except exceptions.NotFound:
            self.logger.warning(f"Secret {secret_id} not found in cloud.")
        except Exception as e:
            self.logger.error(f"Unexpected error retrieving secret {secret_id}: {e}")

        return None
