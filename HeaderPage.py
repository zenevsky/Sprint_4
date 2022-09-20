import allure
from locators import HeaderPageLocators


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_header_order_button(self):
        self.driver.find_element(*HeaderPageLocators.header_order_button).click()

    @allure.step('Кликаем на лого Самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*HeaderPageLocators.scooter_logo).click()

    @allure.step('Кликаем на лого Яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*HeaderPageLocators.yandex_logo).click()


