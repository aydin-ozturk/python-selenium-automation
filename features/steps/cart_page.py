from behave import given, when, then


@then('Verify "Your Amazon Cart is empty" notification is present')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    context.app.cart_page.verify_cart_count(expected_count)


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name()
