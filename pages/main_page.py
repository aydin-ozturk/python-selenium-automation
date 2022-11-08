from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from time import sleep


class MainPage(Page):
    CART = (By.ID, "nav-cart-count")
    DEPARTMENT_SELECTION = (By.ID, "searchDropdownBox")
    FASHION = (By.CSS_SELECTOR, "[data-csa-c-content-id='nav_cs_fashion']")
    LANGUAGE_SELECTION = (By.ID, "icp-nav-flyout")
    RETURNS_ORDERS = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SIGN_IN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-button")
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href*="lang=es"]')

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

    def hover_over_language(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.LANGUAGE_SELECTION))
        actions.perform()

    def verify_spanish_language_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)
