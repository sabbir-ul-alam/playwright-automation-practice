from playwright.sync_api import Page
from page_objects.payment_page import PaymentPage


class CartPage:
    def __init__(self,page:Page):
        self.page= page

    def checkout(self):
        self.page.get_by_role('button', name='Checkout').click()
        return PaymentPage(self.page)
