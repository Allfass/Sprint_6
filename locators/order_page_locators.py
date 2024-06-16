from selenium.webdriver.common.by import By

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
    previous_day_template = [By.XPATH, "//div[contains(text(),???) and contains(@class,'react-datepicker__day--0???')]"]
    next_day_template = [By.XPATH, "//div[contains(text(),???) and contains(@class,'react-datepicker__day--0???')]"]
    metro_subinput_template = [By.XPATH, "//button[@value=???]"]
