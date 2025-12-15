import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from locators.locators import OrderPageLocators



class OrderPage(BasePage):

    @allure.step("Выбираем станцию метро: {metro}")
    def choose_metro(self, metro: str):
        self.click(OrderPageLocators.METRO_INPUT)
        self.type(OrderPageLocators.METRO_INPUT, metro)

        metro_option = (
            By.XPATH,
            f"//div[contains(@class,'select-search__select')]//*[text()='{metro}']"
        )
        self.click(metro_option)

    @allure.step("Заполняем первый шаг заказа: {first_name} {last_name}, метро: {metro}")
    def fill_first_step(self, first_name, last_name, address, metro, phone):
        self.type(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.type(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.type(OrderPageLocators.ADDRESS_INPUT, address)
        self.type(OrderPageLocators.PHONE_INPUT, phone)

        self.choose_metro(metro)

        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Указываем дату доставки: {date}")
    def set_delivery_date(self, date):
        self.type(OrderPageLocators.DATE_INPUT, date)
        self.send_keys(OrderPageLocators.DATE_INPUT, Keys.ENTER)

    @allure.step("Выбираем срок аренды: {rent_period}")
    def choose_rent_period(self, rent_period):
        self.click(OrderPageLocators.RENT_DROPDOWN)
        rent_option = (By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{rent_period}']")
        self.click(rent_option)

    @allure.step("Выбираем цвет самоката")
    def choose_color(self, color_locator):
        self.click(color_locator)

    @allure.step("Добавляем комментарий: {comment}")
    def set_comment(self, comment):
        self.type(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Заполняем второй шаг заказа: дата {date}, срок аренды {rent_period}")
    def fill_second_step(self, date, rent_period, color_locator):
        self.set_delivery_date(date)
        self.choose_rent_period(rent_period)
        self.choose_color(color_locator)

    @allure.step("Подтверждаем заказ")
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверяем, что появилась модалка об успешном заказе")
    def is_order_successful(self):
        return self.is_displayed(OrderPageLocators.SUCCESS_MODAL)
