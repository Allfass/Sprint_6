from pages.order_page import OrderPage
import pytest
import allure 

@pytest.mark.usefixtures("driver")
class TestOrderPage():
    @allure.title('Проверка создания заказа на самокат')
    @allure.description('Заполняем поля заказа валидными значениями(по длине и алфавиту), в конце проверяем наличие строки оформлении заказа')
    @pytest.mark.parametrize("name,surname,city,metro,phone",
                        [('Андрей', "Петрович", "Краснодар", 1, "13212321323"),
                        ('вафывафывафываф', "аи","ааааафывафывафвафвыафвыафвыафвыафывафвыафвыафвыаф", 2, "1321232132323")])
    def test_complete_order_page_return_order_id(self, name, surname, city, metro, phone):
        order_page = OrderPage(self.driver)
        order_page.wait_for_load_main_page()
        order_page.input_name(name)
        order_page.input_surname(surname)
        order_page.input_address(city)
        order_page.select_metro(metro)
        order_page.input_phone(phone)
        order_page.click_further_order_button()
        order_page.wait_for_load_second_order_page()
        order_page.click_date_input_button()
        order_page.click_next_day_button()
        order_page.click_rental_period_button()
        order_page.click_one_day_rental_period_button()
        order_page.click_black_pearls_color_button()
        order_page.click_order_button()
        order_page.click_accept_order_button()
        assert order_page.check_compete_order_message() is not None
