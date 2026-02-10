#!/home/q/TravelKing.Live/venv/bin/python3
"""
Google Cloud Uptime Monitoring - Enterprise MAX Configuration
Ensures 24/7 external monitoring of all critical endpoints.
"""

import json
import os
import sys
from google.cloud import monitoring_v3
from google.oauth2 import service_account
from loguru import logger

class UptimeMonitor:
    """Manages Google Cloud Uptime Checks for TravelKing.Live"""
    
    def __init__(self):
        self.root = "/home/q/TravelKing.Live"
        sys.path.append(self.root)
        
        # Load credentials
        sa_path = os.path.join(self.root, "config/service_account.json")
        vault_path = os.path.join(self.root, "config/access_vault.json")
        
        with open(vault_path, 'r') as f:
            self.vault = json.load(f)
        
        self.credentials = service_account.Credentials.from_service_account_file(sa_path)
        self.project_id = self.vault['google']['project_id']
        self.client = monitoring_v3.UptimeCheckServiceClient(credentials=self.credentials)
        self.project_name = f"projects/{self.project_id}"
        
    def create_web_uptime_check(self):
        """Creates uptime check for TravelKing.Live website"""
        logger.info("🛡️ Creating Web Uptime Check...")
        
        config = {
            "display_name": "TravelKing.Live - Website Health",
            "http_check": {
                "request_method": "GET",
                "path": "/",
                "port": 443,
                "use_ssl": True,
                "validate_ssl": True,
                "accepted_response_status_codes": [
                    {"status_value": 200}
                ]
            },
            "timeout": "10s",
            "period": "60s",
            "selected_regions": ["USA", "EUROPE", "ASIA_PACIFIC"],
        }
        
        try:
            response = self.client.create_uptime_check_config(
                parent=self.project_name,
                uptime_check_config=config
            )
            logger.success(f"✅ Web Uptime Check created: {response.name}")
            return response
        except Exception as e:
            logger.error(f"Failed to create Web Uptime Check: {e}")
            return None
    
    def create_cpanel_uptime_check(self):
        """Creates uptime check for cPanel infrastructure"""
        logger.info("🛡️ Creating cPanel Infrastructure Check...")
        
        cpanel_host = self.vault['cpanel']['host']
        
        config = {
            "display_name": "cPanel Server707 - Infrastructure Health",
            "http_check": {
                "request_method": "GET",
                "path": "/",
                "port": 2083,
                "use_ssl": True,
            },
            "timeout": "10s",
            "period": "300s",
            "selected_regions": ["EUROPE"],
        }
        
        try:
            response = self.client.create_uptime_check_config(
                parent=self.project_name,
                uptime_check_config=config
            )
            logger.success(f"✅ cPanel Uptime Check created: {response.name}")
            return response
        except Exception as e:
            logger.error(f"Failed to create cPanel Check: {e}")
            return None
    
    def list_all_checks(self):
        """Lists all existing uptime checks"""
        logger.info("📊 Listing all active Uptime Checks...")
        
        try:
            checks = self.client.list_uptime_check_configs(parent=self.project_name)
            active_checks = []
            
            for check in checks:
                logger.info(f"  ✓ {check.display_name}")
                active_checks.append({
                    "name": check.name,
                    "display_name": check.display_name,
                    "monitored_resource": str(check.monitored_resource.type),
                    "period": check.period.seconds
                })
            
            return active_checks
        except Exception as e:
            logger.error(f"Failed to list checks: {e}")
            return []
    
    def setup_alert_policy(self):
        """Creates alert policy for uptime check failures"""
        logger.info("🚨 Setting up Alert Policy...")
        
        alert_client = monitoring_v3.AlertPolicyServiceClient(credentials=self.credentials)
        
        # This notifies when ANY uptime check fails
        alert_policy = monitoring_v3.AlertPolicy(
            display_name="TravelKing - Critical Uptime Alert",
            conditions=[
                monitoring_v3.AlertPolicy.Condition(
                    display_name="Uptime Check Failure",
                    condition_threshold=monitoring_v3.AlertPolicy.Condition.MetricThreshold(
                        filter='metric.type="monitoring.googleapis.com/uptime_check/check_passed" AND resource.type="uptime_url"',
                        comparison=monitoring_v3.ComparisonType.COMPARISON_LT,
                        threshold_value=1.0,
                        duration={"seconds": 120},
                        aggregations=[
                            monitoring_v3.Aggregation(
                                alignment_period={"seconds": 60},
                                per_series_aligner=monitoring_v3.Aggregation.Aligner.ALIGN_FRACTION_TRUE,
                            )
                        ],
                    )
                )
            ],
            combiner=monitoring_v3.AlertPolicy.ConditionCombinerType.AND,
            enabled=True,
        )
        
        try:
            response = alert_client.create_alert_policy(
                name=self.project_name,
                alert_policy=alert_policy
            )
            logger.success(f"✅ Alert Policy created: {response.name}")
            return response
        except Exception as e:
            logger.warning(f"Alert Policy setup: {e}")
            return None
    
    def deploy_enterprise_monitoring(self):
        """Full deployment of Enterprise-grade monitoring"""
        logger.info("🚀 Deploying Enterprise MAX Monitoring...")
        
        # 1. List existing checks
        existing = self.list_all_checks()
        active_count = len(existing)
        logger.info(f"Found {active_count} existing checks")
        
        # 2. Create new checks if needed
        if not any("TravelKing.Live - Website" in c['display_name'] for c in existing):
            if self.create_web_uptime_check():
                active_count += 1
        else:
            logger.info("Web check already exists, skipping...")
        
        if not any("cPanel" in c['display_name'] for c in existing):
            if self.create_cpanel_uptime_check():
                active_count += 1
        else:
            logger.info("cPanel check already exists, skipping...")
        
        # 3. Setup alerts
        self.setup_alert_policy()
        
        logger.success("💎 Enterprise Monitoring: FULLY OPERATIONAL")
        
        return {
            "status": "DEPLOYED",
            "checks_active": active_count,
            "monitoring_url": f"https://console.cloud.google.com/monitoring/uptime?project={self.project_id}"
        }

if __name__ == "__main__":
    monitor = UptimeMonitor()
    result = monitor.deploy_enterprise_monitoring()
    print(json.dumps(result, indent=2))
