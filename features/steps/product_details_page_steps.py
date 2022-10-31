from behave import given, when, then


@given('Open amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.app.product_details_page.open_url(f'dp/{product_id}')


@when('Add the product to the cart')
def add_product(context):
    context.app.product_details_page.add_product()


@when('Store product name')
def store_product_name(context):
    context.app.product_details_page.store_product_name()

@when('Hover over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.product_details_page.hover_over_new_arrivals()


@then('Verify Women category is present in deals')
def verify_women_deals_present(context):
    context.app.product_details_page.verify_women_deals_present()


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    context.app.product_details_page.verify_can_click_colors()
