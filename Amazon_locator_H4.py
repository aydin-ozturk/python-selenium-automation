from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

# assert driver.find_element(By.XPATH, "//h1[@class='fs-heading bolded']").text, f'Welcome header not shown'
# assert driver.find_element(By.CSS_SELECTOR, '.fs-heading'), f'Welcome header not shown'

# assert driver.find_element(By.CSS_SELECTOR, ".issue-card-container"), f"Options block not shown"
# assert driver.find_element(By.XPATH, "//*[@class='issue-card-container']"), f"Options block not shown"

# assert driver.find_element(By.XPATH, "//label/h2[@class='fs-heading bolded']"), f'"Search our help library" not shown'
# assert driver.find_element(By.CSS_SELECTOR, 'div[class="page-container"] label h2[class="fs-heading bolded"]'), f'"Search our library" not shown'

# assert driver.find_element(By.CSS_SELECTOR, "#hubHelpSearchInput"), f'Library search bar not shown'
# assert driver.find_element(By.ID, "hubHelpSearchInput"), f'Library search bar not shown'

# assert driver.find_element(By.XPATH,//div[@class='page-container']/h2[@class='fs-heading bolded']), f'"All help topics" not shown'
########

# assert driver.find_element(By.XPATH, "//*[@class='help-topics-list-wrapper']"),f'"Recommended topics" block not shown'
# assert driver.find_element(By.CSS_SELECTOR, '.help-topics-list-wrapper'), f'"Recommended topics" block not shown'


driver.quit()
