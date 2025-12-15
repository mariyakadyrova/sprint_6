import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://qa-scooter.praktikum-services.ru/"
GECKO_PATH = "/opt/homebrew/bin/geckodriver"

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    # options.add_argument("-headless")  # для невидимого запуска
    service = Service(GECKO_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
