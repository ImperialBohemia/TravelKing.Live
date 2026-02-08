
import sys
import os

print("Sys Path:", sys.path)
try:
    import google.oauth2
    print("Import google.oauth2: SUCCESS")
    print("Location:", google.oauth2.__file__)
except ImportError as e:
    print("Import google.oauth2: FAILED", e)

try:
    from google.oauth2 import service_account
    print("Import google.oauth2.service_account: SUCCESS")
except ImportError as e:
    print("Import google.oauth2.service_account: FAILED", e)
