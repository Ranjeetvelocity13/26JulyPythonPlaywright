# Locator Types in Playwright
# ---------------------------
# CSS Selector
# XPath
# Text Locator
# Role Locator
# ID Locator
# Placeholder Locator
# Label Locator
# Title Locator
# GetBy methods (get_by_role, get_by_text, etc.)

from playwright.sync_api import Page, expect

def test_Locators(page: Page):
    
    # Navigate to website
    page.goto("https://www.demoblaze.com/index.html")

    # ------------------------------
    # 1️⃣ ID Locator (CSS)
    # ------------------------------
    page.locator('[id="login2"]').click()     # CSS attribute selector
    # Alternative:
    # page.locator("#login2").click()         # CSS ID selector

    # ------------------------------
    # 2️⃣ Placeholder OR Input field
    # ------------------------------
    page.locator("#loginusername").fill("pavanol")
    page.locator('#loginpassword').fill("test@123")

    # ------------------------------
    # 3️⃣ XPath Locator
    # ------------------------------
    # Using contains(text()) and class attribute
    page.locator("//button[contains(text(),'Log in')]").click()

    # page.wait_for_timeout(5000)   # Not recommended, only for demo


"""
-----------------------------------------------------
Locators in Playwright (Detailed Notes)
-----------------------------------------------------

1. CSS Selectors:
-----------------------------------------------------
#login2
input[name='username']
button.btn-primary
div[class='container']

2. XPath:
-----------------------------------------------------
Absolute  : /html/body/div[2]/div/div
Relative  : //input[@id='loginusername']
By text   : //button[text()='Log in']
Contains  : //a[contains(text(),'Home')]
AND/OR    : //input[@id='user' and @type='text']

3. Text Locator (BEST FEATURE in Playwright):
-----------------------------------------------------
page.get_by_text("Log in").click()

4. Role Locator (Accessibility-based)
-----------------------------------------------------
page.get_by_role("button", name="Log in").click()

5. Label Locator:
-----------------------------------------------------
page.get_by_label("Username").fill("abc")

6. Placeholder Locator:
-----------------------------------------------------
page.get_by_placeholder("Enter username").fill("abc")

7. Title Locator:
-----------------------------------------------------
page.get_by_title("Login").click()

-----------------------------------------------------
Which locator is best?
-----------------------------------------------------
1️⃣ get_by_role → MOST stable  
2️⃣ get_by_text → Easy for buttons/links  
3️⃣ CSS selector → Fast & clean  
4️⃣ XPath → When structure is complex  
"""

