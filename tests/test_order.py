import pytest 
from playwright.sync_api import expect
from src import locators
from src import common

def checkout_continue(page):
    page.locator(locators.checkout_continue_button_locator).click()

user_data = {
   "email": "test@email.com",
   "first_name": "Testfirstname",
   "last_name": "Testlastname",
   "phone_code": "+420",
   "phone_number": "722456789"
}

def test_completing_order(page):
    common.visit_dr_max_and_refuse_cookies(page, "/syoss-intense-plex-sampon-pro-silne-poskozene-vlasy-440-ml")

    common.add_to_cart(page)

    page.locator(locators.continue_to_cart_button_locator).click()

    checkout_continue(page)

    selected_checkbox_button = page.locator(locators.selected_checkbox_button_locator)
    selected_checkbox_button.get_by_text("Osobní odběr v lékárně").click()

    pharmacy_for_delivery = page.locator(locators.pharmacy_for_delivery_locator)
    pharmacy_for_delivery.get_by_text("Na poříčí 1048/30").click()

    page.locator(locators.pharmacy_for_delivery_confirmation_button_locator).click()

    payment_method_checkbox = page.get_by_label("V lékárně Zdarma")
    expect(payment_method_checkbox).to_be_checked()

    checkout_continue(page)

    page.locator(locators.email_field_locator).fill(user_data["email"])
  
    page.locator(locators.name_field_locator).fill(user_data["first_name"])
   
    page.locator(locators.last_name_field_locator).fill(user_data["last_name"])

    page.locator(locators.phone_code_field_locator).select_option(user_data["phone_code"])

    page.locator(locators.phone_number_field_locator).fill(user_data["phone_number"])
    
    checkout_continue(page)

    page.locator(locators.accept_conditions_checkbox_locator).check()

    finish_order_button = page.locator(locators.finish_order_button_locator)
    expect(finish_order_button).to_be_visible()
 # I would click finish order, if tested in testing environment,
 # also I would check if the order was created inside of database, via API or in backoffice.
