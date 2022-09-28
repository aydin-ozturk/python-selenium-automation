from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Select a product')
def select_product(context):
    context.driver.find_element(By.XPATH,"//*[contains(text(), 'Fits 95% of Vehicles - 1 Piece, Black')]").click()