from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    CART = (By.ID, "nav-cart-count")
    RETURNS_ORDERS = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")

    def open_main(self):
        self.open_url()

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click_on_orders(self):
        self.driver.find_element(*self.RETURNS_ORDERS).click()

    def click_on_cart(self):
        self.wait_for_element_click(*self.CART)