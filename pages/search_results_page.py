from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@data-component-type='s-result-info-bar']//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")

    def verify_search_results(self, expected_result):
       self.verify_element_text(expected_result, *self.SEARCH_RESULT)

    def select_first_product(self):
        self.driver.find_element(*self.PRODUCT_PRICE).click()
