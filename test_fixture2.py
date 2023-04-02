import pytest

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.parametrize('language', ['en-gb', 'ru'])
class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    # @pytest.mark.parametrize('language', ['en-gb', 'ru'])
    # @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser, language):
        browser.get(link + language)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    # @pytest.mark.regression
    # @pytest.mark.skip
    def test_guest_should_see_basket_link_on_the_main_page(self, browser, language):
        browser.get(link + language)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    # @pytest.mark.xfail(reason="fixing this bug right now")
    # @pytest.mark.skip
    def test_guest_should_see_search_button_on_the_main_page(self, browser, language):
        browser.get(link + language)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")
