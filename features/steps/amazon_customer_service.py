from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

MENU_CARD = (By.CSS_SELECTOR, 'div .issue-card-container .fs-match-card[role="button"]')

@given('Open amazon customer service page')
def open_amazon_customer_service(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


##Start here
@then('Verify {expected_options} menu options')
def verify_menu_options(context, expected_options):
    expected_options = int(expected_options)
    options_count = len(context.driver.find_elements(*MENU_CARD))
    assert options_count == expected_options, f'Expected {expected_options} links, but got {options_count}'

