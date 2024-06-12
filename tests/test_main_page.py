from pages.main_page import MainPage
from pages.yandex_page import YandexPage
import pytest
import allure 

@pytest.mark.usefixtures("driver")
class TestMainPage():

    @allure.title('Проверка отображения первого вопроса при нажатии на него')
    @allure.description('При нажатии на вопрос, у локатора будет отсуствовать атрибут hidden')
    def test_first_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.wait_for_load_main_page()
        main_page.click_on_first_question()
        assert main_page.check_first_answer_visiable() is None

    @allure.title('Проверка отображения второго вопроса при нажатии на него')
    @allure.description('При нажатии на вопрос, у локатора будет отсуствовать атрибут hidden')
    def test_second_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_second_question()
        assert main_page.check_second_answer_visiable() is None

    @allure.title('Проверка отображения третьего вопроса при нажатии на него')
    @allure.description('При нажатии на вопрос, у локатора будет отсуствовать атрибут hidden')
    def test_third_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_third_question()
        assert main_page.check_third_answer_visiable() is None

    @allure.title('Проверка отображения четвертого вопроса при нажатии на него')
    @allure.description('При нажатии на вопрос, у локатора будет отсуствовать атрибут hidden')
    def test_fourth_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_fourth_question()
        assert main_page.check_fourth_answer_visiable() is None

    @allure.title('Проверка отображения пятого вопроса при нажатии на него')
    @allure.description('При нажатии на вопрос, у локатора будет отсуствовать атрибут hidden')
    def test_fifth_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_fifth_question()
        assert main_page.check_fifth_answer_visiable() is None

    @allure.title('Проверка отображения шестого вопроса при нажатии на него')
    @allure.description('При нажатии на вопрос, у локатора будет отсуствовать атрибут hidden')
    def test_sixth_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_sixth_question()
        assert main_page.check_sixth_answer_visiable() is None

    @allure.title('Проверка отображения седьмого вопроса при нажатии на него')
    @allure.description('При нажатии на вопрос, у локатора будет отсуствовать атрибут hidden')
    def test_seventh_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_seventh_question()
        assert main_page.check_seventh_answer_visiable() is None

    @allure.title('Проверка отображения восьмого вопроса при нажатии на него')
    @allure.description('При нажатии на вопрос, у локатора будет отсуствовать атрибут hidden')
    def test_eighth_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_eighth_question()
        assert main_page.check_eighth_answer_visiable() is None
    
    @allure.title('Проверка перехода на главную страницу')
    @allure.description('При нажатии на иконку самоката, можно будет найти на странице один из вопросов')
    def test_transition_to_main_page(self):
        main_page = MainPage(self.driver)
        main_page.click_on_main_page_link()
        assert main_page.check_main_page_load() is not None

    @allure.title('Проверка перехода на страницу yandex')
    @allure.description('При нажатии на иконку yandex, откроется новая вкладка, на которой можно найти форму для запроса')
    def test_transition_to_yandex_page(self):
        main_page = MainPage(self.driver)
        main_page.click_on_yandex_page_link()
        yandex_page = YandexPage(self.driver)
        yandex_page.swith_to_new_tab()
        yandex_page.wait_for_load_main_page()
        assert yandex_page.check_search_form() is not None
