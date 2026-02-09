import json
import requests
import os

with open("config/access_vault.json", "r") as f:
    vault = json.load(f)

# Try different client IDs
client_ids = [
    "681255809395-oo8ft2oprdrnp9e3aqf6av3hmduib135j.apps.googleusercontent.com",
    "1009428807876-seopbefn13ev9fnot0sdsh1018fp00iu.apps.googleusercontent.com"
]

refresh_token = vault['google']['refresh_token']
client_secret = vault['google']['client_secret']

for cid in client_ids:
    print(f"Testing client_id: {cid}")
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": cid,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    res = requests.post(url, data=data).json()
    print(f"Result: {res}")
    if "access_token" in res:
        print("✅ SUCCESS!")
        vault['google']['access_token'] = res['access_token']
        vault['google']['client_id'] = cid
        with open("config/access_vault.json", "w") as f:
            json.dump(vault, f, indent=4)
        break
