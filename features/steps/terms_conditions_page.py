from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_NOTICE=(By.LINK_TEXT, "Privacy Notice")
HEADER=(By.CSS_SELECTOR, '.help-service-content h1')

@given('Open Amazon T&C page')
def open_terms_conditions(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ")


@when('Store original windows')
def store_original_window(context):
    context.original_window=context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window=context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    expected_header="Amazon.com Privacy Notice"
    actual_header=context.driver.find_element(*HEADER).text
    assert expected_header==actual_header, f'Expected {expected_header} but got {actual_header}'


@then('User can close new window and switch back to original')
def user_can_switch_back_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
