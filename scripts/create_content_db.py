import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
SERVICE_ACCOUNT_FILE = '/home/q/TravelKing.Live/config/service_account.json'
USER_EMAIL = 'valachman@gmail.com'

def create_db():
    print("🔌 Connecting to Google Sheets...")
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    
    # EXISTING CRM SHEET ID (Fallback due to Quota Error)
    EXISTING_SHEET_ID = '1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc'
    
    print(f"📄 Opening Existing Sheet: {EXISTING_SHEET_ID}...")
    sh = client.open_by_key(EXISTING_SHEET_ID)
    
    print(f"✅ Sheet Access Confirmed: {sh.title}")
    
    print("🛠 Setting up 'Content' tab...")
    try:
        ws = sh.worksheet('Content')
    except:
        ws = sh.add_worksheet(title='Content', rows=100, cols=10)
        
    # Set Headers
    ws.update('A1', [['PageID', 'HTML_Content', 'CSS_Custom', 'Last_Updated']])
    
    # Format Headers
    ws.format('A1:D1', {'textFormat': {'bold': True}, 'backgroundColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}})
    
    # Add Initial "Home" Content (from current live site html)
    # We will just put a placeholder for now
    ws.append_row(['home', '<h1>Welcome to TravelKing</h1><p>Dynamic Content Loaded!</p>', 'body { background-color: #f0f0f0; }', 'Initial Setup'])
    
    print("🎉 DB Setup Complete.")
    return sh.id

if __name__ == "__main__":
    create_db()
