from pages.main_page import MainPage
import pytest

@pytest.mark.usefixtures("driver")
class TestMainPage():

    def test_first_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.wait_for_load_main_page()
        main_page.click_on_first_question()
        assert main_page.check_first_answer_visiable() is None

    def test_second_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_second_question()
        assert main_page.check_second_answer_visiable() is None

    def test_third_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_third_question()
        assert main_page.check_third_answer_visiable() is None

    def test_fourth_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_fourth_question()
        assert main_page.check_fourth_answer_visiable() is None

    def test_fifth_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_fifth_question()
        assert main_page.check_fifth_answer_visiable() is None

    def test_sixth_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_sixth_question()
        assert main_page.check_sixth_answer_visiable() is None

    def test_seventh_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_seventh_question()
        assert main_page.check_seventh_answer_visiable() is None

    def test_eighth_answer_on_main_page_are_visiable(self):
        main_page = MainPage(self.driver)
        main_page.click_on_eighth_question()
        assert main_page.check_eighth_answer_visiable() is None
