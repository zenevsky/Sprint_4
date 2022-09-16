from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class YandexPage:

    search_button = [By.XPATH, "//button[text()='Найти']"]

    def __init__(self, driver):
        self.driver = driver

    def wait_for_search_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.search_button))