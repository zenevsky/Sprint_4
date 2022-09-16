import allure
from selenium.webdriver.common.by import By


class HeaderPage:

    yandex_logo = [By.XPATH, "//img[@alt='Yandex']"]

    scooter_logo = [By.XPATH, "//img[@alt='Scooter']"]

    header_order_button = [By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_header_order_button(self):
        self.driver.find_element(*self.header_order_button).click()

    @allure.step('Кликаем на лого Самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step('Кликаем на лого Яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()


