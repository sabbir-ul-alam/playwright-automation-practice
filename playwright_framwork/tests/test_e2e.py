
from playwright.sync_api import Page
from playwright_framwork.page_objects.login_page import Login

def test_login_and_submit_order(page: Page):
    login_page= Login(page)
    login_page.visit("https://rahulshettyacademy.com/client")
    login_page.login('anshika@gmail.com','Iamking@000')