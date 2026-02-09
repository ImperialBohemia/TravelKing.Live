import re
import requests
from loguru import logger

class Validator:
    """Enterprise-grade input validation and sanitization."""
    
    @staticmethod
    def sanitize_instruction(text):
        """Removes potentially dangerous characters or sequences."""
        if not text:
            return ""
        # Basic sanitization
        clean = re.sub(r'[;&|`$]', '', text)
        return clean.strip()

    @staticmethod
    def validate_config(config_dict, required_keys):
        """Ensures all required keys are present in a configuration."""
        missing = [key for key in required_keys if key not in config_dict]
        if missing:
            logger.error(f"Configuration validation failed: Missing {missing}")
            return False
        return True

    @staticmethod
    def verify_url_health(url):
        """Deep check for URL accessibility and SSL status with realistic headers."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        try:
            response = requests.get(url, timeout=15, allow_redirects=True, headers=headers)
            has_ssl = url.startswith("https")
            is_active = response.status_code == 200
            
            logger.info(f"🔍 URL Health: {url} | Status: {response.status_code} | SSL: {has_ssl}")
            return {
                "is_active": is_active,
                "has_ssl": has_ssl,
                "status_code": response.status_code
            }
        except Exception as e:
            logger.warning(f"⚠️ URL Health Check Failed for {url}: {e}")
            return {"is_active": False, "has_ssl": False, "error": str(e)}

    @staticmethod
    def validate_json_output(raw_text):
        """Ensures the AI output is a valid, parseable JSON."""
        try:
            import json
            # Extract JSON if wrapped in markdown
            json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
            if json_match:
                data = json.loads(json_match.group())
                return True, data
            return False, "No JSON object found in text."
        except Exception as e:
            return False, f"JSON Parsing Error: {str(e)}"
