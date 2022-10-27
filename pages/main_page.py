from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class MainPage(Page):
    CART = (By.ID, "nav-cart-count")
    RETURNS_ORDERS = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    SIGN_IN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-button")

    def open_main(self):
        self.open_url()

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click_on_orders(self):
        self.driver.find_element(*self.RETURNS_ORDERS).click()

    def click_on_cart(self):
        self.wait_for_element_click(*self.CART)

    def click_sign_in_popup(self):
        # self.wait_for_element_click(*self.SIGN_IN)
        e = self.driver.wait.until(EC.element_to_be_clickable(self.SIGN_IN), message='Sign in not clickable')
        e.click()

    def verify_signin_popup_clickable(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN),message='Sign in pop up button not clickable')


    def wait_sec(self, sec):
        sleep(int(sec))

    def signin_popup_disappear(self):
        self.wait_for_element_disappear(*self.SIGN_IN)
