from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.ui import Select


class MainPage(Page):
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    SIGN_IN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-button")
    DEPARTMENT_SELECTION = (By.ID, "searchDropdownBox")
    RETURNS_ORDERS = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    CART = (By.ID, "nav-cart-count")
    FASHION = (By.CSS_SELECTOR, "[data-csa-c-content-id='nav_cs_fashion']")

    def open_main(self):
        self.open_url()

    def click_on_orders(self):
        self.click(*self.RETURNS_ORDERS)

    def click_on_cart(self):
        self.click(*self.CART)

    def click_on_fashion(self):
        self.click(*self.FASHION)

    def click_sign_in_popup(self):
        self.wait_for_element_and_click(*self.SIGN_IN)

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def verify_signin_popup_clickable(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN), message='Sign in pop up button not clickable')

    def wait_sec(self, sec):
        sleep(int(sec))

    def signin_popup_disappear(self):
        self.wait_for_element_disappear(*self.SIGN_IN)

    def select_department(self, value):
        select = Select(self.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value(f"search-alias={value}")
