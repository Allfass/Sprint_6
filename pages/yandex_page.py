from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class YandexPage():
    def __init__(self, driver) -> None:
        self.main_url = 'https://yandex.ru/'
        self.driver = driver
        self.search_form = [By.XPATH, "//form[@action='https://yandex.ru/search/']"]

    def load_page(self):
        self.driver.get(self.main_url)

    def swith_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.search_form))

    def check_search_form(self):
        return self.driver.find_element(*self.search_form)
