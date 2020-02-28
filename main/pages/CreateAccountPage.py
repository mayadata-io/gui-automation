import allure
from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage
from main.pages.PortalHomePage import PortalHomePage

FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='John']")
LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='Miller']")
EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
PASSWORD_FIELD = (By.CSS_SELECTOR, ".passify-field")
SIGNUP_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg.btn-block")


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter '{1}' into 'First name' field")
    def enter_first_name(self, firstname):
        self.wait_element_present(FIRST_NAME_FIELD).send_keys(firstname)
        return CreateAccountPage(self.driver)

    @allure.step("Enter '{1}' into 'Last name' field")
    def enter_last_name(self, lastname):
        self.wait_element_present(LAST_NAME_FIELD).send_keys(lastname)
        return CreateAccountPage(self.driver)

    @allure.step("Enter '{1}' into 'Email' field")
    def enter_email(self, email):
        self.wait_element_present(EMAIL_FIELD).send_keys(email)
        return CreateAccountPage(self.driver)

    @allure.step("Enter '{1}' into 'Password' field")
    def enter_password(self, password):
        self.wait_element_present(PASSWORD_FIELD).send_keys(password)
        return CreateAccountPage(self.driver)

    @allure.step("Click 'Signup' button")
    def click_signup_button(self):
        self.wait_element_present(SIGNUP_BUTTON).click()
        return PortalHomePage(self.driver)