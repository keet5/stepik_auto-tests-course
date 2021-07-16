from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()

    def scrollToView(element):
        browser.execute_script(
            "return arguments[0].scrollIntoView(true);", element)

    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    scrollToView(robot_checkbox)
    robot_checkbox.click()

    robot_radio = browser.find_element_by_css_selector(
        '#robotsRule[value="robots"]')
    scrollToView(robot_checkbox)
    robot_radio.click()

    answer = browser.find_element_by_id('answer')
    scrollToView(answer)
    answer.send_keys(y)

    submit = browser.find_element_by_tag_name('button')
    scrollToView(submit)
    submit.click()

except NoSuchElementException:
    print('No Such Element Exception')

finally:
    time.sleep(10)
    browser.quit()
