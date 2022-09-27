from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com")


@when('Click on returns and orders')
def click_on_returns(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
