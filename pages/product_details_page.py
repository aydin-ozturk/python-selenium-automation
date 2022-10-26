from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductDetailsPage(Page):
    PRODUCT_NAME = (By.ID, "productTitle")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")

    def store_product_name(self):
        self.product_name = self.find_element(*self.PRODUCT_NAME).text
        print(f'\nCurrent product: {self.product_name}')

    def add_product(self):
        self.click(*self.ADD_TO_CART_BTN)
