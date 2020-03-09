from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage
from main.pages.CreateAccountPage import CreateAccountPage
from main.pages.SidePanel import SidePanel

EMAIL_FIELD = (By.ID, "signinEmail")
PASSWORD_FIELD = (By.ID, "signinPassword")
LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-login-2.btn-lg.btn-block")
CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a.login-signup-link")


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
        return SidePanel(self.driver)

    def login(self, email, password):
        print("Click 'Login' button")
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        return SidePanel(self.driver)

    def click_create_account_link(self):
        print("Click 'Create account' link")
        self.wait_element_present(CREATE_ACCOUNT_BUTTON).click()
        return CreateAccountPage(self.driver)
