import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

ALERT_CONTAINER = (By.CSS_SELECTOR, ".alert.mo-alert-danger")
LOADING_CONTAINER = (By.CSS_SELECTOR, ".loading-container")


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_element_present(self, *locator):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(*locator))
        return WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable(*locator))

    def wait_element_visible(self, *locator):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(*locator))
        return WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(*locator))

    def wait_elements_visible(self, *locator):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(*locator))
        return WebDriverWait(self.driver, 30).until(ec.presence_of_all_elements_located(*locator))

    @staticmethod
    def sleep(wait_time):
        time.sleep(wait_time)

    def find_element_by_id(self, locator):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_id(locator)

    def navigate_to(self, page):
        self.driver.get(page)

    def verify_alert_present(self, message):
        print("Make sure validation message equals to '%s'" % message)
        text = self.wait_element_visible(ALERT_CONTAINER).text
        is_message_correct = message in text

        assert is_message_correct is True, "Validation message is wrong"
        return BasePage(self.driver)

    def wait_loading_container_absent(self):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(LOADING_CONTAINER))
        return WebDriverWait(self.driver, 30).until(ec.invisibility_of_element(LOADING_CONTAINER))