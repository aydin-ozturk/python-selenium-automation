from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN=(By.ID, "add-to-cart-button")


@when('Add the product to the cart')
def add_product(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
