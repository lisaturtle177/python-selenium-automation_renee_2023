from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#how can I call the 'open anazon main page' from another step file'
@given('Go to amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Click on Orders and Returns')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify sign in page opens')
def verify_signin_page_opens(context):
    expected_result_h1 = 'Sign in'
    actual_result_h1 = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result_h1 == actual_result_h1, f'Error! Expected {expected_result_h1} but got {actual_result_h1}'
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()


@then('Verify cart is empty')
def verify_empty_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Error, Expected {expected_result}, but found {actual_result}'

@when('User adds item to cart')
def add_item_to_cart(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.driver.find_element(By.CSS_SELECTOR, 'img.s-image').click()
    context.driver.find_element(By.ID, 'add-to-cart-button').click()

@then('Verify item is in cart')
def verify_item_in_cart(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(By.ID, 'sc-subtotal-label-buybox').text
    assert expected_result == actual_result, f'Error, Expected {expected_result}, but found {actual_result}'