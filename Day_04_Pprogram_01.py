from playwright.sync_api import Page, expect


def test_handle_dropdown(page: Page):

    page.goto('https://www.facebook.com/r.php?entry_point=login')

    page.wait_for_selector('#day')
    page.wait_for_selector('#month')
    page.wait_for_selector('#year')

    page.select_option('#day', '15')
    page.select_option('#month', label='Apr')
    page.select_option('#year', '1994')

    page.wait_for_timeout(4000)

    selected_day=page.locator('#day').input_value();
    selected_month=page.locator('#month').input_value();
    selected_year=page.locator('#year').input_value();

    #print(selected_day)
    # assert selected_day == '15',f"Expected day '15', got '{selected_day}'"
    # assert selected_month == '4' f"Expected day '4', got '{selected_month}'"
    # assert selected_year == '1994' f"Expected day '1994', got '{selected_year}'"
     
    expect(page.locator('#day')).to_have_value('15');
    expect(page.locator('#month')).to_have_value('Apr');