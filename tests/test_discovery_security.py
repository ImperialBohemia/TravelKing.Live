import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import tempfile

# Mocking modules that might be missing
sys.modules['trafilatura'] = MagicMock()
sys.modules['core.security.validator'] = MagicMock()

from services.discovery import DiscoveryService

class TestDiscoverySecurity(unittest.TestCase):
    def setUp(self):
        self.service = DiscoveryService(venv_python="python3")

    @patch('subprocess.check_output')
    @patch('tempfile.NamedTemporaryFile')
    @patch('os.path.exists')
    @patch('os.remove')
    def test_read_url_headless_no_longer_vulnerable(self, mock_remove, mock_exists, mock_temp, mock_subprocess):
        injection_url = '", wait_until="networkidle")\n        import os\n        os.system("echo hacked")\n        #'
        mock_subprocess.return_value = b"<html></html>"
        mock_exists.return_value = True

        # Mocking tempfile behavior
        mock_temp_instance = MagicMock()
        mock_temp_instance.name = "/tmp/fake_script.py"
        mock_temp.return_value.__enter__.return_value = mock_temp_instance

        self.service.read_url_headless(injection_url)

        # Check if the injection_url is NOT in the script written to file
        written_script = ""
        for call in mock_temp_instance.write.call_args_list:
            written_script += call[0][0]

        self.assertNotIn(injection_url, written_script)
        self.assertIn("url = sys.argv[1]", written_script)

        # In the FIXED version, subprocess is called with 3 arguments: [python, script_path, url]
        args, kwargs = mock_subprocess.call_args
        subprocess_cmd = args[0]
        self.assertEqual(len(subprocess_cmd), 3)
        self.assertEqual(subprocess_cmd[2], injection_url)
        self.assertEqual(subprocess_cmd[1], "/tmp/fake_script.py")

    @patch('subprocess.check_output')
    @patch('tempfile.NamedTemporaryFile')
    @patch('os.path.exists')
    @patch('os.remove')
    def test_concurrent_access_simulation(self, mock_remove, mock_exists, mock_temp, mock_subprocess):
        """Ensures that each call uses a unique temporary file."""
        mock_subprocess.return_value = b"<html></html>"
        mock_exists.return_value = True

        # Mock tempfile to return different names on subsequent calls
        mock_temp_instance1 = MagicMock()
        mock_temp_instance1.name = "/tmp/script1.py"
        mock_temp_instance2 = MagicMock()
        mock_temp_instance2.name = "/tmp/script2.py"

        mock_temp.return_value.__enter__.side_effect = [mock_temp_instance1, mock_temp_instance2]

        self.service.read_url_headless("http://example1.com")
        self.service.read_url_headless("http://example2.com")

        self.assertEqual(mock_subprocess.call_count, 2)
        call1_args = mock_subprocess.call_args_list[0][0][0]
        call2_args = mock_subprocess.call_args_list[1][0][0]

        self.assertNotEqual(call1_args[1], call2_args[1])
        self.assertEqual(call1_args[1], "/tmp/script1.py")
        self.assertEqual(call2_args[1], "/tmp/script2.py")

if __name__ == "__main__":
    unittest.main()
