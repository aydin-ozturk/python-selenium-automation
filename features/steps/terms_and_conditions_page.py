from behave import given, when, then


@given('Open Amazon T&C page')
def open_terms_and_conditions_page(context):
    context.app.terms_and_conditions_page.open_terms_and_conditions_page()


@when('Store original windows')
def store_original_window(context):
    context.app.terms_and_conditions_page.store_original_window()


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.app.terms_and_conditions_page.click_privacy_notice()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.terms_and_conditions_page.switch_to_new_window()


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.app.terms_and_conditions_page.verify_privacy_notice_page_opened()


@then('User can close new window and switch back to original')
def switch_back_original(context):
    context.app.terms_and_conditions_page.switch_back_original()
