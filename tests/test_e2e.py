
from playwright.sync_api import Page
from page_objects.login_page import LoginPage
import os


def test_login_and_submit_order(page: Page, config, user):

    login_page= LoginPage(page)
    login_page.visit(config["base_url"])
    item_page = login_page.login(user["userEmail"], user["userPassword"])
    item_page.get_item_by_name('ADIDAS ORIGINAL')
    cart_page = item_page.goto_cart()
    payment_page = cart_page.checkout()
    payment_page.fill_personal_info(config["card_number"], config["expiry"],config["cvv"], config["name"])
    payment_page.fill_shipping_info(config["email"], config["country"])
    confirmation_page = payment_page.submit_order()
    confirmation_page.download_csv()


