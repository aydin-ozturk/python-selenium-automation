from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")
SEARCH_RESULT_TEXT = (
By.XPATH, "//span[@data-component-type='s-result-info-bar']//span[@class='a-color-state a-text-bold']")
ALL_PRODUCT_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 span.a-text-normal")
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@when('Click on the first product')
def select_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Search results for {search_result} is shown')
def search_product_res(context, search_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert actual_result == search_result, f"Expected {search_result} but got {actual_result}"


@then('Verify every product has a name and image')
def verify_name_img(context):
    products = context.driver.find_elements(*ALL_PRODUCT_RESULTS)
    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, "Error! Title should not be blank"
        assert product.find_element(*PRODUCT_IMG), "Image is not shown"
