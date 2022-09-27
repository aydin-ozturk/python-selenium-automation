from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.com")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

expected_header = "Sign in"
actual_header = driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in')]").text
assert expected_header == actual_header, f'Expected {expected_header} but got {actual_header}'

assert driver.find_element(By.ID, "ap_email"), 'Email field not shown'

print("Test case passed")

driver.quit()
