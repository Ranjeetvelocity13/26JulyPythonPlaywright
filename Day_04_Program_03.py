from playwright.sync_api import Page, expect
import time

# def test_handle_Iframe(page: Page):

#     page.goto('https://demo.automationtesting.in/Frames.html')

#     frameLoc =page.frame_locator('iframe').first

#     frameLoc.locator('input[type="text"]').fill("Welcome")

#     page.locator("//a[contains(text(),'Home')]").click()

#     time.sleep(3)


def test_nested_iframe(page:Page):
    page.goto('https://demo.automationtesting.in/Frames.html')

    
    page.locator("//a[contains(text(),'Iframe with in an Iframe')]").click()

    outerframe =page.frame_locator('#Multiple iframe')
  
    nestedText =outerframe.locator("//h5[contains(text(),'Nested iFrames')]")
    print(nestedText)

    innerFrame =outerframe.frame_locator('iframe')
    innerFrame.locator('input[type="text"]').fill("Welcome to nested iframe")

    time.sleep(3)