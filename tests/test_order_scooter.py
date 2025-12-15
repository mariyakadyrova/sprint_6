import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA_NO_COMMENT, ORDER_DATA_WITH_COMMENT


@allure.feature("Заказ самоката")
@allure.story("Позитивный заказ через верхнюю/нижнюю кнопку")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "open_order_method, title",
    [
        ("open_order_form_from_top", "Позитивный заказ самоката (кнопка сверху)"),
        ("open_order_form_from_bottom", "Позитивный заказ самоката (кнопка снизу)"),
    ],
)
@pytest.mark.parametrize("data", ORDER_DATA_NO_COMMENT)
def test_order_scooter_positive_flow_no_comment(driver, data, open_order_method, title):
    allure.dynamic.title(f"{title} — без комментария")

    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    with allure.step("Открываем главную страницу и принимаем cookies"):
        main_page.open()
        main_page.accept_cookies_if_needed()

    with allure.step("Открываем форму заказа"):
        getattr(main_page, open_order_method)()

    with allure.step("Заполняем первый шаг формы"):
        order_page.fill_first_step(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            metro=data["metro"],
            phone=data["phone"],
        )

    with allure.step("Заполняем второй шаг формы (без комментария)"):
        order_page.fill_second_step(
            date=data["date"],
            rent_period=data["rent_period"],
            color_locator=data["color_locator"],
        )

    with allure.step("Отправляем заказ"):
        order_page.submit_order()

    with allure.step("Проверяем, что заказ успешно оформлен"):
        assert order_page.is_order_successful()


@allure.feature("Заказ самоката")
@allure.story("Позитивный заказ через верхнюю/нижнюю кнопку")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "open_order_method, title",
    [
        ("open_order_form_from_top", "Позитивный заказ самоката (кнопка сверху)"),
        ("open_order_form_from_bottom", "Позитивный заказ самоката (кнопка снизу)"),
    ],
)
@pytest.mark.parametrize("data", ORDER_DATA_WITH_COMMENT)
def test_order_scooter_positive_flow_with_comment(driver, data, open_order_method, title):
    allure.dynamic.title(f"{title} — с комментарием")

    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    with allure.step("Открываем главную страницу и принимаем cookies"):
        main_page.open()
        main_page.accept_cookies_if_needed()

    with allure.step("Открываем форму заказа"):
        getattr(main_page, open_order_method)()

    with allure.step("Заполняем первый шаг формы"):
        order_page.fill_first_step(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            metro=data["metro"],
            phone=data["phone"],
        )

    with allure.step("Заполняем второй шаг формы"):
        order_page.fill_second_step(
            date=data["date"],
            rent_period=data["rent_period"],
            color_locator=data["color_locator"],
        )

    with allure.step("Заполняем комментарий"):
        order_page.set_comment(data["comment"])

    with allure.step("Отправляем заказ"):
        order_page.submit_order()

    with allure.step("Проверяем, что заказ успешно оформлен"):
        assert order_page.is_order_successful()
