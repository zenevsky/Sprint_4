import allure
from selenium import webdriver
from HeaderPage import HeaderPage
from MainPage import MainPage
from OrderPage import OrderPage
from YandexPage import YandexPage


class TestAccordion:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)

    @allure.title('Проверка текста под 1-ым вопросом')
    def test_check_text_under_1_header(self):

        main_page = MainPage(self.driver)

        main_page.open_page('https://qa-scooter.praktikum-services.ru/')

        main_page.accept_cookie()

        text_of_1_accordion = main_page.get_text_by_accordion_header_1()
        assert text_of_1_accordion == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка текста под 2-ым вопросом')
    def test_check_text_under_2_header(self):

        main_page = MainPage(self.driver)

        text_of_2_accordion = main_page.get_text_by_accordion_header_2()
        assert text_of_2_accordion == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с ' \
                                      'друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка текста под 3-им вопросом')
    def test_check_text_under_3_header(self):

        main_page = MainPage(self.driver)

        text_of_3_accordion = main_page.get_text_by_accordion_header_3()
        assert text_of_3_accordion == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение ' \
                                      'дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ ' \
                                      'курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 ' \
                                      'мая в 20:30.'

    @allure.title('Проверка текста под 4-ым вопросом')
    def test_check_text_under_4_header(self):

        main_page = MainPage(self.driver)

        text_of_4_accordion = main_page.get_text_by_accordion_header_4()
        assert text_of_4_accordion == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка текста под 5-ым вопросом')
    def test_check_text_under_5_header(self):

        main_page = MainPage(self.driver)

        text_of_5_accordion = main_page.get_text_by_accordion_header_5()
        assert text_of_5_accordion == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по ' \
                                      'красивому номеру 1010.'

    @allure.title('Проверка текста под 6-ым вопросом')
    def test_check_text_under_6_header(self):

        main_page = MainPage(self.driver)

        text_of_6_accordion = main_page.get_text_by_accordion_header_6()
        assert text_of_6_accordion == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — ' \
                                      'даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка текста под 7-ым вопросом')
    def test_check_text_under_7_header(self):

        main_page = MainPage(self.driver)

        text_of_7_accordion = main_page.get_text_by_accordion_header_7()
        assert text_of_7_accordion == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не ' \
                                      'попросим. Все же свои.'

    @allure.title('Проверка текста под 8-ым вопросом')
    def test_check_text_under_8_header(self):

        main_page = MainPage(self.driver)

        text_of_8_accordion = main_page.get_text_by_accordion_header_8()
        assert text_of_8_accordion == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


class TestOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)

    @allure.title('Проверка заказа с заполнением всех полей валидными значениями')
    def test_order(self):

        main_page = MainPage(self.driver)

        main_page.open_page('https://qa-scooter.praktikum-services.ru/')

        main_page.accept_cookie()

        main_page.click_main_block_order_button()

        order_page = OrderPage(self.driver)
        first_name = 'Тест'
        last_name = 'Тестов'
        address = 'Дельфинарий им. Маска'
        phone_number = '18136469359'
        date = '01.01.2023'
        comment = 'Дайте два'

        order_page.fill_in_fields_on_the_first_order_form(first_name, last_name, address, phone_number)

        order_page.click_next_button()

        order_page.set_date(date)
        order_page.unfocus()
        order_page.select_rent_time_dropdown_option_1()
        order_page.set_checkbox_black()
        order_page.set_comment(comment)

        order_page.click_order_button()

        order_page.click_yes_button()

        assert "Заказ оформлен" in order_page.get_successfully_order_header()

        order_page.click_check_status_button()

    @allure.title('Проверка заказа с заполнением только обязательных полей валидными значениями')
    def test_order_required_fields_only(self):

        header_page = HeaderPage(self.driver)

        header_page.click_header_order_button()

        order_page = OrderPage(self.driver)

        first_name = 'ТЕСТ'
        last_name = 'тестовый'
        address = 'Октябрьская 28А, 14'
        phone_number = '+79648368213'

        order_page.set_first_name(first_name)
        order_page.set_last_name(last_name)
        order_page.set_address(address)
        order_page.set_metro_station_2()
        order_page.set_phone_number(phone_number)

        order_page.click_next_button()

        order_page.select_date()
        order_page.unfocus()
        order_page.select_rent_time_dropdown_option_7()

        order_page.click_order_button()

        order_page.click_yes_button()

        assert "Заказ оформлен" in order_page.get_successfully_order_header()

        order_page.click_check_status_button()

    @allure.title('Проверка перехода на главную страницу Самоката по клику на лого Самокат')
    def test_header_scooter(self):

        header_page = HeaderPage(self.driver)

        header_page.click_scooter_logo()

        assert header_page.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверка перехода на главную страницу Яндекса по клику на лого Яндекс')
    def test_header_yandex(self):

        header_page = HeaderPage(self.driver)

        header_page.click_yandex_logo()

        header_page.driver.switch_to.window(self.driver.window_handles[-1])

        yandex_page = YandexPage(self.driver)

        yandex_page.wait_for_search_button()

        assert yandex_page.driver.current_url == "https://dzen.ru/?yredirect=true"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
