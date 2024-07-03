from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import pickle

with open('fs-driver/assets/subdivisions.py', 'rb') as file:
    subdivisions = pickle.load(file)

load_dotenv()
URL = os.getenv('URL')
PAGE_TITLE = os.getenv('PAGE_TITLE')

def string_to_set(str):
    return set(item.strip() for item in str.split(','))

def sets_are_equal(set1, set2):
    return set1 == set2

try:
    driver = webdriver.Chrome()
    driver.get(URL)

    # Wait for the page to load and ensure the title is correct
    WebDriverWait(driver, 10).until(EC.title_is(PAGE_TITLE))

    # Get all <a> tags with a title attribute
    a_tags = driver.find_elements(By.CSS_SELECTOR, 'a[title]')

    # Iterate over each subdivision
    for key, values in subdivisions:
        key_set = set(key)
        matching_a_tag = None

        # Iterate over each <a> tag and find one with the matching title
        # Finds board with correlating high, middle, elementary and opens board
        for a_tag in a_tags:
            title_set = string_to_set(a_tag.get_attribute("title"))

            if sets_are_equal(title_set, key_set):
                matching_a_tag = a_tag
                break

        if matching_a_tag:
            print("Found matching <a> tag:",
                  matching_a_tag.get_attribute('title'))
            # matching_a_tag.click()
        else:
            print("No matching <a> tag found for:", key_set)

finally:
    time.sleep(30)
    driver.quit()
