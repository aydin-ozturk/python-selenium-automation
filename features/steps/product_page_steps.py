from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN=(By.ID, "add-to-cart-button")
PRODUCT_NAME=(By.ID, "productTitle")

@when('Add the product to the cart')
def add_product(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@when('Store product name')
def store_product_name(context):
    context.product_name=context.driver.find_element(*PRODUCT_NAME).text
    print(f'\nCurrent product: {context.product_name}')