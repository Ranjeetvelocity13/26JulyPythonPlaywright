from playwright.sync_api import Page, expect
import time

def test_DropDown(page: Page):

    page.goto('https://www.w3schools.com/')
    page.evaluate("window.scrollBy(0,document.body.scrollHeight)")
    page.wait_for_timeout(5000)
    page.evaluate("document.documentElement.scrollTop=0");
    page.wait_for_timeout(5000)


def test_DropDown(page: Page):

    page.goto('https://www.w3schools.com/')
    targer =page.locator("//h1[contains(text(),'Code Editor')]")
    targer.scroll_into_view_if_needed()

    page.wait_for_timeout