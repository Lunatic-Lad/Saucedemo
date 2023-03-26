from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from support.logger import log_method


class BaseObject:
    log = log_method()
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_present(self, locator):
        self.log.info(f"{locator} getting present element")
        return self.wait.until(ec.presence_of_element_located(locator))

    def is_visible(self, locator):
        self.log.info(f"{locator} getting visible element")
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        self.log.info(f"{locator} getting clickable element")
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator):
        self.log.info(f"{locator} clicking on the element")
        self.is_visible(locator).click()

    def type_keys(self, locator, text):
        self.log.info(f"{locator} reading visible text")
        self.is_visible(locator).send_keys(text)

    def get_text(self, locator):
        self.log.info(f"{locator} saving visible text")
        return self.is_visible(locator).text


