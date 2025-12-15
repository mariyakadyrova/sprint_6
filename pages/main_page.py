import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage
from locators.locators import MainPageLocators
from config.urls import BASE_URL




class MainPage(BasePage):
    URL = BASE_URL

    @allure.step("Открываем главную страницу Яндекс Самоката")
    def open(self):
        self.open_url(self.URL)

    @allure.step("Принимаем cookies, если баннер отображается")
    def accept_cookies_if_needed(self):
        if self.is_element_present(MainPageLocators.COOKIE_ACCEPT_BUTTON):
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step("Открываем форму заказа (верхняя кнопка)")
    def open_order_form_from_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Открываем форму заказа (нижняя кнопка)")
    def open_order_form_from_bottom(self):
        self.scroll_to(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Получаем текст ответа FAQ по индексу {index}")
    def get_faq_answer_text(self, index: int) -> str:
        question = (By.ID, f"accordion__heading-{index}")
        answer = (By.ID, f"accordion__panel-{index}")
        self.scroll_to(question)
        self.click(question)
        return self.get_text(answer)

    @allure.step("Кликаем по логотипу Яндекс и ожидаем открытие новой вкладки")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Ожидаем появления новой вкладки")
    def wait_for_new_tab(self, current_tabs):
        self.wait_for_new_tab_opened(current_tabs)
