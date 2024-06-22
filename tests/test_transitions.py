from pages.main_page import MainPage
from tests.constants import TestConstants
from pages.yandex_page import YandexPage
import pytest
import allure 

@pytest.mark.usefixtures("driver")
class TestTransitions():
    @allure.title('Проверка перехода на главную страницу')
    @allure.description('При нажатии на иконку самоката, можно будет найти на странице один из вопросов')
    def test_transition_to_main_page(self):
        main_page = MainPage(self.driver, TestConstants.main_url)
        main_page.load_page()
        main_page.wait_for_load_main_page()
        main_page.click_on_main_page_link()
        assert main_page.check_main_page_load() is not None

    @allure.title('Проверка перехода на страницу yandex')
    @allure.description('При нажатии на иконку yandex, откроется новая вкладка, на которой можно найти форму для запроса')
    def test_transition_to_yandex_page(self):
        main_page = MainPage(self.driver, TestConstants.main_url)
        main_page.load_page()
        main_page.wait_for_load_main_page()
        main_page.click_on_yandex_page_link()
        yandex_page = YandexPage(self.driver)
        yandex_page.swith_to_new_tab()
        yandex_page.wait_for_load_page()
        assert yandex_page.check_search_form() is not None