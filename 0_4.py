from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

try:
    links = ["http://suninjuly.github.io/registration1.html",
             "http://suninjuly.github.io/registration2.html"]

    browser = webdriver.Chrome()

    for link in links:
        browser.get(link)

        first_name = browser.find_element_by_css_selector(
            '.first_block input.first')
        first_name.send_keys('Name')

        first_name = browser.find_element_by_css_selector(
            '.first_block input.second')
        first_name.send_keys('Last Name')

        first_name = browser.find_element_by_css_selector(
            '.first_block input.third')
        first_name.send_keys('email')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

except NoSuchElementException:
    print('No Such Element Exception')

finally:
    time.sleep(10)
    browser.quit()
