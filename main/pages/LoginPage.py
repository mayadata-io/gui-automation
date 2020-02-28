import allure
from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage
from main.pages.CreateAccountPage import CreateAccountPage
from main.pages.PortalHomePage import PortalHomePage

EMAIL_FIELD = (By.CSS_SELECTOR, "input[autocomplete='username']")
PASSWORD_FIELD = (By.CSS_SELECTOR, "input[autocomplete='current-password']")
LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg.btn-block")
CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-secondary")


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter '{1}' into 'Email' field")
    def enter_email(self, email):
        self.wait_element_present(EMAIL_FIELD).send_keys(email)
        return LoginPage(self.driver)

    @allure.step("Verify 'Email' field is present")
    def verify_email_field_present(self):
        self.wait_element_present(EMAIL_FIELD)
        return LoginPage(self.driver)

    @allure.step("Enter '{1}' into 'Password' field")
    def enter_password(self, password):
        self.wait_element_present(PASSWORD_FIELD).send_keys(password)
        return LoginPage(self.driver)

    @allure.step("Click 'Login' button")
    def click_login_button(self):
        self.wait_element_present(LOGIN_BUTTON).click()
        return PortalHomePage(self.driver)

    @allure.step("Click 'Create account' link")
    def click_create_account_link(self):
        self.wait_element_present(CREATE_ACCOUNT_BUTTON).click()
        return CreateAccountPage(self.driver)
