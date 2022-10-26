from selenium.webdriver.common.by import By
from behave import given, when, then

ALL_PRODUCT_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 span.a-text-normal")
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@when('Click on the first product')
def select_first_product(context):
    context.app.search_results_page.select_first_product()


@then('Search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)

@then('Verify every product has a name and image')
def verify_name_img(context):
    products = context.driver.find_elements(*ALL_PRODUCT_RESULTS)
    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, "Error! Title should not be blank"
        assert product.find_element(*PRODUCT_IMG), "Image is not shown"
