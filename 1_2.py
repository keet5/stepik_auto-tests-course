from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    a = int(browser.find_element_by_id('num1').text)
    b = int(browser.find_element_by_id('num2').text)

    sum = a + b

    dropdown = Select(browser.find_element_by_id('dropdown'))
    dropdown.select_by_value(str(sum))

    submit = browser.find_element_by_tag_name('button')

finally:
    time.sleep(10)
    browser.quit()
