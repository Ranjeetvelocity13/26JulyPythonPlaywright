from playwright.sync_api import Page, expect
import time

def test_drag_and_Drop(page:Page):
    page.goto('https://www.globalsqa.com/demo-site/draganddrop/')

    frame_element = page.wait_for_selector('iframe.demo-frame')
    frame =frame_element.content_frame()
    src =frame.locator('//img[@alt="The peaks of High Tatras"]')

    dest =frame.locator('#trash')
    src.drag_to(dest)

    page.wait_for_timeout(3000)