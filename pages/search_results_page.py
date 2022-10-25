from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@data-component-type='s-result-info-bar']//span[@class='a-color-state a-text-bold']")

    def verify_search_results(self, expected_result):
       self.verify_element_text(expected_result, *self.SEARCH_RESULT)