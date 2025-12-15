from playwright.sync_api import Page, expect
from pathlib import Path
import time


def test_locators_facebook(page: Page):
    # Navigate to Facebook login page
    page.goto("https://www.facebook.com/login/")

    # Create screenshots directory
    screenshots_dir = Path("tests/Screenshot")
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    # Timestamp for unique names
    timestamp = int(time.time())

    # ---------------------------------------------------
    # 1. FULL PAGE SCREENSHOT
    # ---------------------------------------------------
    fullpage_path = screenshots_dir / f"{timestamp}_fullpage.png"
    page.screenshot(path=str(fullpage_path), full_page=True)
    print(f"Saved Full Page screenshot: {fullpage_path}")

    # ---------------------------------------------------
    # 2. NORMAL VIEWPORT SCREENSHOT
    # ---------------------------------------------------
    viewport_path = screenshots_dir / f"{timestamp}_viewport.png"
    page.screenshot(path=str(viewport_path), full_page=False)
    print(f"Saved Viewport screenshot: {viewport_path}")

    # ---------------------------------------------------
    # 3. ELEMENT SCREENSHOT (Facebook logo)
    # ---------------------------------------------------
    logo = page.locator("img[alt='Facebook']")
    element_path = screenshots_dir / f"{timestamp}_logo.png"
    logo.screenshot(path=str(element_path))
    print(f"Saved Element screenshot: {element_path}")
