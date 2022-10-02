from selenium.webdriver.common.by import By
from behave import given, when, then

CART=(By.ID, "nav-cart-count")


@then('Verify "Your Amazon Cart is empty" notification is present')
def verify_cart_empty(context):
    expected_result="Your Amazon Cart is empty"
    actual_result=context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text
    assert expected_result==actual_result, f'Expected {expected_result} but got {actual_result}'

@then('Then verify cart has {expected_count} item(s)')
def verify_cart_item(context, expected_count):
    actual_count=context.driver.find_element(*CART).text
    assert  expected_count==actual_count, f'Expected {expected_count}, but got {actual_count}'