from locators.main_page_locators import MainPageLocators
from pages.page import Page
import allure

class MainPage(Page):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.main_page_locators = MainPageLocators()

    @allure.step('Ждём загрузки страницы')
    def wait_for_load_main_page(self):
        super().wait_for_load_page(self.main_page_locators.fifth_question)

    @allure.step('Проверяем загрузку элемента страницы')
    def check_main_page_load(self):
        return super().check_page_load(self.main_page_locators.first_question)
    
    @allure.step('Проверяем наличие атрибута "hidden" у элемента')
    def check_is_answer_hidden(self, answer_locator):
        return super().get_element_attribute(answer_locator, "hidden")

    @allure.step('Нажимаем на ссылка на главную страницу')
    def click_on_main_page_link(self):
        super().click_on_element_with_javascript(self.main_page_locators.main_page_link)

    @allure.step('Нажимаем на ссылка на страницу яндекс')  
    def click_on_yandex_page_link(self):
        super().click_on_element_with_javascript(self.main_page_locators.yandex_page_link)