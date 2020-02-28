import allure

from main.pages.BasePage import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Verify if 'Email' field is empty")
    def verify_email_field_empty(self):
        return DashboardPage(self.driver)
