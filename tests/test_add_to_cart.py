import pytest
from playwright.sync_api import expect
from src import locators
from src import common

def test_add_to_cart(page):
    expected_product_title = "Syoss Intense Plex šampon pro silně poškozené vlasy 440 ml"

    common.visit_dr_max_and_refuse_cookies(page,"/syoss-intense-plex-sampon-pro-silne-poskozene-vlasy-440-ml")

    common.add_to_cart(page)

    page.locator(locators.continue_shopping_button_locator).click()
    
    page.locator(locators.microcart_button_locator).click()

    product_in_cart_preview = page.locator(locators.product_in_cart_preview_locator)
    expect(product_in_cart_preview).to_be_visible()
    expect(product_in_cart_preview).to_contain_text(expected_product_title)
    
    page.locator(locators.cart_details_locator).click()

    product_in_cart = page.locator(locators.product_in_cart_locator)
    expect(product_in_cart).to_be_visible()
    expect(product_in_cart).to_contain_text(expected_product_title)
