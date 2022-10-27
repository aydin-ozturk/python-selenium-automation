from behave import given, when, then


@given('Open best seller page')
def open_best_seller(context):
    context.app.bestsellers_page.open_bestsellers()


@then('Verify footer has {expected_link_count} link(s)')
def verify_footer_link_count(context, expected_link_count):
    context.app.bestsellers_page.verify_footer_link_count(expected_link_count)


@then('Click on each link and verify footer includes link name')
def verify_footer_links(context):
    context.app.bestsellers_page.verify_footer_links()
