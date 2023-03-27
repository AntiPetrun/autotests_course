import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x: str):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button#book.btn.btn-primary")

    price = WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), '100')
        )
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
    x = x_element.text
    result = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    input1.send_keys(result)
    submit = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#solve.btn.btn-primary'))
    )
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
