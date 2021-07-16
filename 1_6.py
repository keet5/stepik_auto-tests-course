from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    def button_click():
        button = browser.find_element_by_tag_name('button')
        button.click()

    button_click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    button_click()


finally:
    time.sleep(10)
    browser.quit()
