from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TermsAndConditionsPage(Page):
    PRIVACY_NOTICE = (By.LINK_TEXT, "Privacy Notice")
    HEADER = (By.CSS_SELECTOR, '.help-service-content h1')
    original_window = None

    def open_terms_and_conditions_page(self):
        self.open_url(
            "gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")

    def store_original_window(self):
        self.original_window = self.driver.current_window_handle

    def click_privacy_notice(self):
        self.click(*self.PRIVACY_NOTICE)

    def switch_to_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def verify_privacy_notice_page_opened(self):
        self.verify_element_text("Amazon.com Privacy Notice", *self.HEADER)

    def switch_back_original(self):
        self.driver.close()
        self.driver.switch_to.window(self.original_window)
