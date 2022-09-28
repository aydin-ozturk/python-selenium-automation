from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify "Your Amazon Cart is empty" notification is present')
def verify_cart_empty(context):
    expected_result="Your Amazon Cart is empty"
    actual_result=context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text
    assert expected_result==actual_result, f'Expected {expected_result} but got {actual_result}'