# Sprint_6 — UI автотесты для Яндекс Самокат

Проект с UI-автотестами на **Python + Pytest + Selenium** для сайта:
`https://qa-scooter.praktikum-services.ru/`

## Стек
- Python 3.12
- Pytest
- Selenium WebDriver (Firefox / geckodriver)
- Allure Report

## Структура проекта
- `pages/` — Page Object модели (BasePage, MainPage, OrderPage)
- `locators/` — локаторы страниц
- `tests/` — автотесты
- `data.py` — тестовые данные (ORDER_DATA, FAQ_DATA)
- `config/urls.py` — базовый URL проекта
- `pytest.ini` — настройки pytest (включая alluredir)
- `allure-results/` — результаты запуска (обычно игнорируются в git)

## Установка
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
