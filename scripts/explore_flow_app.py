
import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = '/home/q/TravelKing.Live/tmp_profile/google-chrome'

async def explore_app():
    async with async_playwright() as p:
        print("🚀 Launching Headless Browser for Google Flow App Exploration...")
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        page = await context.new_page()
        
        # Test the direct tool URL
        url = 'https://labs.google/fx/tools/flow/'
        print(f"🌐 Navigating to {url}...")
        try:
            await page.goto(url, wait_until="networkidle", timeout=60000)
            await asyncio.sleep(8)
            
            # Check if we are logged in or if there is a 'Get started' button
            await page.screenshot(path="flow_app_start.png")
            print("📸 Checkout flow_app_start.png")
            
            # Check content for "Sign in" or "Create project"
            content = await page.content()
            if "Sign in" in content:
                print("⚠️ Not logged in! (Found 'Sign in')")
            elif "New project" in content or "Create project" in content:
                print("✅ Logged in! Found Project creation buttons.")
                # Try to find the prompt box for image generation
            
            # List all buttons and their roles
            elements = await page.query_selector_all('button, div[role="button"]')
            for el in elements:
                text = await el.inner_text()
                label = await el.get_attribute("aria-label")
                if text or label:
                    print(f"🔘 Element: Text='{text.strip()}' Label='{label}'")

        except Exception as e:
            print(f"❌ Error: {e}")
            await page.screenshot(path="flow_app_error.png")
        finally:
            await context.close()

if __name__ == "__main__":
    asyncio.run(explore_app())
