from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон: на него позвонит курьер')]")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class,'Button_Middle')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")


class MainPageLocators:
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button") #кнопка да все привыкли
    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//button[contains(@class,'Button_Button__') and text()='Заказать']"
    ) # верхняя кнопка "Заказать"

    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//button[contains(@class,'Button_Middle') and text()='Заказать']"
    ) # нижняя кнопка "Заказать"

    # логотип самоката на главной
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    # логотип Яндекса
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
