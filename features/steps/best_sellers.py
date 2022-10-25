from behave import given, when, then



@given('Open best seller page')
def open_best_seller(context):
    context.app.bestsellers_page.open_bestsellers()


@then('Verify footer has {expected_link_count} link(s)')
def verify_footer_links(context, expected_link_count):
    all_links_count = len(context.driver.find_elements(*FOOTER_LINKS))
    assert int(expected_link_count) == all_links_count, \
        f'Expected {expected_link_count} links but got {all_links_count}'


@then('Click on each link and verify header includes link name')
def verify_footer_links(context):
    context.app.bestsellers_page.verify_footer_links()
