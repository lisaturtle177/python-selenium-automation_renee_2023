from selenium.webdriver.common.by import By
from behave import given, when, then
import time
from time import sleep


#BEST_SELLERS_LINKS = (By.CSS_SELECTOR, "zg_header a") - doesn't work somehow, even though it should??
BEST_SELLERS_LINKS = (By.XPATH, "//a[contains(@href, 'ref=zg_bs_tab')]")

#I am repeating the footer step from the class,
#How can I resure the one from the footer exercise and just change
#the variable passed here: links_count = len(context.driver.find_elements(*LINKS))

@then('Verify {expected_links} Best Sellers links')
def best_sellers_links(context, expected_links):
    expected_links = int(expected_links)
    print(type(expected_links)) #troubleshooting cuz other locator issue
    count_links = len(context.driver.find_elements(*BEST_SELLERS_LINKS))
    assert count_links == expected_links, f'Expected {expected_links} links, but got {count_links}'


