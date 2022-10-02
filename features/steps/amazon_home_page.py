from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_BAR=(By.ID, "twotabsearchtextbox")
SEARCH_BTN=(By.ID, "nav-search-submit-button")
CART=(By.ID, "nav-cart-count")
RETURNS_ORDERS=(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com")
    context.driver.refresh()


@when('Click on returns and orders')
def click_on_returns(context):
    context.driver.find_element(*RETURNS_ORDERS).click()


@when('Click on Cart')
def click_on_cart(context):
    context.driver.find_element(*CART).click()


@when('Search for "{product}"')
def searh_product(context, product):
    element=context.driver.find_element(*SEARCH_BAR)
    element.clear()
    element.send_keys('Black Panther Luxury Car Seat Cover Front')
    context.driver.find_element(*SEARCH_BTN).click()
