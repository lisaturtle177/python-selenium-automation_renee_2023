from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.ID, 'nav-cart-count')
EMPTY_CART = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
SEARCH_RESULT = (By.CSS_SELECTOR, 'span.a-size-base-plus.a-color-base.a-text-normal')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
SUBTOTAL = (By.ID, 'sc-subtotal-label-buybox')

@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify cart is empty')
def verify_empty_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(*EMPTY_CART).text
    assert expected_result == actual_result, f'Error, Expected {expected_result}, but found {actual_result}'

@when('User adds item to cart')
def add_item_to_cart(context):
    context.driver.find_element(*SEARCH_FIELD).send_keys('stuffed monkey')
    context.driver.find_element(*SEARCH_BTN).click()
    context.driver.find_element(*SEARCH_RESULT).click()
    context.driver.find_element(*ADD_TO_CART).click()

@then('Verify item is in cart')
def verify_item_in_cart(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(*SUBTOTAL).text
    assert expected_result == actual_result, f'Error, Expected {expected_result}, but found {actual_result}'