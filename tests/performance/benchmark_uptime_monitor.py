import sys
import time
import os
from unittest.mock import MagicMock, patch

# --- MOCKING STARTS ---
# We must mock 'google' and its submodules before importing UptimeMonitor
mock_google = MagicMock()
mock_monitoring_v3 = MagicMock()
mock_service_account = MagicMock()

sys.modules['google'] = mock_google
sys.modules['google.cloud'] = MagicMock()
sys.modules['google.cloud.monitoring_v3'] = mock_monitoring_v3
sys.modules['google.oauth2'] = MagicMock()
sys.modules['google.oauth2.service_account'] = mock_service_account

# Mock loguru.logger
mock_loguru = MagicMock()
sys.modules['loguru'] = mock_loguru

# Add project root to sys.path
sys.path.append(os.getcwd())

# Now we can import UptimeMonitor
from core.enterprise.uptime_monitor import UptimeMonitor

def run_benchmark():
    print("🚀 Starting UptimeMonitor Benchmark...")

    # Mocking __init__ to avoid file I/O and credentials validation
    with patch.object(UptimeMonitor, '__init__', return_value=None):
        monitor = UptimeMonitor()
        monitor.root = os.getcwd()
        monitor.project_id = "test-project"
        monitor.project_name = "projects/test-project"
        monitor.vault = {
            "google": {"project_id": "test-project"},
            "cpanel": {"host": "cpanel.test.com"}
        }
        monitor.client = MagicMock()

        # Tracking calls
        list_calls = 0

        def mocked_list_uptime_check_configs(parent):
            nonlocal list_calls
            list_calls += 1
            print(f"  [Mock] list_uptime_check_configs called (Total: {list_calls})")
            time.sleep(0.5) # 500ms latency
            # Return some dummy checks
            mock_check = MagicMock()
            mock_check.display_name = "Some existing check"
            mock_check.name = "projects/test-project/uptimeCheckConfigs/123"
            mock_check.monitored_resource.type = "uptime_url"
            mock_check.period.seconds = 60
            return [mock_check]

        def mocked_create_uptime_check_config(parent, uptime_check_config):
            print(f"  [Mock] create_uptime_check_config called for {uptime_check_config.get('display_name')}")
            time.sleep(0.5) # 500ms latency
            mock_resp = MagicMock()
            mock_resp.name = "newly-created-check"
            return mock_resp

        monitor.client.list_uptime_check_configs = mocked_list_uptime_check_configs
        monitor.client.create_uptime_check_config = mocked_create_uptime_check_config

        # Mock setup_alert_policy to avoid more complexity
        monitor.setup_alert_policy = MagicMock()

        start_time = time.time()
        result = monitor.deploy_enterprise_monitoring()
        end_time = time.time()

        duration = end_time - start_time
        print(f"\n📊 Results:")
        print(f"  Execution Time: {duration:.4f} seconds")
        print(f"  list_all_checks calls: {list_calls}")
        print(f"  Checks active reported: {result['checks_active']}")

        return duration, list_calls

if __name__ == "__main__":
    run_benchmark()
