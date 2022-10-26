from behave import given, when, then


@then('Verify Sign In page is opened')
def verify_sign_in_page_opened(context):
    context.app.sign_in_page.verify_sign_in_page_opened()