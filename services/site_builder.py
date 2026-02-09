import os
import json
from loguru import logger

class SiteBuilder:
    """Builds a Google-compliant, high-authority luxury aviation portal."""
    def __init__(self, target_url="https://villiers.ai/?id=11089"):
        self.target_url = target_url
        self.output_dir = "dashboard/site_build"
        os.makedirs(self.output_dir, exist_ok=True)
        logger.info("Site Builder: Initialized for E-E-A-T compliance.")

    def generate_privacy_policy(self):
        """Generates a mandatory Privacy Policy for Google Trust."""
        content = "<h1>Privacy Policy</h1><p>Your privacy is paramount at Elite Aviation Insider...</p>"
        self._save_page("privacy", content)

    def generate_contact_page(self):
        """Generates a Contact page (Crucial for Google Trust)."""
        content = "<h1>Contact Our Aviation Experts</h1><p>Inquiries regarding private jet charters...</p>"
        self._save_page("contact", content)

    def generate_about_page(self):
        """Generates an Authority/About page (Expertise signal)."""
        content = "<h1>About Elite Aviation Insider</h1><p>We are a specialized portal providing market intelligence for the private aviation sector...</p>"
        self._save_page("about", content)

    def generate_index(self, live_deals):
        """Builds the high-value Homepage with live RSS data."""
        deals_html = "".join([f"<li>{d['aircraft']} from {d['origin']} - {d['price']}</li>" for d in live_deals[:3]])
        
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Elite Aviation Insider | Professional Private Jet Charter Intelligence</title>
            <script type="application/ld+json">
            {{
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": "Elite Aviation Insider",
                "url": "https://yourdomain.com"
            }}
            </script>
            <style>
                body {{ font-family: 'Helvetica Neue', Arial, sans-serif; background: #fff; color: #111; line-height: 1.6; margin: 0; }}
                nav {{ background: #000; color: #fff; padding: 20px; text-align: center; }}
                nav a {{ color: #fff; margin: 0 15px; text-decoration: none; font-weight: bold; }}
                .hero {{ padding: 100px 20px; text-align: center; background: #f8f8f8; }}
                .deals-box {{ background: #000; color: #d4af37; padding: 40px; margin: 40px auto; max-width: 800px; }}
                .footer {{ background: #f0f0f0; padding: 40px; text-align: center; font-size: 0.9rem; }}
            </style>
        </head>
        <body>
            <nav>
                <a href="index.html">HOME</a>
                <a href="about.html">EXPERTISE</a>
                <a href="contact.html">CONTACT</a>
            </nav>
            <div class="hero">
                <h1>Data-Driven Aviation Intelligence</h1>
                <p>Access the world's most sophisticated private jet network with Villiers AI.</p>
                <a href="{self.target_url}" style="background:#000; color:#fff; padding:20px 40px; text-decoration:none;">GET AN INSTANT QUOTE</a>
            </div>
            <div class="deals-box">
                <h2>Live Empty Leg Alerts</h2>
                <ul>{deals_html}</ul>
            </div>
            <div class="footer">
                &copy; 2026 Elite Aviation Insider. <a href="privacy.html">Privacy Policy</a> | <a href="about.html">About Us</a>
            </div>
        </body>
        </html>
        """
        self._save_page("index", html)

    def _save_page(self, name, content):
        with open(f"{self.output_dir}/{name}.html", "w") as f:
            f.write(content)
        logger.info(f"Page {name}.html generated.")

if __name__ == "__main__":
    builder = SiteBuilder()
    builder.generate_privacy_policy()
    builder.generate_about_page()
    builder.generate_contact_page()
    builder.generate_index([{"aircraft": "Global 7500", "origin": "London", "price": "£12,000"}])
