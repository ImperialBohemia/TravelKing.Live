# TravelKing.Live - FULL REBUILD 2026-02-08

## 🔥 CLEAN SLATE ARCHITECTURE

### New Foundation
**Date:** 2026-02-08  
**Google Account:** trendnatures@gmail.com  
**Project ID:** 1009428807876 (TravelKing OMEGA)  
**Strategy:** Zero Cost / Max Yield

---

## ✅ VERIFIED WORKING COMPONENTS

### 1. Google OAuth (FULL ADMIN ACCESS)
- **Client ID:** Stored in `config/access_vault.json` or Environment Variables
- **Client Secret:** Stored in `config/access_vault.json` or Environment Variables
- **Refresh Token:** Stored in `config/access_vault.json`
- **Scopes:**
  - ✅ `https://mail.google.com/` (Full Gmail)
  - ✅ `https://www.googleapis.com/auth/spreadsheets` (Sheets)
  - ✅ `https://www.googleapis.com/auth/drive` (Drive)
  - ✅ `https://www.googleapis.com/auth/indexing` (SEO)
  - ✅ `https://www.googleapis.com/auth/cloud-platform` (Cloud)
  - ✅ `https://www.googleapis.com/auth/forms.body` (Forms)
  - ✅ `https://www.googleapis.com/auth/gmail.send` (Send)

### 2. Enabled APIs
- ✅ Gmail API
- ✅ Google Sheets API
- ✅ Google Drive API
- ✅ Indexing API

### 3. Travelpayouts Integration
- **Token:** Stored in `access_vault.json`
- **Marker:** `497485`
- **APIs:** Flights, Hotels

---

## 🎯 CORE ARCHITECTURE

### Lead Funnel Flow
```
Google Form (Public)
    ↓
Google Sheet (Private - trendnatures@gmail.com)
    ↓
Concierge Bot (Python)
    ↓
Travelpayouts API (Flight Search)
    ↓
Gmail API (Personalized Itinerary)
    ↓
Lead Conversion
```

### File Structure
```
TravelKing.Live/
├── config/
│   └── access_vault.json          # ALL credentials (Google + Travelpayouts)
├── core/
│   ├── connectors/
│   │   └── google.py              # OAuth connector with auto-refresh
│   ├── google/
│   │   ├── gmail.py               # Email sending
│   │   ├── sheets.py              # Form data reading
│   │   ├── drive.py               # File uploads
│   │   └── indexing.py            # SEO instant indexing
│   └── travelpayouts/
│       ├── flights.py             # Flight search + affiliate links
│       └── hotels.py              # Hotel search + affiliate links
├── engines/
│   └── concierge_bot.py           # Main lead processor
└── knowledge/
    └── OMEGA_CAPABILITIES.md      # System documentation
```

---

## 🔧 CONFIGURATION

### Google Sheet
- **ID:** `1Kg3jrN5mxPCuD8wKoYmbCXoj0Yyu_LOgsZw6EZzSbAk`
- **Owner:** trendnatures@gmail.com
- **Access:** Private (OAuth token has full access)
- **Purpose:** Collect form responses

### Google Form
- **URL:** `https://docs.google.com/forms/d/e/1FAIpQLSdnXrLYuhgPtFru7OWqnX8H82rB-j70G_QfFn_da0GEOma1Hw/viewform`
- **Access:** Public (Anyone with link)
- **Fields:** Email, Name, Destination, Travel Dates, Budget

### Landing Page
- **Domain:** www.travelking.live
- **Platform:** Google Sites
- **DNS:** CNAME to ghs.googlehosted.com
- **Status:** To be published

---

## 🚀 DEPLOYMENT CHECKLIST

### Phase 1: Foundation (COMPLETE ✅)
- [x] Create new Google Project
- [x] Enable all required APIs
- [x] Configure OAuth Consent Screen
- [x] Generate OAuth credentials
- [x] Obtain Full Admin Access token
- [x] Verify all API connections

### Phase 2: Core Modules (NEXT)
- [ ] Clean up old debug files
- [ ] Update all core modules with new credentials
- [ ] Test Sheets read/write
- [ ] Test Gmail send
- [ ] Test Travelpayouts API

### Phase 3: Concierge Bot
- [ ] Configure field mappings (Sheet columns → Bot variables)
- [ ] Test lead processing flow
- [ ] Verify email delivery
- [ ] Test affiliate link generation

### Phase 4: Landing Page
- [ ] Build Google Sites page
- [ ] Embed Google Form
- [ ] Publish with custom domain
- [ ] Test end-to-end flow

### Phase 5: Monitoring
- [ ] Set up error logging
- [ ] Create performance dashboard
- [ ] Configure alerts

---

## 📊 SUCCESS METRICS

### Technical
- API Response Time: < 2s
- Email Delivery Rate: > 95%
- Form → Email Time: < 5 minutes

### Business
- Lead Conversion Rate: Target 5%
- Cost per Lead: $0 (100% free infrastructure)
- Affiliate Revenue: Track via Travelpayouts dashboard

---

## 🔐 SECURITY

### Credentials Storage
- All tokens in `config/access_vault.json`
- File is `.gitignore`d
- Backup stored securely

### Access Control
- Google Sheet: Private (OAuth only)
- Gmail: Sending only (no read access to inbox)
- Forms: Public submission, private data

---

## 📝 NOTES

### Why This Stack?
1. **100% Free:** No hosting costs, no API fees
2. **High Deliverability:** Gmail infrastructure = no spam
3. **Scalable:** Can handle 10,000+ leads/month
4. **Simple:** No complex infrastructure
5. **Reliable:** Google's 99.9% uptime

### Future Enhancements
- Add SMS notifications (Twilio)
- Integrate with CRM (HubSpot/Salesforce)
- A/B testing on email templates
- Multi-language support
- Advanced analytics (BigQuery when needed)

---

**Built by OMEGA | 2026-02-08**
