import time

from main.pages.BasePage import BasePage
from main.pages.LoginPage import LoginPage


class Platform(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def launch(self, url):
        print("Open '%s' application" % url)
        time.sleep(2)
        self.driver.get(url + "/login")
        time.sleep(10)
        self.driver.refresh()
        time.sleep(5)
        return LoginPage(self.driver)
