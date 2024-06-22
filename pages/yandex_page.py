from selenium.webdriver.common.by import By
from pages.page import Page
from locators.yandex_page_locators import YandexPageLocators
import allure

class YandexPage(Page):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.yandex_locators = YandexPageLocators()

    @allure.step('Ждем загрузки страницы "яндекс-дзен"')
    def wait_for_load_main_page(self):
        super().wait_for_load_page(self.yandex_locators.search_form)

    @allure.step('Проверяем наличие на страницы формы поиска')
    def check_search_form(self):
        return self.check_page_load(self.yandex_locators.search_form)
