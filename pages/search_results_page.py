from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    ALL_PRODUCT_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 span.a-text-normal")
    SEARCH_RESULT = (
    By.XPATH, "//span[@data-component-type='s-result-info-bar']//span[@class='a-color-state a-text-bold']")
    SELECTED_DEPARTMENT = (By.CSS_SELECTOR, "#nav-subnav[data-category='{DEPARTMENT}']")

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.SEARCH_RESULT)

    def select_first_product(self):
        self.find_element(*self.PRODUCT_PRICE).click()

    def verify_product_name_img(self):
        products = self.find_elements(*self.ALL_PRODUCT_RESULTS)
        for product in products:
            title = product.find_element(*self.PRODUCT_TITLE).text
            assert title, "Error! Title should not be blank"
            assert product.find_element(*self.PRODUCT_IMG), "Image is not shown"

    def get_department_locator(self, department:str):
        return [self.SELECTED_DEPARTMENT[0], self.SELECTED_DEPARTMENT[1].replace("{DEPARTMENT}", department)]

    def verify_department(self, department):
        department_locator = self.get_department_locator(department)
        print(department_locator)
        self.wait_for_element_appear(*department_locator)




