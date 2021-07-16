from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import math
import os


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    text_fields = browser.find_elements_by_css_selector('input[type="text"]')

    values = ['Name', 'Last name', 'Email']

    for field, value in zip(text_fields, values):
        field.send_keys(value)

    file_field = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file_field.send_keys(file_path)

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
