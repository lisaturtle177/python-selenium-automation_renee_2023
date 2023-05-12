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

# open the url
driver.get('https://www.amazon.com/')

#amazon logo - CSS selector using class
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

#create account - CSS selector using class
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#I know I can just use by id but want to practice with css selectors more...
#name - CSS selector using id
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#email - CSS selector using Id - with tag
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

#pw - CSS selector using ID
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#re-enter pw -CSS selector using id
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#create your account button- called continue on my screen - CSS selector using id with tag
driver.find_element(By.CSS_SELECTOR, 'input#continue')

#conditions of use - css selector - parent - child
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='condition']")

#privacy Notice
driver.find_element(By.CSS_SELECTOR,"div.a-section.a-spacing-extra-large a[href*='privacy']")

#already... sign in
driver.find_element(By.CSS_SELECTOR,"a.a-link-emphasis[href*='signin']")