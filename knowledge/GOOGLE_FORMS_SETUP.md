# Google Forms -> CRM Integration Guide

To enable the "Total Sync" where a form submission instantly appears in our CRM and triggers an email:

## 1. Create the Form
1. Go to [Google Forms](https://forms.google.com)
2. Create a new form "TravelKing Inquiry"
3. Add these EXACT questions (case sensitive for auto-mapping logic):
   - **Timestamp** (Auto-created)
   - **Full Name** (Short answer)
   - **Email** (Short answer)
   - **Interest** (Dropdown: Private Jet, Empty Leg, Yacht, Other)
   - **Source** (Short answer - hidden/pre-filled or Question "How did you find us?")

## 2. Connect to Spreadsheet
1. In the Form, go to **Responses** tab.
2. Click the green **Sheets icon** ("Link to Sheets").
3. Select **"Select existing spreadsheet"**.
4. Choose the `TravelKing CRM` sheet (ID: `1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc`).

## 3. Rename the Tab
1. Open the Spreadsheet.
2. You will see a new tab named "Form Responses 1".
3. **RENAME** this tab to `Leads`.
4. Ensure the columns match what `CRMEngine` expects:
   - A: Timestamp
   - B: Full Name
   - C: Email
   - D: Interest
   - E: Source 
   - F: Status (Add this header manually if needed, leave rows empty)

## 4. Automation Logic
The `WorkspaceHub` daemon checks this `Leads` sheet every 60 seconds.
- It looks for rows where **Column F (Status)** is EMPTY or "NEW".
- If found -> Processes lead -> Updates Status to "PROCESSED".

## ✅ Done!
Once this is set up, any form submission will:
1. Land in `Leads` sheet.
2. Be detected by `WorkspaceHub`.
3. Trigger a welcome email via Gmail.
4. Be marked as processed.
