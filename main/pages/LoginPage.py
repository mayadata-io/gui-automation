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

    def enter_email(self, email):
        print("Enter '%s' into 'Email' field" % email)
        self.wait_element_present(EMAIL_FIELD).send_keys(email)
        return LoginPage(self.driver)

    def verify_email_field_present(self):
        print("Verify 'Email' field is present")
        self.wait_element_present(EMAIL_FIELD)
        return LoginPage(self.driver)

    def enter_password(self, password):
        print("Enter '%s' into 'Email' field" % password)
        self.wait_element_present(PASSWORD_FIELD).send_keys(password)
        return LoginPage(self.driver)

    def click_login_button(self):
        print("Click 'Login' button")
        self.wait_element_present(LOGIN_BUTTON).click()
        return PortalHomePage(self.driver)

    def click_create_account_link(self):
        print("Click 'Create account' link")
        self.wait_element_present(CREATE_ACCOUNT_BUTTON).click()
        return CreateAccountPage(self.driver)
