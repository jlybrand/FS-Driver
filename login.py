from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()
URL = os.getenv('LOGIN_URL')
PAGE_TITLE = os.getenv('LOGIN_TITLE')
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Open login page and enter username
# Wait for password page to open and enter password
try:
    driver = webdriver.Chrome(options=chrome_options)
    # TODO rename $cdc_  variable in chromedrive.exe 
    driver.get(URL)

    # Wait for the page to load and ensure the title is correct
    WebDriverWait(driver, 10).until(EC.title_is(PAGE_TITLE))

    username_field = driver.find_element_by_id("fsAdminLoginUsername")
    username_field.send_keys(USERNAME)

    # Wait for a few seconds to let the page load
    time.sleep(10)

    password_field = driver.find_element_by_id("fsAdminLoginPassword")
    password_field.send_keys(PASSWORD)

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for a few seconds to let the page load
    time.sleep(10)

    # Check if login was successful

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    time.sleep(30)
    driver.quit()


