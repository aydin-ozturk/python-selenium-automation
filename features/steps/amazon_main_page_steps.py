from behave import given, when, then


@given('Open Amazon home page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Click on returns and orders')
def click_on_returns(context):
    context.app.main_page.click_on_orders()


@when('Click on Cart')
def click_on_cart(context):
    context.app.main_page.click_on_cart()


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search_product(product)


@when('Click on sign in pop up')
def click_sign_in_popup(context):
    context.app.main_page.click_sign_in_popup()


@when('Wait for {sec} sec')
def wait_sec(context, sec):
    context.app.main_page.wait_sec(sec)


@when("Select department by value {value}")
def select_department(context, value):
    context.app.main_page.select_department(value)


@when("Hover over language options")
def hover_over_language(context):
    context.app.main_page.hover_over_language()


@then("Verify Spanish option is present")
def verify_spanish_language_present(context):
    context.app.main_page.verify_spanish_language_present()


@then('Verify sign in pop up button is clickable')
def verify_signin_popup_clickable(context):
    context.app.main_page.verify_signin_popup_clickable()


@then('Verify sign in pop up button disappears')
def signin_popup_disappear(context):
    context.app.main_page.signin_popup_disappear()
