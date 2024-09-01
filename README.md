# PlaywrightProject

## About

Automatic tests written in playrwight python, goal of this collection of tests is to verify basic functionality of eshop [DrMax CZ](www.drmax.cz).

### Contains 3 test scenarios:

  1. test_navigation_to product - shows choosing product from categories and ensures add to cart button is visible
  2. test_add_to_cart - checks every step of adding product to cart and ensures correct product is added
  3. test_order - checks steps of finishing order, without the last step because test is running in production environment (steps for finishing order in testing env
  ironment are provided in comments)

## How to run

 - Python version 3.10.2 is needed
 - to install pytest use pip install -U pytest
 - to install playwright use pip install pytest-playwright
