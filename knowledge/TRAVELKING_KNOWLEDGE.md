# TravelKing.Live - Enterprise Knowledge Base

**Last Updated:** 2026-02-08  
**Status:** Production Ready  
**Architecture:** Clean Rebuild with Google OAuth

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
Processing:      Python Bot (local server)
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

### Google OAuth
- **Account:** trendnatures@gmail.com
- **Project:** TravelKing OMEGA (ID: 1009428807876)
- **Client ID:** `1009428807876-seopbefn13ev9fnot0sdsh1018fp00iu.apps.googleusercontent.com`
- **Scopes:** Gmail (send), Sheets, Drive, Indexing, Cloud Platform

### Travelpayouts
- **Marker:** 497485
- **APIs:** Flights, Hotels

### Domain
- **Primary:** www.travelking.live
- **DNS:** CNAME → ghs.googlehosted.com
- **Hosting:** Google Sites (zero cost)

---

## 📊 ENABLED APIS

- ✅ Gmail API
- ✅ Google Sheets API
- ✅ Google Drive API
- ✅ Google Indexing API

---

## 🤖 CONCIERGE BOT

**Location:** `/home/q/TravelKing.Live/engines/concierge_bot.py`

**Function:**
1. Reads new leads from Google Sheet
2. Searches flights via Travelpayouts
3. Composes personalized HTML email
4. Sends via Gmail API
5. Tracks processed leads in memory

**Run:**
```bash
cd /home/q/TravelKing.Live
~/SimpleCodeSpace/venv/bin/python3 engines/concierge_bot.py
```

---

## 📝 GOOGLE FORM

**URL:** https://docs.google.com/forms/d/e/1FAIpQLSdnXrLYuhgPtFru7OWqnX8H82rB-j70G_QfFn_da0GEOma1Hw/viewform

**Fields:**
- Email (required)
- Name
- Destination
- Travel Dates
- Budget

**Access:** Public (anyone with link)

---

## 📊 GOOGLE SHEET

**ID:** `1Kg3jrN5mxPCuD8wKoYmbCXoj0Yyu_LOgsZw6EZzSbAk`

**Owner:** trendnatures@gmail.com

**Access:** Private (OAuth token only)

**Purpose:** Collect form responses, serve as CRM

---

## 🌐 LANDING PAGE

**Platform:** Google Sites

**Domain:** www.travelking.live

**Status:** To be published

**Content:**
- Hero section with value proposition
- Embedded Google Form
- Trust signals
- Clear CTA

---

## 🔧 DEVELOPMENT

### File Structure
```
TravelKing.Live/
├── config/
│   └── access_vault.json       # All credentials
├── core/
│   ├── connectors/
│   │   └── google.py           # OAuth with auto-refresh
│   ├── google/
│   │   ├── gmail.py            # Email sending
│   │   ├── sheets.py           # Data reading
│   │   ├── drive.py            # File uploads
│   │   └── indexing.py         # SEO
│   └── travelpayouts/
│       ├── flights.py          # Flight search
│       └── hotels.py           # Hotel search
├── engines/
│   └── concierge_bot.py        # Main processor
└── knowledge/
    └── TRAVELKING_KNOWLEDGE.md # This file
```

### Git Repository
**URL:** https://github.com/ImperialBohemia/TravelKing.Live

**Branch:** clean-rebuild-2026

**Status:** Clean, production-ready

---

## 🚀 DEPLOYMENT CHECKLIST

### Phase 1: Foundation ✅
- [x] Google Project created
- [x] OAuth configured
- [x] All APIs enabled
- [x] Full admin access verified

### Phase 2: Core ✅
- [x] Concierge Bot built
- [x] All modules tested
- [x] Git repository clean

### Phase 3: Landing Page (IN PROGRESS)
- [ ] Build Google Sites page
- [ ] Embed form
- [ ] Publish with custom domain
- [ ] Test end-to-end

### Phase 4: Launch
- [ ] Submit test lead
- [ ] Verify email delivery
- [ ] Monitor performance
- [ ] Scale

---

## 📈 SUCCESS METRICS

### Technical
- API response time: < 2s
- Email delivery rate: > 95%
- Form → Email time: < 5 min

### Business
- Lead conversion: Target 5%
- Cost per lead: $0
- Revenue: Track via Travelpayouts

---

## 🔄 MAINTENANCE

### Daily
- Check bot logs
- Monitor email delivery

### Weekly
- Review lead quality
- Optimize email templates
- A/B test landing page

### Monthly
- Analyze conversion rates
- Update flight search logic
- Expand destination coverage

---

## 🆘 TROUBLESHOOTING

### Bot not processing leads
1. Check Google Sheet has data
2. Verify OAuth token is valid
3. Check API quotas

### Emails not sending
1. Verify Gmail API enabled
2. Check token scopes
3. Review email content for spam triggers

### Form not submitting
1. Check form is public
2. Verify Sheet is linked
3. Test form manually

---

## 📚 REFERENCES

- [Google Sheets API](https://developers.google.com/sheets/api)
- [Gmail API](https://developers.google.com/gmail/api)
- [Travelpayouts API](https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-API)
- [Google Sites](https://sites.google.com)

---

**Built by OMEGA | Enterprise Architecture | 2026**
