
import os
import logging
import requests
from google import genai
from typing import Optional

class GeminiClient:
    """
    Enterprise Gemini AI Client for TravelKing OMEGA.
    Powering flight analysis, delay prediction, and content generation.
    Uses the latest google-genai SDK.
    """
    def __init__(self, api_key: Optional[str] = None, access_token: Optional[str] = None, project_id: Optional[str] = None):
        self.logger = logging.getLogger("OMEGA.Gemini")
        self.api_key = api_key
        self.access_token = access_token
        self.project_id = project_id

        try:
            if api_key:
                self.client = genai.Client(api_key=api_key)
            elif access_token and project_id:
                # Vertex AI initialization
                self.client = genai.Client(
                    vertexai=True,
                    project=project_id,
                    location="us-central1"
                )
            else:
                self.client = None
        except Exception as e:
            self.logger.warning(f"Gemini Client initialization failed: {e}")
            self.client = None

    def generate_content(self, prompt: str) -> str:
        """Generates content based on a prompt."""
        if not self.client:
            return self._generate_via_rest(prompt)

        try:
            self.logger.info(f"🧠 Gemini: Generating content for prompt: {prompt[:50]}...")
            response = self.client.models.generate_content(
                model='gemini-1.5-pro',
                contents=prompt
            )
            return response.text
        except Exception as e:
            self.logger.error(f"❌ Gemini SDK Error: {e}")
            return self._generate_via_rest(prompt)

    def _generate_via_rest(self, prompt: str) -> str:
        """Fallback to raw REST API for Vertex AI."""
        if not self.access_token or not self.project_id:
            return "Error: No credentials for Gemini (REST fallback failed)."

        url = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{self.project_id}/locations/us-central1/publishers/google/models/gemini-1.5-pro:streamGenerateContent"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "contents": {
                "role": "USER",
                "parts": {"text": prompt}
            }
        }
        try:
            res = requests.post(url, headers=headers, json=data)
            if res.status_code == 200:
                results = res.json()
                text = ""
                # Simple parsing for stream response
                for part in results:
                    candidates = part.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        if parts:
                            text += parts[0].get("text", "")
                return text or "Error: Empty response from Gemini REST."
            else:
                return f"REST Error: {res.status_code} - {res.text}"
        except Exception as e:
            return f"REST Exception: {e}"

    def analyze_flight_delay(self, flight_data: str) -> str:
        """Analyzes flight data for disruption potential."""
        prompt = f"Analyze flight data for delay risk: {flight_data}"
        return self.generate_content(prompt)

    def generate_sniper_copy(self, flight_number: str, destination: str) -> str:
        """Generates high-conversion copy for a sniper page."""
        prompt = f"Generate landing page copy for flight {flight_number} to {destination}."
        return self.generate_content(prompt)
