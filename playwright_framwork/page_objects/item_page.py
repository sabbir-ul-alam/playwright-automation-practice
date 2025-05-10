from playwright.sync_api import Page
class ItemPage:
    def __init__(self,page:Page):
        self.page = page