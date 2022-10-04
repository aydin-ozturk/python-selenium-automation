from selenium.webdriver.common.by import By
from behave import given, when, then

# FOOTER_LINKS=(By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a')
FOOTER_LINKS=(By.XPATH, "//*[@id='zg_header']//a")

@given('Open best seller page')
def open_best_seller(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then('Verify footer has {expected_link_count} link(s)')
def verify_footer_links(context,expected_link_count):
    footer_links=context.driver.find_elements(*FOOTER_LINKS)
    print(footer_links)
    footer_link_count=len(footer_links)
    assert int(expected_link_count) == footer_link_count, f'Expected {expected_link_count} but got {footer_link_count}'
