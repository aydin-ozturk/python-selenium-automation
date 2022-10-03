from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_PRICE=(By.XPATH,"//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")
SEARCH_RESULT_TEXT=(By.XPATH,"//span[@data-component-type='s-result-info-bar']//span[@class='a-color-state a-text-bold']")

@when('Click on the first product')
def select_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()

@then('Search results for {search_result} is shown')
def search_product_res(context,search_result):
    actual_result=context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert actual_result==search_result, f"Expected {search_result} but got {actual_result}"
