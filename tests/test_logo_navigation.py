import allure
from pages.main_page import MainPage


@allure.feature("Навигация по логотипам")
@allure.story("Переход на Дзен по клику на логотип Яндекса")
@allure.severity(allure.severity_level.NORMAL)
def test_click_yandex_logo_opens_dzen(driver):
    allure.dynamic.title("Проверка перехода на Дзен по клику на логотип Яндекса")

    main_page = MainPage(driver)

    with allure.step("Открываем главную страницу"):
        main_page.open()
        main_page.accept_cookies_if_needed()

    with allure.step("Кликаем по логотипу Яндекса"):
        main_page.click_yandex_logo()

    with allure.step("Переключаемся на новую вкладку и проверяем URL"):
        main_page.switch_to_new_tab()
        main_page.wait_url_contains("dzen.ru")
        assert main_page.current_url_contains("dzen.ru")

