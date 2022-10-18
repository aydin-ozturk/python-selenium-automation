from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Redirected to sign in page with "Sign in" header and email input field')
def verify_sign_in_header(context):
    expected_header = "Sign in"
    actual_header = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in')]").text
    assert expected_header == actual_header, f'Expected {expected_header} but got {actual_header}'
    assert context.driver.find_element(By.ID, "ap_email"), 'Email field not shown'


@then('Verify sign in page opened')
def verify_sign_in_page_opened(context):
    context.driver.wait.until(EC.url_contains("ap/signin"), message='Sign in URL did not open')