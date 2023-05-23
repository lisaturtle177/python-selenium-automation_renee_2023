from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
BEST_SELLERS = (By.CSS_SELECTOR, '#nav-xshop > a[href*="bestsellers"]')

@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()

@when('Click on Orders and Returns')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()

@when('User click on Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()

@then('Verify there are {expected_amount} links')
def verify_footer_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links_count = len(context.driver.find_elements(*FOOTER_LINKS)) #36
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'

