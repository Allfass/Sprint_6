from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from tests.constants import TestConstants
import pytest
import allure 

@pytest.mark.usefixtures("driver")
class TestMainPage():
    @allure.title('Проверка отображения вопросов при нажатии на него')
    @allure.description('При нажатии на вопрос, у локатора будет отсуствовать атрибут hidden')
    @pytest.mark.parametrize("question,answer",[
        (MainPageLocators.first_question, MainPageLocators.first_answer),
        (MainPageLocators.second_question, MainPageLocators.second_answer),
        (MainPageLocators.third_question, MainPageLocators.third_answer),
        (MainPageLocators.fourth_question, MainPageLocators.fourth_answer),
        (MainPageLocators.fifth_question, MainPageLocators.fifth_answer),
        (MainPageLocators.sixth_question, MainPageLocators.sixth_answer),
        (MainPageLocators.seventh_question, MainPageLocators.seventh_answer),
        (MainPageLocators.eighth_question, MainPageLocators.eighth_answer),
        ])
    def test_answers_on_main_page_are_visiable_after_click(self, question, answer):
        main_page = MainPage(self.driver, TestConstants.main_url)
        main_page.load_page()
        main_page.wait_for_load_main_page()
        main_page.click_on_element(question)
        assert main_page.check_is_answer_hidden(answer) is None
