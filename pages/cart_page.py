from pages.base_page import Page
from selenium.webdriver.common.by import By


class Cart(Page):
    CART = (By.ID, "nav-cart-count")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")

    def verify_cart_empty(self):
        self.verify_element_text("Your Amazon Cart is empty", *self.EMPTY_CART_MSG)

    def verify_cart_count(self, expected_count):
        self.verify_element_text(expected_count, *self.CART)

    def verify_product_name(self):
        product_name = self.find_element(*self.PRODUCT_NAME).text
        self.verify_partial_text(product_name[:30], *self.PRODUCT_NAME)
