from pages.order_page import OrderPage
import pytest

@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("name,surname,city,metro,phone",
                        [('Андрей', "Петрович", "Краснодар", 1, "13212321323"),
                        ('вафывафывафываф', "аи","ааааафывафывафвафвыафвыафвыафвыафывафвыафвыафвыаф", 2, "1321232132323")])
class TestOrderPage():

    def test_create_order_on_order_page_return_compete_order_message(self, name, surname, city, metro, phone):
        order_page = OrderPage(self.driver)
        order_page.wait_for_load_main_page()
        order_page.input_name(name)
        order_page.input_surname(surname)
        order_page.input_address(city)
        order_page.select_metro(metro)
        order_page.phone_input(phone)
        order_page.click_further_order_button()
        assert order_page.check_compete_first_step_of_order() is not None