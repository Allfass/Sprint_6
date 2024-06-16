from locators.order_page_locators import OrderPageLocators
from locators.helper import OrderPageHelper
from pages.page import Page
import allure

class OrderPage(Page):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.order_page_locators = OrderPageLocators()

    @allure.step('Ждём загрузки страницы')
    def wait_for_load_main_page(self):
        super().wait_for_load_page(self.order_page_locators.name_input)

    @allure.step('Выбираем одну из станций метро')
    def select_metro(self, metro_number_in_order):
        super().click_on_element(OrderPageLocators.metro_input)
        super().click_on_element(OrderPageLocators.metro_input)
        metro_number = OrderPageHelper.select_metro_subinput(metro_number_in_order)
        metro_locator = OrderPageLocators.metro_subinput_template[1].replace("???", metro_number)
        super().click_on_element(metro_locator)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_further_order_button(self):
        super().click_on_element_with_javascript(self.further_button)

    @allure.step('Ждём загрузки страницы')
    def wait_for_load_second_order_page(self):
        super().wait_for_load_page(self.date_input)

    @allure.step('Кликаем на поле с датой')
    def click_date_input_button(self):
        super().click_on_element_with_javascript(self.date_input)

    @allure.step('В поле даты выбираем предыдущую')
    def click_previous_day_button(self):
        super().click_on_element_with_javascript(self.date_input)
        previous_day = OrderPageHelper.get_previous_day()
        date_locator = OrderPageLocators.previous_day_template[1].replace("???", previous_day)
        super().click_on_element_with_javascript(date_locator)

    @allure.step('В поле даты выбираем следующую')
    def click_next_day_button(self):
        super().click_on_element_with_javascript(self.date_input)
        next_day = OrderPageHelper.get_next_day()
        date_locator = OrderPageLocators.next_day_template[1].replace("???", next_day)
        super().click_on_element_with_javascript(date_locator)

    @allure.step('Кликаем на поле доставки')
    def click_rental_period_button(self):
        super().click_on_element(self.rental_period_input)

    @allure.step('Кликаем на аренда самоката на один день')
    def click_one_day_rental_period_button(self):
        super().click_on_element_with_javascript(self.rental_period_dropdown_day)

    @allure.step('Кликаем на аренда самоката на два дня')
    def click_two_days_rental_period_button(self):
        super().click_on_element_with_javascript(self.rental_period_dropdown_two_days)

    @allure.step('Кликаем на аренда самоката на три дня')
    def click_three_day_rental_period_button(self):
        super().click_on_element_with_javascript(self.rental_period_dropdown_three_day)

    @allure.step('Выбираем чекбокс "черный жемчуг"')
    def click_black_pearls_color_button(self):
        super().click_on_element_with_javascript(self.checkbox_black_pearls)

    @allure.step('Выбираем чекбокс "серая безысходность"')
    def click_gray_despair_color_button(self):
        super().click_on_element_with_javascript(self.checkbox_gray_despair)

    @allure.step('Кликаем кнопку заказа')
    def click_order_button(self):
        super().click_on_element_with_javascript(self.order_button)

    @allure.step('Кликаем подтвердить заказ')
    def click_accept_order_button(self):
        super().click_on_element_with_javascript(self.accept_order_button)

    @allure.step('Кликаем отменить заказ')
    def click_decline_order_button(self):
        super().click_on_element_with_javascript(self.decline_order_button)

    @allure.step('Проверяем отображения поля статуса заказа')
    def check_compete_order_message(self):
        return super().check_page_load(self.compete_order_message)
