#What is pom - Page object model 
# POM is test automation design paterrn in which every webpage of u=your application
# is represent as sprate class and all locators, all actions

# //Poroject
# tests/
#    test_login.py
   
# pages/
#     login_Page.py
#     abc_page.py

#     conftest.py


# tests/test_login.py
from playwright.sync_api import Page
from pages1.login_page import LoginPage

def test_login(page: Page):
    # Create page object (calls constructor)
    login_page = LoginPage(page)
    
    # Use page object methods
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
