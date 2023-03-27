from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x: str):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, 'img#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    y_element = browser.find_element(By.CSS_SELECTOR, 'input#answer')
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
