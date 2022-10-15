from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN=(By.ID, "add-to-cart-button")
PRODUCT_NAME=(By.ID, "productTitle")
COLOR_OPTIONS=(By.XPATH,"//div[@id='variation_color_name']//li")
CURRENT_COLOR=(By.XPATH,"//div[@id='variation_color_name']//*[@class='selection']")
@given('Open amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@when('Add the product to the cart')
def add_product(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@when('Store product name')
def store_product_name(context):
    context.product_name=context.driver.find_element(*PRODUCT_NAME).text
    print(f'\nCurrent product: {context.product_name}')


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors=['Army Green', 'Black', 'Blue']

    actual_colors=[]

    colors= context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors[:3]:
        color.click()
        current_color=context.driver.find_element(*CURRENT_COLOR).text
        actual_colors+=[current_color]
    print("Actual colors:", actual_colors)

    assert expected_colors==actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'

































