from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url="https://demoqa.com/"):
        self.driver = driver
        self.base_url = base_url

    def open(self, path=""):
        self.driver.get(self.base_url + path)

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise NoSuchElementException(f"Element with locator {locator} not found within {time} seconds.")

