import time
import math
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from params import my_login, my_password

# link = "https://stepik.org/lesson/236895/step/1/"


def answer():
    return math.log(int(time.time()))


source_list = ['https://stepik.org/lesson/236895/step/1',
               'https://stepik.org/lesson/236896/step/1',
               'https://stepik.org/lesson/236897/step/1',
               'https://stepik.org/lesson/236898/step/1',
               'https://stepik.org/lesson/236899/step/1',
               'https://stepik.org/lesson/236903/step/1',
               'https://stepik.org/lesson/236904/step/1',
               'https://stepik.org/lesson/236905/step/1'
               ]


@pytest.fixture(autouse=True)
def to_login(browser, sources):
    browser.get(sources)
    login_button = WebDriverWait(browser, timeout=16).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, 'a.navbar__auth_login'))
    )
    login_button.click()
    email = WebDriverWait(browser, timeout=16).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '#id_login_email'))
    )
    email.send_keys(my_login)
    password = WebDriverWait(browser, timeout=16).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '#id_login_password'))
    )
    password.send_keys(my_password)
    submit_login_button = WebDriverWait(browser, timeout=16).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '.sign-form__btn'))
    )
    submit_login_button.click()
    window = WebDriverWait(browser, timeout=16).until(
        ec.invisibility_of_element_located((By.CSS_SELECTOR, 'div.box'))
    )
    yield
    clean_result = WebDriverWait(browser, timeout=16).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, 'button.again-btn.white'))
    )
    clean_result.click()


@pytest.mark.parametrize('sources', source_list)
class TestLoginPage:
    def test_guest_should_login(self, browser):
        input_answer = WebDriverWait(browser, timeout=16).until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea'))
        )
        result = answer()
        input_answer.send_keys(result)
        send_answer = WebDriverWait(browser, timeout=16).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))
        )
        send_answer.click()
        actual = WebDriverWait(browser, timeout=16).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint'))
        )
        expected = 'Correct!'
        if actual.text != expected:
            with open('result.txt', 'a') as fout:
                fout.write(actual.text)
        assert actual.text == expected, f'AssertionError. Feedback text is incorrect: {actual.text}'
