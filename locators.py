from selenium.webdriver.common.by import By


class MainPageLocators:

    main_block_order_button = [By.XPATH, "//div[contains(@class, 'Finish')]//button[text()='Заказать']"]

    accordion_header_1 = [By.ID, "accordion__heading-0"]

    accordion_panel_1 = [By.XPATH, "//div[@id='accordion__panel-0']//p"]

    accordion_header_2 = [By.ID, "accordion__heading-1"]

    accordion_panel_2 = [By.XPATH, "//div[@id='accordion__panel-1']//p"]

    accordion_header_3 = [By.ID, "accordion__heading-2"]

    accordion_panel_3 = [By.XPATH, "//div[@id='accordion__panel-2']//p"]

    accordion_header_4 = [By.ID, "accordion__heading-3"]

    accordion_panel_4 = [By.XPATH, "//div[@id='accordion__panel-3']//p"]

    accordion_header_5 = [By.ID, "accordion__heading-4"]

    accordion_panel_5 = [By.XPATH, "//div[@id='accordion__panel-4']//p"]

    accordion_header_6 = [By.ID, "accordion__heading-5"]

    accordion_panel_6 = [By.XPATH, "//div[@id='accordion__panel-5']//p"]

    accordion_header_7 = [By.ID, "accordion__heading-6"]

    accordion_panel_7 = [By.XPATH, "//div[@id='accordion__panel-6']//p"]

    accordion_header_8 = [By.ID, "accordion__heading-7"]

    accordion_panel_8 = [By.XPATH, "//div[@id='accordion__panel-7']//p"]

    cookie_button = [By.ID, "rcc-confirm-button"]


class OrderPageLocators:

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


class HeaderPageLocators:

    yandex_logo = [By.XPATH, "//img[@alt='Yandex']"]

    scooter_logo = [By.XPATH, "//img[@alt='Scooter']"]

    header_order_button = [By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']"]


class YandexPageLocators:

    search_button = [By.XPATH, "//button[text()='Найти']"]