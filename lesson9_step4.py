import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x: str):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button.click()
    time.sleep(5)
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    x = x_element.text
    result = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    input1.send_keys(result)
    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
