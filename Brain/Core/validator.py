
import requests
import logging

class BrainValidator:
    """Quality Control: Ensures nothing 'crap' or 'broken' goes live."""
    
    @staticmethod
    def verify_url(url, expected_text=None):
        try:
            # We use a real browser-like header to avoid being blocked
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) BrainOmega/1.0'}
            response = requests.get(url, headers=headers, timeout=10, verify=False)
            
            if response.status_code != 200:
                return False, f"❌ DEAD LINK: {url} returned {response.status_code}"
            
            if expected_text and expected_text not in response.text:
                return False, f"❌ CONTENT MISMATCH: {url} lives, but expected content is missing."
            
            return True, f"✅ VERIFIED: {url} is live and correct."
        except Exception as e:
            return False, f"❌ CONNECTION ERROR: {str(e)}"

# Global guard
guard = BrainValidator()
