# TravelKing.Live - Enterprise Knowledge Base

**Last Updated:** 2026-02-08  
**Status:** Production Ready  
**Architecture:** OMEGA Enterprise Autonomous Console

---

## 🎯 PROJECT OVERVIEW

**Mission:** Zero-cost lead generation funnel for travel deals using Google ecosystem + Travelpayouts affiliate network.

**Strategy:** "Zero Cost / Max Yield"
- No hosting fees
- No API costs
- 100% free infrastructure
- Revenue via affiliate commissions

---

## 🏗️ ARCHITECTURE

### Tech Stack
```
Landing Page:    Google Sites (www.travelking.live)
Lead Capture:    Google Forms (public)
Data Storage:    Google Sheets (private)
Processing:      OMEGA Concierge Engine (Enterprise)
Flight Search:   Travelpayouts API
Email Delivery:  Gmail API
Indexing:        Google Indexing API
```

### Data Flow
```
User visits Landing Page
    ↓
Fills Google Form
    ↓
Data saved to Google Sheet
    ↓
Concierge Bot reads Sheet
    ↓
Searches flights on Travelpayouts
    ↓
Sends personalized email via Gmail
    ↓
User clicks affiliate link
    ↓
Commission earned
```

---

## 🔐 CREDENTIALS

### Google Account & Service Account
- **Admin Email:** trendnatures@gmail.com
- **Service Account Email:** travelking@travelking.iam.gserviceaccount.com
- **OAuth Project:** TravelKing OMEGA (ID: 1009428807876)

### Travelpayouts
- **Marker:** 497485
- **Token:** f47a61f5c0d9f0b285fd3551cc66f69d

### Infrastructure Access
- **cPanel/SSH:** imperkhx @ server707.web-hosting.com
- **Gmail SMTP:** via App Password (zzpd unbh srxl omvu)

---

## 📊 ENABLED APIS

- ✅ Gmail API (SMTP Relay)
- ✅ Google Sheets API (v4)
- ✅ Google Drive API
- ✅ Google Indexing API
- ✅ Google Analytics GA4 (G-CENSTCTLCW)

---

## 🤖 CONCIERGE BOT (ENTERPRISE)

**Location:** `/home/q/TravelKing.Live/engines/concierge_bot.py`

**Key Features:**
1. **Permanent Auth:** Uses Service Account for Sheets and App Password for Gmail.
2. **Autonomous Notifier:** Sends alerts on system failures.
3. **Structured Logging:** Full audit trail in `logs/omega_bot.log`.
4. **Link Tracking:** Ready for affiliate redirection.

---

## 💓 SYSTEM HEARTBEAT
Automated monitoring via `core/heartbeat.py`. Verifies all node connections and updates `SYSTEM_STATUS` dashboard in CRM.

---

## 🚀 DEPLOYMENT STATUS

- [x] Phase 1: Foundation (OAuth, Service Account, APIs)
- [x] Phase 2: Core (Engine, Notifications, Heartbeat)
- [/] Phase 3: Landing Page (Google Sites, Forms, GA4)
- [ ] Phase 4: Launch (Test Lead, Scaling)

---

## 📚 REFERENCES

- [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Google Tag Manager API](https://developers.google.com/tag-manager/api/v2)
- [Travelpayouts v3 Docs](https://developers.travelpayouts.com/en/v3)
- [cPanel UAPI Docs](https://api.docs.cpanel.net/uapi/introduction/)

---

**Built by OMEGA | Enterprise Architecture | 2026**
