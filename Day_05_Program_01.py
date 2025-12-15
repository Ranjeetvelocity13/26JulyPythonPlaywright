from playwright.sync_api import Page, expect
import time

def test_double_click(page:Page):

    page.goto("https://demo.guru99.com/test/simple_context_menu.html")
    double_click =page.locator("//button[contains(text(),'Double-Click Me To See Alert')]")
    double_click.db()

    page.wait_for_timeout(4000)

