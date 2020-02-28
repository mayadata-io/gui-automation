import allure

from main.pages.BasePage import BasePage
from main.pages.LoginPage import LoginPage


class Platform(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Open '{1}' application")
    def launch(self, url):
        self.driver.get(url)
        return LoginPage(self.driver)
