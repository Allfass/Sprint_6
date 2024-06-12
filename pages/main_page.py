from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MainPage(MainPageLocators):
    def __init__(self, driver) -> None:
        self.main_url = 'https://qa-scooter.praktikum-services.ru/'
        self.driver = driver
        self.driver.get(self.main_url)

    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.first_question))

    def check_main_page_load(self):
        return self.driver.find_element(*self.first_question)

    def click_on_first_question(self):
        element = self.driver.find_element(*self.first_question)
        self.driver.execute_script("arguments[0].click();", element)

    def check_first_answer_visiable(self):
        self.driver.find_element(*self.first_answer).get_attribute("hidden")

    def click_on_second_question(self):
        element = self.driver.find_element(*self.second_question)
        self.driver.execute_script("arguments[0].click();", element)

    def check_second_answer_visiable(self):
        self.driver.find_element(*self.second_question).get_attribute("hidden")

    def click_on_third_question(self):
        element = self.driver.find_element(*self.third_question)
        self.driver.execute_script("arguments[0].click();", element)

    def check_third_answer_visiable(self):
        self.driver.find_element(*self.third_question).get_attribute("hidden")

    def click_on_fourth_question(self):
        element = self.driver.find_element(*self.fourth_question)
        self.driver.execute_script("arguments[0].click();", element)

    def check_fourth_answer_visiable(self):
        self.driver.find_element(*self.fourth_question).get_attribute("hidden")

    def click_on_fifth_question(self):
        element = self.driver.find_element(*self.fifth_question)
        self.driver.execute_script("arguments[0].click();", element)

    def check_fifth_answer_visiable(self):
        self.driver.find_element(*self.fifth_question).get_attribute("hidden")

    def click_on_sixth_question(self):
        element = self.driver.find_element(*self.sixth_question)
        self.driver.execute_script("arguments[0].click();", element)

    def check_sixth_answer_visiable(self):
        self.driver.find_element(*self.sixth_question).get_attribute("hidden")

    def click_on_seventh_question(self):
        element = self.driver.find_element(*self.seventh_question)
        self.driver.execute_script("arguments[0].click();", element)

    def check_seventh_answer_visiable(self):
        self.driver.find_element(*self.seventh_question).get_attribute("hidden")

    def click_on_eighth_question(self):
        element = self.driver.find_element(*self.eighth_question)
        self.driver.execute_script("arguments[0].click();", element)

    def check_eighth_answer_visiable(self):
        self.driver.find_element(*self.eighth_question).get_attribute("hidden")

    def click_on_main_page_link(self):
        self.driver.find_element(*self.main_page_link).click()

    def click_on_yandex_page_link(self):
        self.driver.find_element(*self.yandex_page_link).click()
    