from playwright.sync_api import Page,expect

def test_alert_popup_assertion(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.click("#alertBtn")
    #Define dialog handler
    # 
    def handl_dialog(dialog):
        assert dialog.message == "I am an alert box!"
        dialog.accept()
    
    page.once("dialog", handl_dialog)
    page.locator("#alertBtn").click()
    page.wait_for_timeout(3000)