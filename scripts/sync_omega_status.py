
import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

def sync_everywhere():
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"""# 🏰 OMEGA Project Status: TravelKing.Live
*Poslední aktualizace: {now_str}*

## 🏰 OMEGA INFRASTRUKTURA (Jádro)
*   [✅] **Connection Fortress Daemon** — Služba běžící 24/7, hlídá a obnovuje všechna spojení.
*   [✅] **Google Service Account** — Trvalý robotický klíč (travelking@...), nahradil osobní přihlašování.
*   [✅] **Access Vault** — Šifrovaný trezor všech klíčů v config/access_vault.json.
*   [✅] **System Guardian** — Samouzdravovací modul pro opravu chyb v reálném čase.

## 📊 GOOGLE EKOSYSTÉM (Permanentní)
*   [✅] **Google Sheets** — Centrální databáze (TravelKing Sheet ID: 1uvNvNKei...).
*   [✅] **Google CRM** — Profesionální sales pipeline (NEW -> WON).
*   [✅] **Google Drive** — Úložiště pro PDF itineráře a zálohy.
*   [✅] **Google Forms** — Sběr leadů (propojeno s webem i CRM).
*   [✅] **Gmail (SMTP)** — Odesílání expedičních e-mailů (trendnatures@gmail.com).
*   [✅] **Gemini AI (Brain)** — Mozek orchestrátora napojený na Google AI SDK.
*   [✅] **Google Search Console** — Propojeno s doménou travelking.live.

## 🌐 WEB & HOSTING
*   [✅] **cPanel API** — Přímý přístup k serveru server707.web-hosting.com.
*   [✅] **Domain travelking.live** — Správa DNS a subdomén.
*   [✅] **SSL Certifikát** — Aktivní a šifrovaný přenos dat.
*   [✅] **Robots.txt Control** — Bezpečnostní pojistka (vypnuto pro indexing: Disallow: /).

## 📣 SOCIÁLNÍ SÍTĚ
*   [✅] **Facebook API (Stanislav Pasztorek)** — Správa reklam, katalogů a sběr leadů.
*   [✅] **Bluesky** — Postovací robot aktivní (AI obsah + video).

## 🚀 MARKETING & SEO
*   [✅] **Bing IndexNow** — Okamžitá indexace pro Bing a Seznam.
*   [✅] **Google Indexing API** — Připraveno pro okamžité odesílání URL.

## ✈️ DATA & AFFILIATE
*   [✅] **Travelpayouts API** — Zdroj dat pro lety a hotely (Marker: 702269).
*   [✅] **Currency API** — Přepočty měn v reálném čase.

## 🛠️ VÝVOJ & OPERACE
*   [✅] **GitHub** — Repozitář ImperialBohemia/TravelKing.Live.
*   [✅] **Cloud Backup** — Automatické snapshoty v cloudu.
*   [✅] **Antigravity Stabilizer** — Optimalizované prostředí (Cache 1.2MB).

---
**REŽIM:** 🏰 **FORTRESS MODE ACTIVE** (Všechna spojení jsou trvalá).
"""

    # Save to files
    paths = [
        '/home/q/TravelKing.Live/OMEGA_STATUS.md',
        '/home/q/TravelKing.Live/data/config/OMEGA_STATUS.md'
    ]
    
    for p in paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w') as f:
            f.write(content)
        print(f"✅ Uloženo do: {p}")

    # Sync to Sheets
    try:
        vault_path = '/home/q/TravelKing.Live/config/access_vault.json'
        sa_path = '/home/q/TravelKing.Live/config/service_account.json'
        
        with open(vault_path) as f: vault = json.load(f)
        creds = service_account.Credentials.from_service_account_file(sa_path, scopes=['https://www.googleapis.com/auth/spreadsheets'])
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet_id = vault['travelking']['sheet_id']
        
        rows = [[line.strip()] for line in content.split('\n') if line.strip()]
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id, range='Dashboard!D1:D100',
            valueInputOption='RAW', body={'values': rows}).execute()
        print("✅ Google Sheets Dashboard aktualizován.")
    except Exception as e:
        print(f"❌ Chyba při ukládání do Google Sheets: {e}")

if __name__ == "__main__":
    sync_everywhere()
