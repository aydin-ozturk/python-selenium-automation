from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SIGN_IN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-button")
BEST_SELLERS = (By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")


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
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign in not clickable')
    e.click()


@when('Wait for {sec} sec')
def wait_sec(context, sec):
    sleep(int(sec))


@when('Click on best sellers')
def open_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@then('Verify sign in pop up button is clickable')
def verify_signin_popup_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign in pop up button not clickable')


@then('Verify sign in pop up button disappears')
def signin_popup_disappear(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN),
                              message='Sign in pop up button did not disappear')
