# File: Day_01_FirstProgram.py
import re
from playwright.sync_api import Page, expect

# -----------------------------------------------------------
# TEST 1: Verify that the homepage title contains “Playwright”
# -----------------------------------------------------------
def test_has_title(page: Page):
    # Navigate to Playwright official website
    page.goto("https://playwright.dev/")

    # Validate page title using regex (dynamic match)
    expect(page).to_have_title(re.compile("Playwright"))


# -----------------------------------------------------------
# TEST 2: Open homepage and verify the title again
# (Duplicate test for practice and understanding)
# -----------------------------------------------------------
def test_homepage_navigation(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))


# -----------------------------------------------------------
# TEST 3: Read & Print Page Title
# -----------------------------------------------------------
def test_homepage_navigation1(page: Page):
    page.goto("https://playwright.dev/")

    # Validate page title
    expect(page).to_have_title(re.compile("Playwright"))

    # Print the page title on console (only visible with -s flag)
    print("Page title:", page.title())    # Read and print title


"""
-----------------------------------------------------------
How to Run These Tests (Important Notes)
-----------------------------------------------------------

1️⃣ Install Playwright
    pip install playwright

2️⃣ Install Playwright browsers
    playwright install

3️⃣ Run tests normally
    pytest Day_01_FirstProgram.py -v

4️⃣ Run tests in HEADED mode (open browser window)
    pytest Day_01_FirstProgram.py --headed -v

5️⃣ Show print statements in console
    pytest Day_01_FirstProgram.py -v -s

6️⃣ Run on a specific browser:
    pytest Day_01_FirstProgram.py --browser chromium -v
    pytest Day_01_FirstProgram.py --browser firefox -v
    pytest Day_01_FirstProgram.py --browser webkit -v

7️⃣ Run on ALL browsers:
    pytest Day_01_FirstProgram.py --browser chromium --browser firefox --browser webkit -v
-----------------------------------------------------------
"""
