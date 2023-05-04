from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'nav-orders').click()

expected_result_h1 = 'Sign in'
actual_result_h1 = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert expected_result_h1 == actual_result_h1, f'Error! Expected {expected_result_h1} but got {actual_result_h1}'

#should this go at the end - 1 for each?
print('Test case passed!')

#was not sure how to do this assertion so I asked ChatGPT
field = driver.find_element(By.ID, 'ap_email')

assert field.is_displayed()
#I wanted to do an error message here but the style above didn't seem to work, curious how to do that?


driver.quit()

