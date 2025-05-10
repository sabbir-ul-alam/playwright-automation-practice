from playwright.sync_api import Page
from page_objects.item_page import ItemPage
class LoginPage:
    def __init__(self, page:Page):
        self.page = page

    def visit(self,url):
        self.page.goto(url)

    def login(self, user_name, password):
        self.page.get_by_placeholder("email@example.com").fill(user_name)
        self.page.get_by_placeholder("enter your passsword").fill(password)
        self.page.locator('#login').click()
        # self.page.pause()
        return ItemPage(self.page)





