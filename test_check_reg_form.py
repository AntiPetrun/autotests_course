import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestRegistration(unittest.TestCase):
    def test_reg_form1(self):
        browser = webdriver.Chrome()
        browser.get(link1)
        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
        first_name.send_keys('Zhora')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
        last_name.send_keys('Pompidu')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
        email.send_keys('example@gmail.com')
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-default'))
        )
        button.click()
        message = browser.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(message.text, 'Congratulations! You have successfully registered!', 'Test failed')
        browser.quit()

    def test_reg_form2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
        first_name.send_keys('Zhora')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
        last_name.send_keys('Pompidu')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
        email.send_keys('example@gmail.com')
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-default'))
        )
        button.click()
        message = browser.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(message.text, 'Congratulations! You have successfully registered!', 'Test failed')
        browser.quit()


if __name__ == '__main__':
    unittest.main()
