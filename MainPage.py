import allure
from locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем главную страницу https://qa-scooter.praktikum-services.ru/')
    def open_page(self, page):
        self.driver.get(page)

    @allure.step('Принимаем куки, кликая на кнопку "да все привыкли"')
    def accept_cookie(self):
        self.driver.find_element(*MainPageLocators.cookie_button).click()

    def scroll_down(self):
        element = self.driver.find_element(*MainPageLocators.cookie_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_main_block_order_button_is_enabled(self):
        return self.driver.find_element(*MainPageLocators.main_block_order_button).is_enabled()

    @allure.step('Кликаем на кнопку "Заказать" в главном блоке страницы')
    def click_main_block_order_button(self):
        self.driver.find_element(*MainPageLocators.main_block_order_button).click()

    @allure.step('Получаем текст под 1-ым вопросом')
    def get_text_by_accordion_header_1(self):
        self.driver.find_element(*MainPageLocators.accordion_header_1).click()
        return self.driver.find_element(*MainPageLocators.accordion_panel_1).text

    @allure.step('Получаем текст под 2-ым вопросом')
    def get_text_by_accordion_header_2(self):
        self.driver.find_element(*MainPageLocators.accordion_header_2).click()
        return self.driver.find_element(*MainPageLocators.accordion_panel_2).text

    @allure.step('Получаем текст под 3-ым вопросом')
    def get_text_by_accordion_header_3(self):
        self.driver.find_element(*MainPageLocators.accordion_header_3).click()
        return self.driver.find_element(*MainPageLocators.accordion_panel_3).text

    @allure.step('Получаем текст под 4-ым вопросом')
    def get_text_by_accordion_header_4(self):
        self.driver.find_element(*MainPageLocators.accordion_header_4).click()
        return self.driver.find_element(*MainPageLocators.accordion_panel_4).text

    @allure.step('Получаем текст под 5-ым вопросом')
    def get_text_by_accordion_header_5(self):
        self.driver.find_element(*MainPageLocators.accordion_header_5).click()
        return self.driver.find_element(*MainPageLocators.accordion_panel_5).text

    @allure.step('Получаем текст под 6-ым вопросом')
    def get_text_by_accordion_header_6(self):
        self.driver.find_element(*MainPageLocators.accordion_header_6).click()
        return self.driver.find_element(*MainPageLocators.accordion_panel_6).text

    @allure.step('Получаем текст под 7-ым вопросом')
    def get_text_by_accordion_header_7(self):
        self.driver.find_element(*MainPageLocators.accordion_header_7).click()
        return self.driver.find_element(*MainPageLocators.accordion_panel_7).text

    @allure.step('Получаем текст под 8-ым вопросом')
    def get_text_by_accordion_header_8(self):
        self.driver.find_element(*MainPageLocators.accordion_header_8).click()
        return self.driver.find_element(*MainPageLocators.accordion_panel_8).text

