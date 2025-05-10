from page_objects.cart_page import  CartPage
from playwright.sync_api import Page
class ItemPage:
    def __init__(self,page:Page):
        self.page = page

    def get_item_by_name(self,product_name):
        (self.page.locator('.card-body',has_text=product_name).
         get_by_role("button",name='Add To Cart')).click()

    def goto_cart(self):
        self.page.locator(".btn.btn-custom", has_text='Cart').click()
        return CartPage(self.page)

