import allure
from locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем главную страницу https://qa-scooter.praktikum-services.ru/')
    def open_page(self, page):
        self.driver.get(page)

    @allure.step('Заполняем поле "Имя"')
    def set_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.first_name_field).send_keys(first_name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.last_name_field).send_keys(last_name)

    @allure.step('Заполняем поле "Адрес"')
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.address_field).send_keys(address)

    @allure.step('Заполняем поле "Станция метро"')
    def set_metro_station_1(self):
        self.driver.find_element(*OrderPageLocators.metro_station_field).click()
        self.driver.find_element(*OrderPageLocators.metro_station_1).click()

    @allure.step('Заполняем поле "Станция метро"')
    def set_metro_station_2(self):
        self.driver.find_element(*OrderPageLocators.metro_station_field).click()
        self.driver.find_element(*OrderPageLocators.metro_station_2).click()

    @allure.step('Заполняем поле "Телефон"')
    def set_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.phone_number_field).send_keys(phone_number)

    @allure.step('Заполняем первую страницу формы')
    def fill_in_fields_on_the_first_order_form(self, first_name, last_name, address, phone_number):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro_station_1()
        self.set_phone_number(phone_number)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    @allure.step('Заполняем дату вводом с клавиатуры')
    def set_date(self, date):
        self.driver.find_element(*OrderPageLocators.date_field).send_keys(date)

    @allure.step('Заполняем дату выбором через календарь')
    def select_date(self):
        self.driver.find_element(*OrderPageLocators.date_field).click()
        self.driver.find_element(*OrderPageLocators.day_in_the_calendar).click()

    def unfocus(self):
        self.driver.find_element(*OrderPageLocators.about_rent_header).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_1(self):
        self.driver.find_element(*OrderPageLocators.rent_time_field).click()
        self.driver.find_element(*OrderPageLocators.rent_time_dropdown_option_1).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_2(self):
        self.driver.find_element(*OrderPageLocators.rent_time_field).click()
        self.driver.find_element(*OrderPageLocators.rent_time_dropdown_option_2).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_3(self):
        self.driver.find_element(*OrderPageLocators.rent_time_field).click()
        self.driver.find_element(*OrderPageLocators.rent_time_dropdown_option_3).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_4(self):
        self.driver.find_element(*OrderPageLocators.rent_time_field).click()
        self.driver.find_element(*OrderPageLocators.rent_time_dropdown_option_4).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_5(self):
        self.driver.find_element(*OrderPageLocators.rent_time_field).click()
        self.driver.find_element(*OrderPageLocators.rent_time_dropdown_option_5).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_6(self):
        self.driver.find_element(*OrderPageLocators.rent_time_field).click()
        self.driver.find_element(*OrderPageLocators.rent_time_dropdown_option_6).click()

    @allure.step('Выбираем значение срока аренды')
    def select_rent_time_dropdown_option_7(self):
        self.driver.find_element(*OrderPageLocators.rent_time_field).click()
        self.driver.find_element(*OrderPageLocators.rent_time_dropdown_option_7).click()

    @allure.step('Отмечаем чек-бокс цвета "Черный жемчуг"')
    def set_checkbox_black(self):
        self.driver.find_element(*OrderPageLocators.checkbox_black).click()

    @allure.step('Отмечаем чек-бокс цвета "Серая безысходность"')
    def set_checkbox_grey(self):
        self.driver.find_element(*OrderPageLocators.checkbox_grey).click()

    @allure.step('Заполняем поле "Комментарий"')
    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.comment_field).send_keys(comment)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    @allure.step('Кликаем на кнопку "Да"')
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Проверяем заголовок успешного заказа')
    def get_successfully_order_header(self):
        return self.driver.find_element(*OrderPageLocators.order_modal_window).text

    @allure.step('Кликаем на кнопку "Посмотреть статус"')
    def click_check_status_button(self):
        self.driver.find_element(*OrderPageLocators.check_status_button).click()




