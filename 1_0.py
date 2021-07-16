from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()

    browser.get(link)
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute('value')
    print(type(x))

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    # if not robot_checkbox.is_selected:
    robot_checkbox.click()

    robot_radio = browser.find_element_by_css_selector(
        '#robotsRule[value="robots"]')
    robot_radio.click()

    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    submit = browser.find_element_by_tag_name('button')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
