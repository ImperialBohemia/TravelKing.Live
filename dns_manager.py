
import json
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - DNS - %(message)s')
logger = logging.getLogger(__name__)

class DNSManager:
    def __init__(self):
        with open("config/access_vault.json") as f:
            self.vault = json.load(f)
        
        self.cpanel = self.vault["cpanel"]
        self.base_url = f"https://{self.cpanel['host']}:2083/execute"
        self.headers = {"Authorization": f"cpanel {self.cpanel['user']}:{self.cpanel['api_token']}"}

    def add_zone_record(self, domain, name, type, data):
        """
        Add a DNS record via cPanel UAPI's mass_edit_zone which is often more reliable.
        This function handles adding by 'editing' the zone serial.
        """
        logger.info(f"🚀 Adding DNS Record: {name} ({type}) -> {data}")
        
        # Construct the payload for mass_edit_zone
        # Important: The serial number must usually be incremented or managed by cPanel.
        # But we can try just adding a line.
        
        params = {
            "zone": domain,
            "add": json.dumps([{
                "dname": name,
                "ttl": 14400,
                "record_type": type,
                "data": [data]
            }])
        }

        try:
            res = requests.get(f"{self.base_url}/DNS/mass_edit_zone", headers=self.headers, params=params, verify=False)
            logger.info(f"Result: {res.text}")
            return res.json()
        except Exception as e:
            logger.error(f"Failed to add record: {e}")
            return {"status": 0, "errors": [str(e)]}

    def configure_domains(self):
        """
        Configure:
        1. www.travelking.live -> ghs.googlehosted.com
        2. travelking.live -> ghs.googlehosted.com IPs
        """
        
        # 1. Google Sites CNAME for WWW
        self.add_zone_record("travelking.live", "www.travelking.live.", "CNAME", "ghs.googlehosted.com")
        
        # 2. Point root domain to Google's redirect IP
        self.add_zone_record("travelking.live", "travelking.live.", "A", "216.239.32.21")
        self.add_zone_record("travelking.live", "travelking.live.", "A", "216.239.34.21")

if __name__ == "__main__":
    manager = DNSManager()
    manager.configure_domains()
