from playwright.sync_api import Page, expect
import time

def test_Mouse_Hover(page: Page):

    page.goto('https://demo.automationtesting.in/Register.html')

    Switch=page.locator("//a[text()='SwitchTo']")
    Switch.hover()

    time.sleep(2)
    Widgets =page.locator("//a[text()='Widgets']")
    Widgets.hover()

    time.sleep(4)
