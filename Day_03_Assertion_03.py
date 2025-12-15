from playwright.sync_api import Page, expect
from pathlib import Path
import time


def test_locators_facebook(page: Page):

    # Navigate to registration page
    page.goto("https://demo.automationtesting.in/Register.html")

    # ---------------------------------------------------------
    # PAGE-LEVEL ASSERTIONS
    # ---------------------------------------------------------
    expect(page).to_have_title("Register")
    expect(page).to_have_url("https://demo.automationtesting.in/Register.html")

    # ---------------------------------------------------------
    # HEADER ASSERTION
    # ---------------------------------------------------------
    header = page.locator(".container h2")
    expect(header).to_be_visible()
    expect(header).to_have_text("Register")

    # ---------------------------------------------------------
    # BUTTON ASSERTIONS
    # ---------------------------------------------------------
    submit_btn = page.locator("#submitbtn")
    expect(submit_btn).to_be_visible()
    expect(submit_btn).to_be_enabled()

    # Negative assertion example (button should NOT have wrong text)
    expect(submit_btn).not_to_have_text("WrongText")

    # ---------------------------------------------------------
    # INPUT FIELD ASSERTIONS
    # ---------------------------------------------------------
    fname = page.locator('[placeholder="First Name"]')
    lname = page.locator('[placeholder="Last Name"]')

    expect(fname).to_be_visible()
    expect(lname).to_be_visible()

    # Placeholder check (important UI validation)
    expect(fname).to_have_attribute("placeholder", "First Name")
    expect(lname).to_have_attribute("placeholder", "Last Name")

    # Fill values and validate
    fname.fill("Ranjeet")
    lname.fill("Automation")

    expect(fname).to_have_value("Ranjeet")
    expect(lname).to_have_value("Automation")

    # ---------------------------------------------------------
    # DROPDOWN ASSERTIONS
    # ---------------------------------------------------------
    country_list = page.locator("#countries option")
    expect(country_list).to_have_count(250)   # number may vary — example

    # ---------------------------------------------------------
    # RADIO BUTTON ASSERTION
    # ---------------------------------------------------------
    male_radio = page.locator("input[value='Male']")
    expect(male_radio).to_be_visible()
    male_radio.check()
    expect(male_radio).to_be_checked()

    # ---------------------------------------------------------
    # CHECKBOX VALIDATION
    # ---------------------------------------------------------
    hobbies_checkbox = page.locator("#checkbox1")
    hobbies_checkbox.check()
    expect(hobbies_checkbox).to_be_checked()

    print("All assertions executed successfully!")
