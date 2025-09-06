from playwright.sync_api import sync_playwright
import time

def test_open_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set True for headless
        page = browser.new_page()
        page.goto("https://www.google.com")
        time.sleep(20)
        assert "Google" in page.title()
        browser.close()