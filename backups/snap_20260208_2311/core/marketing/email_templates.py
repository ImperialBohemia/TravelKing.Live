
"""
💎 TRAVELKING.LIVE - EMAIL BUILDING ENGINE
Template: The "Global Authority" Welcome Email
Owner: Stanislav Pasztorek
Strategy: High Trust, Low Friction, Direct Conversion
"""

def get_welcome_email(name, magnet_link):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <style>
            body {{ font-family: 'Helvetica', sans-serif; background-color: #f8fafc; color: #1e293b; padding: 40px; }}
            .container {{ max-width: 600px; background: white; border-radius: 24px; padding: 40px; border: 1px solid #e2e8f0; }}
            .header {{ font-weight: 800; font-size: 24px; color: #0f172a; margin-bottom: 20px; }}
            .highlight {{ color: #3b82f6; }}
            .button {{ display: inline-block; background: #3b82f6; color: white !important; padding: 16px 32px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 20px; }}
            .footer {{ margin-top: 40px; font-size: 12px; color: #94a3b8; border-top: 1px solid #f1f5f9; pt: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">TRAVELKING<span class="highlight">.LIVE</span></div>
            <p>Hi {name},</p>
            <p>Welcome to the <b>Elite Circle</b> of smart travelers. You're now protected by the King's Shield.</p>
            <p>As promised, here is your access to the <b>Smart Traveler's Toolkit 2026</b>:</p>
            <a href="{magnet_link}" class="button">Download My Toolkit</a>
            <p style="margin-top:30px;"><b>Quick Tip:</b> Did you know that 85% of passengers never claim the €600 they are owed? We are here to change that.</p>
            <p>Safe travels,</p>
            <p><b>Stanislav Pasztorek</b><br>Independent Passenger Rights Advocate</p>
            <div class="footer">
                © 2026 TravelKing.live | Authorized by Imperial Bohemia<br>
                You received this because you requested the Smart Traveler's Toolkit.
            </div>
        </div>
    </body>
    </html>
    """
