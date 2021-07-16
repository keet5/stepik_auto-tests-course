from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element_by_id('book')
    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button.click()
    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    button = browser.find_element_by_id('solve')
    button.click()

finally:
    time.sleep(1000)
    browser.quit()