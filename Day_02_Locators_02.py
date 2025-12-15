from playwright.sync_api import Page, expect

def test_Locators(page: Page):
    # Step 1: Open the webpage
    page.goto("https://www.demoblaze.com/index.html")

    # Step 2: Click on the Login button (locator by ID)
    page.locator('#login2').click()
    # Alternate method:
    # page.click("#login2")

    # Static wait (NOT recommended for real automation, but useful for demo)
    page.wait_for_timeout(1000)

    # Step 3: Enter username (locator by attribute)
    page.locator('[id="loginusername"]').fill("pavanol")

    # Step 4: Enter password (locator by ID)
    page.locator('#loginpassword').fill("test@123")
    # Alternate:
    # page.fill('#loginpassword', "test@123")

    # Step 5: Click on Login button using XPath (locator by text + class)
    page.locator('//button[contains(text(),"Log in") and @class="btn btn-primary"]').click()

    # -----------------------------------------------
    # FIND ALL ANCHOR LINKS ON THE WEBPAGE
    # -----------------------------------------------
    print("\nAll links on the webpage:")
    links = page.locator('a').all()   # Fetch all <a> tags (anchor links)

    for link in links:
        link_text = link.text_content()
        print(link_text)

    print('-------------------------------------')

    # -----------------------------------------------
    # FIND PRODUCT NAMES FROM THE HOME PAGE LIST
    # -----------------------------------------------
    print("\nProduct names on Home Page:")
    products = page.locator('//div[@id="tbodyid"]//h4//a').all()

    for product in products:
        p_name = product.text_content()
        print(p_name)


"""
📘 NOTES: XPath & CSS Selectors
-------------------------------------------------

🎯 XPATH TYPES
1) Absolute XPath
   /html/body/div[2]/div[1]/h4

2) Relative XPath (recommended)
   //input[@id='username']

3) XPath by attribute
   //button[@type='submit']

4) XPath by text()
   //a[text()='Login']

5) XPath contains()
   //a[contains(text(),'Log')]

6) XPath by AND/OR
   //input[@id='user' and @type='text']

7) XPath axes
   parent::, child::, following-sibling::, ancestor::

🎯 CSS SELECTOR TYPES
1) By ID
   #login2

2) Tag + ID
   button#login2

3) By attribute
   [id="loginusername"]

4) Tag + attribute
   input[type="text"]

-------------------------------------------------

❗ CSS VS XPATH
-------------------------------------------------
CSS Selector:
- Faster
- Cleaner syntax
- CANNOT traverse backward (no parent access)
- Preferred in Playwright

XPath:
- Can traverse up/down anywhere in DOM
- Supports text(), contains(), axes
- Slower but powerful
"""
