from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import math

with open('./script.js') as f:
    script = f.read()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_id('input_value')
    y = calc(x)

    # dropdown = Select(browser.find_element_by_id('dropdown'))
    # dropdown.select_by_value(str(sum))

    # submit = browser.find_element_by_tag_name('button')
finally:
    time.sleep(10)
    browser.quit()
