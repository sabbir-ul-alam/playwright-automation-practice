from playwright.sync_api import Page
from page_objects.confirmation_page import ConfirmationPage

class PaymentPage:
    def __init__(self, page: Page):
        self.page = page


    def convert_string_to_date(self,val:str):
        return val.split(sep='/')

    def fill_personal_info(self, card_number, exp_date, cvv, name):
        month, day = self.convert_string_to_date(exp_date)
        #self.page.locator(".field:has-text('Credit Card Number') input").fill(card_number)

        self.page.locator(
            ".field", has_text="Credit Card Number").locator(
            "input").fill(card_number)
        self.page.locator(".input.ddl").nth(0).select_option(index=int(month)-1)
        self.page.locator(".input.ddl").nth(1).select_option(index=int(day) - 1)

        self.page.locator(".field.small:has-text('CVV Code') input").fill(str(cvv))
        self.page.locator(".field:has-text('Name on Card ') input").fill(name)

    def fill_shipping_info(self, email, country):
        self.page.locator('.user__name input').first.fill(email)
        self.page.get_by_placeholder("Select Country").type(country)
        # self.page.pause()
        self.page.get_by_role('button', name='Button').click()

    def submit_order(self):
        self.page.locator('.action__submit').click()
        return ConfirmationPage(self.page)

