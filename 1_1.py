from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()

    browser.get(link)
    x_element = browser.find_element_by_id('input_value')

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    # if not robot_checkbox.is_selected:
    robot_checkbox.click()

    robot_radio = browser.find_element_by_css_selector(
        '#robotsRule[value="robots"]')
    robot_radio.click()

    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    submit = browser.find_element_by_tag_name('button')
    submit.click()

except NoSuchElementException:
    print('No Such Element Exception')

finally:
    time.sleep(10)
    browser.quit()
