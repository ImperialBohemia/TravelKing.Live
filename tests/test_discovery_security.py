
import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import sys

# Mocking modules that might be missing
sys.modules['trafilatura'] = MagicMock()
sys.modules['core.security.validator'] = MagicMock()

from services.discovery import DiscoveryService

class TestDiscoverySecurity(unittest.TestCase):
    def setUp(self):
        self.service = DiscoveryService(venv_python="python3")

    @patch('subprocess.check_output')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.makedirs')
    @patch('os.path.exists')
    @patch('os.remove')
    def test_read_url_headless_no_longer_vulnerable(self, mock_remove, mock_exists, mock_makedirs, mock_file, mock_subprocess):
        injection_url = '", wait_until="networkidle")\n        import os\n        os.system("echo hacked")\n        #'
        mock_subprocess.return_value = b"<html></html>"
        mock_exists.return_value = True

        self.service.read_url_headless(injection_url)

        # Check if the injection URL is in the script written to file
        written_script = ""
        for call in mock_file().write.call_args_list:
            written_script += call[0][0]

        # In the FIXED version, the injection_url should NOT be directly in the script
        self.assertNotIn(injection_url, written_script)
        # Instead, it should use sys.argv[1]
        self.assertIn("url = sys.argv[1]", written_script)

        # In the FIXED version, subprocess is called with 3 arguments: [python, script_path, url]
        args, kwargs = mock_subprocess.call_args
        subprocess_cmd = args[0]
        self.assertEqual(len(subprocess_cmd), 3)
        self.assertEqual(subprocess_cmd[2], injection_url)

if __name__ == "__main__":
    unittest.main()
