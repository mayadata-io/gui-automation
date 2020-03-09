from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, ALERT_CONTAINER
from main.pages.OnboardingPage import OnboardingPage

FIRST_NAME_FIELD = (By.ID, "signupFirstName")
LAST_NAME_FIELD = (By.ID, "signupLastName")
EMAIL_FIELD = (By.ID, "signupEmail")
PASSWORD_FIELD = (By.ID, "signupPassword")
SIGNUP_BUTTON = (By.CSS_SELECTOR, "button.btn-login-2.btn-block.btn-lg")


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, firstname):
        print("Enter '%s' into 'First name' field" % firstname)
        self.wait_element_present(FIRST_NAME_FIELD).send_keys(firstname)
        return CreateAccountPage(self.driver)

    def enter_last_name(self, lastname):
        print("Enter '%s' into 'Last name' field" % lastname)
        self.wait_element_present(LAST_NAME_FIELD).send_keys(lastname)
        return CreateAccountPage(self.driver)

    def enter_email(self, email):
        print("Enter '%s' into 'Email' field" % email)
        self.wait_element_present(EMAIL_FIELD).clear()
        self.wait_element_present(EMAIL_FIELD).send_keys(email)
        return CreateAccountPage(self.driver)

    def enter_password(self, password):
        print("Enter '%s' into 'Password' field" % password)
        self.wait_element_present(PASSWORD_FIELD).send_keys(password)
        return CreateAccountPage(self.driver)

    def click_signup_button_for_validation(self):
        print("Click 'Signup' link")
        self.wait_element_present(SIGNUP_BUTTON).click()
        return CreateAccountPage(self.driver)

    def click_signup_button(self):
        print("Click 'Signup' link")
        self.wait_element_present(SIGNUP_BUTTON).click()
        return OnboardingPage(self.driver)

    def verify_error_message_present(self, message):
        print("Make sure validation message equals to '%s'" % message)
        text = self.wait_element_visible(ALERT_CONTAINER).text
        is_message_correct = message in text

        assert is_message_correct is True, "Validation message is wrong"
        return CreateAccountPage(self.driver)