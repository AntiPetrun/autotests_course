import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys("Petrov")
    mail = browser.find_element(By.NAME, 'email')
    mail.send_keys("example@gmail.com")
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_path, 'file.txt')
    file = browser.find_element(By.CSS_SELECTOR, 'input#file')
    file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
# print(current_dir)
# print(os.path.abspath(__file__))
# print(file_path)
