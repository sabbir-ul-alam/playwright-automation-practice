
from playwright.sync_api import Page
from page_objects.login_page import LoginPage


def test_login_and_submit_order(page: Page):
    login_page= LoginPage(page)
    login_page.visit("https://rahulshettyacademy.com/client")
    item_page = login_page.login('anshika@gmail.com','Iamking@000')
    item_page.get_item_by_name('ADIDAS ORIGINAL')
    cart_page = item_page.goto_cart()
    cart_page.checkout()


