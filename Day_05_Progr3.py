import pytest
from playwright.sync_api import Page, expect

def test_alert_popup_assertion(page: Page):
    # Step 1: Open the application
    page.goto("https://testautomationpractice.blogspot.com/")

    # Step 2: Define dialog (alert) handler
    def handle_dialog(dialog):
        # Validate dialog type
        assert dialog.type == "alert"

        # Validate alert message
        assert "I am an alert box!" in dialog.message

        # Accept the alert
        dialog.accept()

    # Step 3: Register dialog handler (runs only once)
    page.once("dialog", handle_dialog)

    # Step 4: Click button that triggers alert
    page.click("#alertBtn")

    # Step 5: Optional wait to observe behavior
    page.wait_for_timeout(2000)
