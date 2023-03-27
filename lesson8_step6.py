from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/execute_script.html'


def calc(x: str):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    browser.execute_script("return arguments[0].scrollIntoView(true);", y_element)
    y_element.send_keys(y)
    not_robot = browser.find_element(By.ID, 'robotCheckbox')
    not_robot.click()
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
