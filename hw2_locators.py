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

# Amazon logo - by xpath
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Continue button - by ID
driver.find_element(By.ID, 'continue')

# Need help link - xpath
driver.find_element(By.XPATH, "//input[@name='metadata1']")

# Forgot your password link - by ID
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link - by ID
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button - by id / xpath
driver.find_element(By.ID, 'createAccountSubmit')
driver.find_element(By.XPATH, "//a[@class='a-button-text']")

# *Conditions of use link - xpath, contains and attribute
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions') and @class='a-link-normal']")

# *Privacy Notice link - xpath parent and child element
driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-small a-text-center a-size-mini']//a[contains(text(), 'Privacy')]")
