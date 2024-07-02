from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from dotenv import load_dotenv
import os

load_dotenv()
URL = os.getenv('URL')
PAGE_TITLE = os.getenv('PAGE_TITLE')

driver = webdriver.Chrome()

# Open page and test button click
driver.get(URL)

try:
    WebDriverWait(driver, 10).until(EC.title_is(PAGE_TITLE))
    button = driver.find_element(By.CLASS_NAME, 'ps-link')
    button.click()
finally:
    time.sleep(30)
    driver.quit()
