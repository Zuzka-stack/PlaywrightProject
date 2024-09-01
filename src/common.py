from src import locators

def visit_dr_max_and_refuse_cookies(page, path = ""):
    page.goto("https://www.drmax.cz" + path)
    refuse_button = page.locator(locators.cookiebot_refuse_button_locator)
    refuse_button.click()

def add_to_cart(page):
    page.locator(locators.add_to_cart_button_locator).click()
