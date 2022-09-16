import allure
from selenium.webdriver.common.by import By


class OrderPage:

    first_name_field = [By.XPATH, "//input[@placeholder='* Имя']"]

    last_name_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]

    address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]

    metro_station_field = [By.XPATH, "//input[@placeholder='* Станция метро']"]

    metro_station_1 = [By.XPATH, "//input[@placeholder='* Станция метро']/parent::div/parent::div//li[1]"]

    metro_station_2 = [By.XPATH, "//input[@placeholder='* Станция метро']/parent::div/parent::div//li[25]"]

    phone_number_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

    next_button = [By.XPATH, "//button[text()='Далее']"]

    about_rent_header = [By.XPATH, "//div[text()='Про аренду']"]

    date_field = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

    day_in_the_calendar = [By.XPATH, "//div[@class='react-datepicker__month']//div[contains(text(),'15')]"]

    rent_time_field = [By.XPATH, "//div[text()='* Срок аренды']"]

    rent_time_dropdown_option_1 = [By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"]

    rent_time_dropdown_option_2 = [By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']"]

    rent_time_dropdown_option_3 = [By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"]

    rent_time_dropdown_option_4 = [By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']"]

    rent_time_dropdown_option_5 = [By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']"]

    rent_time_dropdown_option_6 = [By.XPATH, "//div[@class='Dropdown-option' and text()='шестеро суток']"]

    rent_time_dropdown_option_7 = [By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']"]

    checkbox_black = [By.ID, "black"]

    checkbox_grey = [By.ID, "grey"]

    comment_field = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    back_button = [By.XPATH, "//button[text()='Назад']"]

    order_button = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"]

    order_modal_window = [By.XPATH, "//div[contains(@class, 'Order_Modal')]"]

    no_button = [By.XPATH, "//button[text()='Нет']"]

    yes_button = [By.XPATH, "//button[text()='Да']"]

    successfully_order_header = [By.XPATH, "//div[text()='Заказ оформлен']"]

    check_status_button = [By.XPATH, "//button[text()='Посмотреть статус']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем главную страницу https://qa-scooter.praktikum-services.ru/')
    def open_page(self, page):
        self.driver.get(page)

    @allure.step('Заполняем поле "Имя"')
    def set_first_name(self, first_name):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_last_name(self, last_name):
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    @allure.step('Заполняем поле "Адрес"')
    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    @allure.step('Заполняем поле "Станция метро"')
    def set_metro_station_1(self):
        self.driver.find_element(*self.metro_station_field).click()
        self.driver.find_element(*self.metro_station_1).click()

    @allure.step('Заполняем поле "Станция метро"')
    def set_metro_station_2(self):
        self.driver.find_element(*self.metro_station_field).click()
        self.driver.find_element(*self.metro_station_2).click()

    @allure.step('Заполняем поле "Телефон"')
    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    @allure.step('Заполняем первую страницу формы')
    def fill_in_fields_on_the_first_order_form(self, first_name, last_name, address, phone_number):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro_station_1()
        self.set_phone_number(phone_number)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Заполняем дату вводом с клавиатуры')
    def set_date(self, date):
        self.driver.find_element(*self.date_field).send_keys(date)

    @allure.step('Заполняем дату выбором через календарь')
    def select_date(self):
        self.driver.find_element(*self.date_field).click()
        self.driver.find_element(*self.day_in_the_calendar).click()

    def unfocus(self):
        self.driver.find_element(*self.about_rent_header).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_1(self):
        self.driver.find_element(*self.rent_time_field).click()
        self.driver.find_element(*self.rent_time_dropdown_option_1).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_2(self):
        self.driver.find_element(*self.rent_time_field).click()
        self.driver.find_element(*self.rent_time_dropdown_option_2).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_3(self):
        self.driver.find_element(*self.rent_time_field).click()
        self.driver.find_element(*self.rent_time_dropdown_option_3).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_4(self):
        self.driver.find_element(*self.rent_time_field).click()
        self.driver.find_element(*self.rent_time_dropdown_option_4).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_5(self):
        self.driver.find_element(*self.rent_time_field).click()
        self.driver.find_element(*self.rent_time_dropdown_option_5).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_6(self):
        self.driver.find_element(*self.rent_time_field).click()
        self.driver.find_element(*self.rent_time_dropdown_option_6).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_7(self):
        self.driver.find_element(*self.rent_time_field).click()
        self.driver.find_element(*self.rent_time_dropdown_option_7).click()

    @allure.step('Отмечаем чек-бокс цвета "Черный жемчуг"')
    def set_checkbox_black(self):
        self.driver.find_element(*self.checkbox_black).click()

    @allure.step('Отмечаем чек-бокс цвета "Серая безысходность"')
    def set_checkbox_grey(self):
        self.driver.find_element(*self.checkbox_grey).click()

    @allure.step('Заполняем поле "Комментарий"')
    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Кликаем на кнопку "Да"')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Проверяем заголовок успешного заказа')
    def get_successfully_order_header(self):
        return self.driver.find_element(*self.order_modal_window).text

    @allure.step('Кликаем на кнопку "Посмотреть статус"')
    def click_check_status_button(self):
        self.driver.find_element(*self.check_status_button).click()




