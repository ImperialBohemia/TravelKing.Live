import trafilatura
import logging
import os
import tempfile
import subprocess
from core.security.validator import Validator


class DiscoveryService:
    """
    Universal Reading Engine for SimpleCodeSpace.
    Uses trafilatura for clean text extraction and playwright for complex JS sites.
    """

    def __init__(self, venv_python="./venv/bin/python3"):
        self.venv_python = venv_python

    def read_url(self, url):
        """Attempts to read a URL after verifying its health."""
        logging.info(f"🌐 Discovery: Initiating verification for {url}")
        
        health = Validator.verify_url_health(url)
        if not health["is_active"]:
            logging.error(f"🛑 Discovery Aborted: {url} is inactive or unreachable.")
            return None

        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            content = trafilatura.extract(downloaded)
            if content:
                return content

        # Fallback to Playwright if static fails or is empty
        logging.warning("Discovery: Static fail, falling back to Headless Browser.")
        return self.read_url_headless(url)

    def read_url_headless(self, url):
        """Uses playwright via a subprocess script to handle JS-heavy sites."""
        script = """
import asyncio
import sys
from playwright.async_api import async_playwright

async def run():
    if len(sys.argv) < 2:
        return
    url = sys.argv[1]
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        content = await page.content()
        await browser.close()
        print(content)

if __name__ == "__main__":
    asyncio.run(run())
"""
        # Use a secure temporary file to avoid race conditions and improve security
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
            tmp.write(script)
            tmp_path = tmp.name

        try:
            # Pass URL as a command line argument to avoid code injection
            res = subprocess.check_output(
                [self.venv_python, tmp_path, url], stderr=subprocess.STDOUT, timeout=120
            ).decode()
            # Feed raw HTML back to trafilatura for cleaning
            return trafilatura.extract(res)
        except subprocess.TimeoutExpired:
            logging.error(f"Discovery: Headless timeout for {url}")
            return None
        except Exception as e:
            logging.error(f"Discovery: Headless failure: {e}")
            return None
        finally:
            if os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except Exception as e:
                    logging.warning(f"Discovery: Failed to remove temp file {tmp_path}: {e}")

    def search_google_products(self, knowledge_manager=None):
        """Specific logic to keep Google Products knowledge updated."""
        wiki_url = "https://en.wikipedia.org/wiki/List_of_Google_products"
        content = self.read_url(wiki_url)
        if content:
            # Save raw knowledge for the Brain
            path = "ai/prompts/google_knowledge_base.txt"
            os.makedirs("ai/prompts", exist_ok=True)
            with open(path, "w") as f:
                f.write(content)
            
            if knowledge_manager:
                knowledge_manager.record_finding("Google Products Wiki", "Knowledge base updated from Wikipedia.")
                
            logging.info("✅ Discovery: Google Knowledge Base updated.")
            return True
        return False
