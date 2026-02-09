# 📝 GOOGLE FORMS & SHEETS: ENTERPRISE LOGIC

This document defines the backend logic for the TravelKing Lead Magnet.

## 📋 FORM SCHEMA (The "Strategic Capture")
To maximize conversion, the form uses progressive disclosure logic:
1. **Initial Hook:** "Check your flight protection status" (Requires Name & Next Destination).
2. **Commitment:** "Where should we send your report?" (Requires Email).
3. **Upsell:** "Would you like secret deals for this destination?" (Checkbox).

## 🧠 SHEET AUTOMATION (`LeadMagnet.gs`)
The attached Apps Script (`core/google/scripts/LeadMagnet.gs`) performs several critical tasks:
- **Instant Triage:** Assigns a status code (`0_NEW`) that the Concierge Bot looks for.
- **Priority Scoring:** Analyzes the destination and intent to flag high-value leads.
- **Data Hygiene:** Validates email formats before the bot attempts to send.
- **Admin Alerting:** Sends an instant email notification to the owner.

## 📊 CRM WORKFLOW
- **Row Color Coding:** Visual feedback for the owner (Yellow = New, Green = Processed, Red = Error).
- **Frozen Headers:** Essential for usability on mobile.
- **Data Protection:** Sheet is private; access is strictly via Service Account.

---
**ENTERPRISE CRM | OMEGA SUPREME | 2026**
