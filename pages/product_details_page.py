from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductDetailsPage(Page):
    PRODUCT_NAME = (By.ID, "productTitle")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    COLOR_OPTIONS = (By.XPATH, "//div[@id='variation_color_name']//li")
    CURRENT_COLOR = (By.XPATH, "//div[@id='variation_color_name']//*[@class='selection']")

    def store_product_name(self):
        self.product_name = self.find_element(*self.PRODUCT_NAME).text
        print(f'\nCurrent product: {self.product_name}')

    def add_product(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_can_click_colors(self):
        expected_colors = ['Army Green', 'Black', 'Blue']
        actual_colors = []
        colors = self.driver.find_elements(*self.COLOR_OPTIONS)
        for color in colors[:3]:
            color.click()
            current_color = self.driver.find_element(*self.CURRENT_COLOR).text
            actual_colors += [current_color]
        print("Actual colors:", actual_colors)
        assert expected_colors == actual_colors, \
            f'Expected colors {expected_colors} did not match actual {actual_colors}'