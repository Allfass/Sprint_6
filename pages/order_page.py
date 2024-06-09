from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MainPage(OrderPageLocators):
    def __init__(self, driver) -> None:
        self.main_url = 'https://qa-scooter.praktikum-services.ru/order'
        self.driver = driver
        self.driver.get(self.main_url)

    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.name_input))

    def input_name(self, name):
        self.driver.find_element(*self.input_name).send_keys(name)

    def select_metro(self, metro_number_in_order):
        element = self.driver.find_element(*self.metro_input)
        self.driver.execute_script("arguments[0].click();", element)
        element = self.driver.find_element(*self.select_metro_subinput(metro_number_in_order))
        self.driver.execute_script("arguments[0].click();", element)

    def click_further_order_button(self):
        element = self.driver.find_element(*self.further_button)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.date_input))
    
    def click_date_input_button(self):
        element = self.driver.find_element(*self.date_input)
        self.driver.execute_script("arguments[0].click();", element)

    def click_previous_day_button(self):
        element = self.driver.find_element(*self.get_previous_day())
        self.driver.execute_script("arguments[0].click();", element)

    def click_next_day_button(self):
        element = self.driver.find_element(*self.get_next_day())
        self.driver.execute_script("arguments[0].click();", element)

    def click_rental_period_button(self):
        element = self.driver.find_element(*self.rental_period_input)
        self.driver.execute_script("arguments[0].click();", element)

    def click_one_day_rental_period_button(self):
        element = self.driver.find_element(*self.rental_period_dropdown_day)
        self.driver.execute_script("arguments[0].click();", element)

    def click_two_days_rental_period_button(self):
        element = self.driver.find_element(*self.rental_period_dropdown_two_days)
        self.driver.execute_script("arguments[0].click();", element)
        
    def click_three_day_rental_period_button(self):
        element = self.driver.find_element(*self.rental_period_dropdown_three_day)
        self.driver.execute_script("arguments[0].click();", element)

    
