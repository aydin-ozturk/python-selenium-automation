from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ProductDetailsPage(Page):
    product_name = None
    PRODUCT_NAME = (By.ID, "productTitle")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    COLOR_OPTIONS = (By.XPATH, "//div[@id='variation_color_name']//li")
    CURRENT_COLOR = (By.XPATH, "//div[@id='variation_color_name']//*[@class='selection']")
    NEW_ARRIVALS = (By.CSS_SELECTOR, '[aria-label="New Arrivals"')
    WOMEN_DEALS = (By.CSS_SELECTOR, "a[href*='fashion-women'] h3")

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

    def hover_over_new_arrivals(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(*self.NEW_ARRIVALS))
        actions.perform()

    def verify_women_deals_present(self):
        self.verify_element_text("Women",*self.WOMEN_DEALS)
