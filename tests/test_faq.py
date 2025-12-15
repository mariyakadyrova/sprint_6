import allure
from pages.main_page import MainPage


@allure.feature("FAQ")
@allure.story("Проверка текста ответов в аккордеоне")
@allure.severity(allure.severity_level.MINOR)
def test_faq_answer_text(driver):
    main_page = MainPage(driver)

    with allure.step("Открываем главную страницу"):
        main_page.open()
        main_page.accept_cookies_if_needed()

    with allure.step("Получаем текст ответа на вопрос по индексу 0"):
        answer_text = main_page.get_faq_answer_text(index=0)

    with allure.step("Проверяем, что текст не пустой"):
        assert answer_text.strip() != ""
