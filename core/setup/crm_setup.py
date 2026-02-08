
import os
import sys
from googleapiclient.discovery import build
from google.oauth2 import service_account

def setup_free_crm():
    print("💎 OMEGA FREE CRM SETUP: Transforming Sheet into Unlimited CRM...")
    
    try:
        # 1. Auth
        creds = service_account.Credentials.from_service_account_file(
            'config/service_account.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet_id = "1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc" # TravelKing ID from vault

        # 2. Define the CRM Structure
        # We assume the form dumps data into columns A, B, C...
        # We will add CRM columns to the RIGHT of the data.
        
        # Requests to format the sheet
        requests = [
            # Add CRM Header Row if not exists (assuming Row 1 is headers)
            {
                "updateCells": {
                    "range": {
                        "sheetId": 0, # Assuming first sheet
                        "startRowIndex": 0,
                        "endRowIndex": 1,
                        "startColumnIndex": 5, # Start after Form Data (approx col F)
                        "endColumnIndex": 9
                    },
                    "rows": [{
                        "values": [
                            {"userEnteredValue": {"stringValue": "STATUS"}},
                            {"userEnteredValue": {"stringValue": "ASSIGNED TO"}},
                            {"userEnteredValue": {"stringValue": "POTENTIAL VALUE (€)"}},
                            {"userEnteredValue": {"stringValue": "NOTES"}}
                        ]
                    }],
                    "fields": "userEnteredValue"
                }
            },
            # Add Dropdown Validation for STATUS (Unlimited rows)
            {
                "setDataValidation": {
                    "range": {
                        "sheetId": 0,
                        "startRowIndex": 1, # Skip header
                        "startColumnIndex": 5, # Column F (Status)
                        "endColumnIndex": 6
                    },
                    "rule": {
                        "condition": {
                            "type": "ONE_OF_LIST",
                            "values": [
                                {"userEnteredValue": "NEW"},
                                {"userEnteredValue": "CONTACTED"},
                                {"userEnteredValue": "DOCS SENT"},
                                {"userEnteredValue": "WON"},
                                {"userEnteredValue": "LOST"}
                            ]
                        },
                        "showCustomUi": True,
                        "strict": True
                    }
                }
            },
            # Color Coding (Conditional Formatting)
            {
                "addConditionalFormatRule": {
                    "rule": {
                        "ranges": [{"sheetId": 0, "startColumnIndex": 5, "endColumnIndex": 6}],
                        "booleanRule": {
                            "condition": {
                                "type": "TEXT_EQ",
                                "values": [{"userEnteredValue": "NEW"}]
                            },
                            "format": {
                                "backgroundColor": {"red": 0.9, "green": 0.9, "blue": 1.0} # Light Blue
                            }
                        }
                    },
                    "index": 0
                }
            },
             {
                "addConditionalFormatRule": {
                    "rule": {
                        "ranges": [{"sheetId": 0, "startColumnIndex": 5, "endColumnIndex": 6}],
                        "booleanRule": {
                            "condition": {
                                "type": "TEXT_EQ",
                                "values": [{"userEnteredValue": "WON"}]
                            },
                            "format": {
                                "backgroundColor": {"red": 0.8, "green": 1.0, "blue": 0.8} # Light Green
                            }
                        }
                    },
                    "index": 1
                }
            }
        ]

        body = {'requests': requests}
        
        # 3. Execute
        response = service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()
        
        print(f"✅ CRM Columns & Rules Added! ({len(response.get('replies', []))} updates)")
        print("   - Status Dropdown: NEW, CONTACTED, WON...")
        print("   - Auto-Coloring: Active")
        print("   - Cost: €0.00 (Forever)")

    except Exception as e:
        print(f"❌ Error setting up CRM: {e}")
        if "403" in str(e):
            print("   -> Bot lacks 'Editor' permission on the Sheet.")

if __name__ == "__main__":
    setup_free_crm()
