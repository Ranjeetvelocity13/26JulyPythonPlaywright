from playwright.sync_api import Page, expect


def test_handle_dropdown(page: Page):

    page.goto('https://testautomationpractice.blogspot.com/')

    page.select_option('#colors', ['Blue','Red', 'White'])
    page.wait_for_timeout(4000)
    
    options_locators =page.locator('#colors option')
    expect(options_locators).to_have_count(7)

    allText =options_locators.all_text_contents()
    print("All dropdown text",allText)
    
    page.wait_for_timeout(4000)
