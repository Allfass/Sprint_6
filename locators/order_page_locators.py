from selenium.webdriver.common.by import By
import datetime

class OrderPageLocators():
    
    name_input = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname_input = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_input = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    phone_input = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    further_button = [By.XPATH, "//button[contains(text(), 'Далее')]"]
    date_input = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rental_period_input = [By.XPATH, "//div[contains(text(), '* Срок аренды')]"]
    rental_period_dropdown_day = [By.XPATH, "//div[contains(text(), 'сутки')]"]
    rental_period_dropdown_two_days = [By.XPATH, "//div[contains(text(), 'двое суток')]"]
    rental_period_dropdown_three_day = [By.XPATH, "//div[contains(text(), 'трое суток')]"]
    checkbox_black_pearls = [By.XPATH, "//input[@id='black']"]
    checkbox_gray_despair = [By.XPATH, "//input[@id='grey']"]
    order_button = [By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle__1CSJM')]"]
    accept_order_button = [By.XPATH, "//button[contains(text(), 'Да')]"]
    decline_order_button = [By.XPATH, "//button[contains(text(), 'Нет')]"]
    compete_order_message = [By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"]
    
    def get_previous_day(self):
        now = datetime.date.today()-datetime.timedelta(1)
        previous_day = now.day
        if 0 < now.day < 10:
            previous_day = f"0{str(now.day)}"
        else:
            previous_day = str(now.day)
        return [By.XPATH, f"//div[contains(text(),{previous_day}) and contains(@class,'react-datepicker__day--0{previous_day}')]"]

    def get_next_day(self):
        now = datetime.date.today()+datetime.timedelta(1)
        next_day = now.day
        if 0 < now.day < 10:
            next_day = f"0{str(now.day)}"
        else:
            next_day = str(now.day)
        return [By.XPATH, f"//div[contains(text(),{next_day}) and contains(@class,'react-datepicker__day--0{next_day}')]"]

    def select_metro_subinput(self, metro_number):
        if 0 < metro_number < 238:
            metro_subinput = [By.XPATH, f"//button[@value={metro_number}]"]
            return metro_subinput
        else:
            raise(RuntimeError(f'The passed value {metro_number} does not exist'))
        