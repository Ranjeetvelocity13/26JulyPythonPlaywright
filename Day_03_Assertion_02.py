from playwright.sync_api import Page, expect

def test_soft_assertions_manual(page: Page):

    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    product = page.locator(".inventory_item")

    expect(product).to_have_count(6)

    errors = []

    # 1st product — should pass
    try:
        assert "Sauce Labs Backpack" in product.nth(0).text_content()
    except AssertionError as e:
        errors.append("Soft Assert 1 Failed: " + str(e))

    # 2nd product — corrected text
    try:
        assert "Sauce Labs Bike Light" in product.nth(1).text_content()
    except AssertionError as e:
        errors.append("Soft Assert 2 Failed: " + str(e))

    # 3rd product — also valid
    try:
        assert "Sauce Labs Bolt T-Shirt" in product.nth(2).text_content()
    except AssertionError as e:
        errors.append("Soft Assert 3 Failed: " + str(e))

    if errors:
        raise AssertionError("\n".join(errors))

    print("All soft assertions passed successfully!")
