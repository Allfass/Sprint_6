from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class YandexPage():
    def __init__(self, driver) -> None:
        self.main_url = 'https://yandex.ru/'
        self.driver = driver
        self.driver.get(self.main_url)
        self.search_form = [By.XPATH, "//form[@action='https://yandex.ru/search/']"]

    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.search_form))

    def check_search_form(self):
        self.driver.find_element(*self.search_form)