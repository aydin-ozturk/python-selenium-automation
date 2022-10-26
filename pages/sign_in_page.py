from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class SignInPage(Page):

    def verify_sign_in_page_opened(self):
        # self.driver.wait.until(EC.url_contains("ap/signin"), message='Sign in URL did not open')
        self.wait.until(EC.url_contains("ap/signin"))