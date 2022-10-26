from pages.bestsellers_page import BestsellersPage
from pages.cart_page import Cart
from pages.main_page import MainPage
from pages.product_details_page import ProductDetailsPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.bestsellers_page=BestsellersPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page=SearchResultsPage(self.driver)
        self.sign_in_page=SignInPage(self.driver)
        self.cart_page=Cart(self.driver)
        self.product_details_page=ProductDetailsPage(self.driver)

