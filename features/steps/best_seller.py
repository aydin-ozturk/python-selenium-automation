from selenium.webdriver.common.by import By
from behave import given, when, then

# FOOTER_LINKS=(By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a')
FOOTER_LINKS=(By.XPATH, "//*[@id='zg_header']//a")

@given('Open best seller page')
def open_best_seller(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then('Verify footer has {expected_link_count} link(s)')
def verify_footer_links(context,expected_link_count):
    all_links_count= len(context.driver.find_elements(*FOOTER_LINKS))
    assert int(expected_link_count)==all_links_count, \
        f'Expected {expected_link_count} links but got {all_links_count}'


@then('Click on each link')   #stale element example
def verify_footer_links(context):
    footer_links=context.driver.find_elements(*FOOTER_LINKS)
    for r in range(len(footer_links)):
        footer_links=context.driver.find_elements(*FOOTER_LINKS)
        footer_links[r].click()
        r += 1

