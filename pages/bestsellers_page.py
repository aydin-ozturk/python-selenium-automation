from pages.base_page import Page
from selenium.webdriver.common.by import By


class BestsellersPage(Page):
    FOOTER_LINKS = (By.XPATH, "//*[@id='zg_header']//a")
    HEADER = (By.CSS_SELECTOR, "#zg_banner_text")

    def open_bestsellers(self):
        self.open_url("gp/bestsellers")

    def verify_footer_links(self):
        footer_links = self.find_elements(*self.FOOTER_LINKS)
        for n in range(len(footer_links)):
            footer_links[n].click()
            header = self.driver.find_element(*self.HEADER).text
            footer_links = self.driver.find_elements(*self.FOOTER_LINKS)
            link_text = footer_links[n].text
            assert link_text in header, \
                f'Expected link text "{link_text}" to be in header {header} but not'

    def verify_footer_link_count(self, expected_link_count):
        actual_link_count = len(self.find_elements(*self.FOOTER_LINKS))
        assert actual_link_count == int(expected_link_count), f"Expected {expected_link_count} but got {actual_link_count}"
