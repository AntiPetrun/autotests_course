from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'


def calc(x, y):
    return str(x + y)


# variant 1
browser = webdriver.Chrome()
browser.get(link)

# browser.find_element(By.TAG_NAME, "select").click()
# browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
# browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

# variant 2
try:
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#num1.nowrap')
    x = int(x_element.text)
    y_element = browser.find_element(By.CSS_SELECTOR, 'span#num2.nowrap')
    y = int(y_element.text)
    summa = calc(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    print(summa)
    select.select_by_value(summa)  # ищем элемент с текстом "Python"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
