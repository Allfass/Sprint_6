from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage(OrderPageLocators):
    def __init__(self, driver) -> None:
        self.main_url = 'https://qa-scooter.praktikum-services.ru/order'
        self.driver = driver
        self.driver.get(self.main_url)

    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.name_input))

    def input_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def input_surname(self, surname):
        self.driver.find_element(*self.surname_input).send_keys(surname)

    def input_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    def input_phone(self, phone):
        self.driver.find_element(*self.phone_input).send_keys(phone)

    def select_metro(self, metro_number_in_order):
        self.driver.find_element(*self.metro_input).click()
        self.driver.find_element(*self.select_metro_subinput(metro_number_in_order)).click()

    def click_further_order_button(self):
        element = self.driver.find_element(*self.further_button).click()

    def wait_for_load_second_order_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.date_input))

    def check_complete_first_step_of_order(self):
        return self.driver.find_element(*self.date_input)
    
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
        self.driver.find_element(*self.rental_period_input).click()

    def click_one_day_rental_period_button(self):
        element = self.driver.find_element(*self.rental_period_dropdown_day)
        self.driver.execute_script("arguments[0].click();", element)

    def click_two_days_rental_period_button(self):
        element = self.driver.find_element(*self.rental_period_dropdown_two_days)
        self.driver.execute_script("arguments[0].click();", element)
        
    def click_three_day_rental_period_button(self):
        element = self.driver.find_element(*self.rental_period_dropdown_three_day)
        self.driver.execute_script("arguments[0].click();", element)

    def click_black_pearls_color_button(self):
        element = self.driver.find_element(*self.checkbox_black_pearls)
        self.driver.execute_script("arguments[0].click();", element)

    def click_gray_despair_color_button(self):
        element = self.driver.find_element(*self.checkbox_gray_despair)
        self.driver.execute_script("arguments[0].click();", element)

    def click_order_button(self):
        element = self.driver.find_element(*self.order_button)
        self.driver.execute_script("arguments[0].click();", element)

    def click_accept_order_button(self):
        element = self.driver.find_element(*self.accept_order_button)
        self.driver.execute_script("arguments[0].click();", element)

    def click_decline_order_button(self):
        element = self.driver.find_element(*self.decline_order_button)
        self.driver.execute_script("arguments[0].click();", element)
        
    def check_compete_order_message(self):
        return self.driver.find_element(*self.compete_order_message)
