import asyncio
import os
import sys
from playwright.async_api import async_playwright

# Path to the HTML we want to embed
HTML_FILE = '/home/q/TravelKing.Live/public_html/help/index.html'
SITE_URL = 'https://sites.google.com/d/1Kc8GEiGzgo2YdyzDViq1T8NXQpipjQwF/edit'
USER_DATA_DIR = os.path.expanduser('~/.config/google-chrome')

async def inject_content():
    with open(HTML_FILE, 'r') as f:
        html_code = f.read()

    async with async_playwright() as p:
        print("🚀 Spouštím prohlížeč s vaším profilem...")
        # Launching with existing user data to bypass login if possible
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False, # We want to see it or at least let it run with UI elements
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
        )
        
        page = await context.new_page()
        print(f"🌐 Otevírám editor: {SITE_URL}")
        
        try:
            await page.goto(SITE_URL, wait_until="networkidle", timeout=60000)
            
            # Check if we need to log in
            if "signin" in page.url or "login" in page.url:
                print("⚠️ Vyžadováno přihlášení! Prosím přihlaste se v okně prohlížeče, pokud se zastavím.")
                # We wait specifically for the editor to appear
                await page.wait_for_selector('div[aria-label="Insert"]', timeout=300000)

            print("✅ Editor načten. Hledám tlačítko 'Embed'...")
            
            # 1. Click 'Insert' tab (usually active by default)
            # 2. Click 'Embed'
            await page.click('div[role="button"][aria-label="Embed"]')
            await asyncio.sleep(2)
            
            # 3. Click 'Embed code' tab in the dialog
            await page.click('div[role="tab"]:has-text("Embed code")')
            await asyncio.sleep(1)
            
            # 4. Paste HTML code
            await page.fill('textarea[aria-label="Embed code"]', html_code)
            await asyncio.sleep(1)
            
            # 5. Click 'Next'
            await page.click('div[role="button"]:has-text("Next")')
            await asyncio.sleep(3)
            
            # 6. Click 'Insert'
            await page.click('div[role="button"]:has-text("Insert")')
            print("✅ HTML vložen do stránky.")
            
            # 7. Resize the embed to be full width/height (this is tricky but Playwright can do it)
            # For now, let's just publish and see
            
            print("📦 Publikuji změny...")
            await page.click('div[role="button"][aria-label="Publish"]')
            await asyncio.sleep(3)
            
            # Confirm publish if there's a diff view
            publish_confirm = await page.query_selector('div[role="button"][data-tooltip="Publish"]:has-text("Publish")')
            if publish_confirm:
                await publish_confirm.click()
                await asyncio.sleep(5)
            
            print("🎉 HOTOVO! Web by měl být live.")

        except Exception as e:
            print(f"❌ Chyba při injektáži: {e}")
        finally:
            await context.close()

if __name__ == "__main__":
    asyncio.run(inject_content())
