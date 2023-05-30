from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, 'img.imgSwatch')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

@then('Verify user can click through colors')
def verify_click_colors(context):
    expected_colors=['Army Green', 'Black', 'Brown', 'Burgundy', 'Caramel']
    actual_colors=[]
#is there a way to reuse this step but do the expected colors as a variable array
    #so I can verify these too
    #['Black-2205', 'Black-2206', 'Bluegrey-2205', 'Darkpurple-2205', 'Deepcamel-2205']
    #since the second test fails

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors +=[current_color]

    assert expected_colors == actual_colors, \
    f'Expected colors {expected_colors} did not match actual {actual_colors}'