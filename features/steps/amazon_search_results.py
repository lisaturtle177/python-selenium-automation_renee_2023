from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS = (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
#xpath for all "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]"
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2')
PRODUCT_IMG = (By.CSS_SELECTOR, 'a.a-link-normal.s-no-outline')

@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got {actual_result}'

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(all_products)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Title should not be blank'
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Image not found'