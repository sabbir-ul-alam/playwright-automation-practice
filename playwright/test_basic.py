from playwright.sync_api import Page



#here playwright is a global fixture given by playwright
def test_create_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page() #context is like a new fresh browser instace
    page.goto("http://rahulshettyacademy.com")
    context2 = browser.new_context()#one text can have multiple context, context doest share cookies
    page2 = context2.new_page()
    page2.goto("https://www.facebook.com/")


#page is also a global fixture
#here only one single context can be used
def test_create_browser_shortcut(page:Page):
    page.goto("http://rahulshettyacademy.com")



