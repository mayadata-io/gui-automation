import time

from main.pages.BasePage import BasePage
from main.pages.LoginPage import LoginPage


class Platform(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def launch(self, url):
        print("Open '%s' application" % url)
        time.sleep(2)
        self.driver.get(url)
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        return LoginPage(self.driver)
