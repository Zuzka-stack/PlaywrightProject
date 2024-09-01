import pytest 
from playwright.sync_api import expect
from src import locators
from src import common

def test_navigation_to_product(page):
    common.visit_dr_max_and_refuse_cookies(page)

    page.get_by_role("menuItem", name="Krása a péče").hover()
    
    page.get_by_role("link", name = "Šampony").click()
  
    first_product = page.locator(locators.first_product_locator).first
    first_product.get_by_role("heading").click()
  
    add_to_cart_button = page.locator(locators.add_to_cart_button_locator)
    expect(add_to_cart_button).to_be_visible()
