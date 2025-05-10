from playwright.sync_api import  Page
class PaymentPage:
    def __init__(self,page:Page):
        self.page = page

    def convert_string_to_date(self,val:str):
        return val.split(sep='/')

    def fill_personal_info(self, card_number, exp_date, cvv, name):
        month, day = self.convert_string_to_date(exp_date)
        self.page.locator(".field", has_text="Credit Card Number",
                          has=self.page.locator("input")).fill(card_number)
        self.page.locator(".input.ddl").nth(0).select_option(index=month-1)
        self.page.locator(".input.ddl").nth(1).select_option(index=day - 1)
        self.page.pause()

    def fill_shipping_info(self, email, country):
        pass
