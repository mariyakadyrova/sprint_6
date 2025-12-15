from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- базовые действия ---
    def open_url(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("window.scrollBy(0, -100);")
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text: str, clear: bool = True):
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def send_keys(self, locator, *keys):
        element = self.find(locator)
        element.send_keys(*keys)

    def scroll_to(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("window.scrollBy(0, -100);")
        return element

    def get_text(self, locator) -> str:
        return self.find(locator).text

    # --- проверки ---
    def is_element_present(self, locator, timeout: int = 2) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_displayed(self, locator, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # --- работа с URL ---
    def get_current_url(self) -> str:
        return self.driver.current_url

    def current_url_contains(self, text: str) -> bool:
        return text in self.get_current_url()

    # --- вкладки (табы) ---
    def wait_for_new_tab_opened(self, current_tabs, timeout: int = 5):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > len(current_tabs)
        )

    def switch_to_new_tab(self, timeout: int = 5):
        current_handle = self.driver.current_window_handle

        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
        )

        for handle in self.driver.window_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                return handle

        raise TimeoutException("New tab did not appear")

    def wait_url_contains(self, text: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))