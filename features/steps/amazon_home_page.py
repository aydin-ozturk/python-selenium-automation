from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com")
    context.driver.refresh()


@when('Click on returns and orders')
def click_on_returns(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()


@when('Click on Cart')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='nav-cart-icon']").click()


@when('Search a product using search bar')
def searh_product(context):
    context.driver.find_element(By.ID, "twotabsearchtextbox").clear()
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys('Black Panther Luxury Car Seat Cover Front')
    context.driver.find_element(By.ID, "nav-search-submit-button").click()
