import time

from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
from main.pages.LoginPage import LoginPage

EMAIL_FIELD = (By.ID, "signinEmail")


class Platform(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def launch(self, url):
        print("Open '%s' application" % url)
        time.sleep(2)
        self.driver.get(url.replace('https', 'http') + "/login")
        time.sleep(5)

        try:
            self.wait_element_present(EMAIL_FIELD).click()
        except Exception:
            self.driver.refresh()
            time.sleep(5)

        return LoginPage(self.driver)
