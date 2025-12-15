import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://www.facebook.com/")
    page.get_by_test_id("open-registration-form-button").click()
    page.get_by_role("textbox", name="First name").click()
    page.get_by_role("textbox", name="First name").fill("Rahul")
    page.get_by_role("textbox", name="Surname").click()
    page.get_by_role("textbox", name="Surname").fill("Patil")
    page.get_by_label("Day").select_option("11")
    page.get_by_label("Month").select_option("11")
    page.get_by_label("Year").select_option("2018")
    page.get_by_role("radio", name="Female").check()
    page.get_by_role("textbox", name="Mobile number or email address").click()
    page.get_by_role("textbox", name="Mobile number or email address").fill("8765345678")
    page.get_by_role("textbox", name="New password").click()
    page.get_by_role("textbox", name="New password").fill("Er@123")
