
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account

def overhaul_crm():
    print("💎 OMEGA ENTERPRISE OVERHAUL: Building Profi CRM...")

    try:
        creds = service_account.Credentials.from_service_account_file(
            'config/service_account.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet_id = "1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc"

        # 1. Create the Structure (Requests)
        requests = [
            # B. Set Professional Headers for LEADS
            {
                "updateCells": {
                    "range": {"sheetId": 0, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 12},
                    "rows": [{
                        "values": [
                            {"userEnteredValue": {"stringValue": "ID"}},
                            {"userEnteredValue": {"stringValue": "TIMESTAMP"}},
                            {"userEnteredValue": {"stringValue": "FULL NAME"}},
                            {"userEnteredValue": {"stringValue": "EMAIL"}},
                            {"userEnteredValue": {"stringValue": "FLIGHT NO."}},
                            {"userEnteredValue": {"stringValue": "STATUS"}},
                            {"userEnteredValue": {"stringValue": "PRIORITY"}},
                            {"userEnteredValue": {"stringValue": "VALUATION (€)"}},
                            {"userEnteredValue": {"stringValue": "NEXT ACTION"}},
                            {"userEnteredValue": {"stringValue": "LAST CONTACT"}},
                            {"userEnteredValue": {"stringValue": "PROCESSED BY"}},
                            {"userEnteredValue": {"stringValue": "INTERNAL NOTES"}}
                        ]
                    }],
                    "fields": "userEnteredValue"
                }
            },
            # C. Professional Formatting: Freeze Top Row
            {
                "updateSheetProperties": {
                    "properties": {
                        "sheetId": 0,
                        "gridProperties": {"frozenRowCount": 1}
                    },
                    "fields": "gridProperties.frozenRowCount"
                }
            },
            # D. Bold Headers & Dark Background
            {
                "repeatCell": {
                    "range": {"sheetId": 0, "startRowIndex": 0, "endRowIndex": 1},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 0.05, "green": 0.1, "blue": 0.2},
                            "textFormat": {"foregroundColor": {"red": 1, "green": 1, "blue": 1}, "bold": True, "fontSize": 10},
                            "horizontalAlignment": "CENTER"
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"
                }
            },
            # E. Dropdowns for STATUS
            {
                "setDataValidation": {
                    "range": {"sheetId": 0, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 5, "endColumnIndex": 6},
                    "rule": {
                        "condition": {"type": "ONE_OF_LIST", "values": [
                            {"userEnteredValue": "0_NEW"},
                            {"userEnteredValue": "1_CONTACTED"},
                            {"userEnteredValue": "2_LEGAL_REVIEW"},
                            {"userEnteredValue": "3_FILED"},
                            {"userEnteredValue": "4_WON_PAID"},
                            {"userEnteredValue": "5_LOST_REJECTED"}
                        ]},
                        "showCustomUi": True
                    }
                }
            },
            # F. Dropdowns for PRIORITY
            {
                "setDataValidation": {
                    "range": {"sheetId": 0, "startRowIndex": 1, "endRowIndex": 1000, "startColumnIndex": 6, "endColumnIndex": 7},
                    "rule": {
                        "condition": {"type": "ONE_OF_LIST", "values": [
                            {"userEnteredValue": "🔥 HIGH"},
                            {"userEnteredValue": "⚡ MEDIUM"},
                            {"userEnteredValue": "❄️ LOW"}
                        ]},
                        "showCustomUi": True
                    }
                }
            }
        ]

        body = {'requests': requests}
        service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

        print("✅ CRM OVERHAUL COMPLETE.")
        print("   - Professional Dark Headers (Frozen)")
        print("   - Sales Pipelines (NEW -> WON)")
        print("   - Priority Scoring (HIGH/MEDIUM/LOW)")

    except Exception as e:
        print(f"❌ Error during overhaul: {e}")

if __name__ == "__main__":
    overhaul_crm()
