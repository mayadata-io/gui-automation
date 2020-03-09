import time
from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

FIRST_NAME_FIELD = (By.XPATH, "//label[text()='First Name']/following-sibling::input")
LAST_NAME_FIELD = (By.XPATH, "//label[text()='Last Name']/following-sibling::input")
EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
COMPANY_FIELD = (By.XPATH, "//label[text()='Company']/following-sibling::input")
ROLE_FIELD = (By.XPATH, "//label[text()='Role']/following-sibling::input")
PHONE_FIELD = (By.XPATH, "//label[text()='Phone']/following-sibling::input")
CHANGE_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Change Password']")

CURRENT_PASSWORD_FIELD = (By.XPATH, "//div[text()='Current password']/input")
NEW_PASSWORD_FIELD = (By.XPATH, "//div[text()='New password']/input")
RETYPE_PASSWORD_FIELD = (By.XPATH, "//div[text()='Retype password']/input")
UPDATE_PASSWORD_BUTTON = (By.XPATH, "//input[@value='Change Password']")


class UserProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_first_name_equals(self, first_name):
        print("Make sure 'First name' equals to '%s'" % first_name)
        actual_first_name = self.wait_element_present(FIRST_NAME_FIELD).get_attribute('value')

        assert actual_first_name == first_name, \
            "First name is wrong. Expected: %r; Actual: %r" % first_name % actual_first_name
        return UserProfilePage(self.driver)

    def verify_last_name_equals(self, last_name):
        print("Make sure 'Last name' equals to '%s'" % last_name)
        actual_last_name = self.wait_element_present(LAST_NAME_FIELD).get_attribute('value')

        assert actual_last_name == last_name, \
            "Last name is wrong. Expected: %r; Actual: %r" % last_name % actual_last_name
        return UserProfilePage(self.driver)

    def verify_email_equals(self, email):
        print("Make sure 'Email' equals to '%s'" % email)
        actual_email = self.wait_element_present(EMAIL_FIELD).get_attribute('value')

        assert actual_email == email, \
            "Email is wrong. Expected: %r; Actual: %r" % email % actual_email
        return UserProfilePage(self.driver)

    def verify_company_equals(self, company):
        print("Make sure 'Company' equals to '%s'" % company)
        actual_company = self.wait_element_present(COMPANY_FIELD).get_attribute('value')

        assert actual_company == company, \
            "Company is wrong. Expected: %r; Actual: %r" % company % actual_company
        return UserProfilePage(self.driver)

    def verify_role_equals(self, role):
        print("Make sure 'Role' equals to '%s'" % role)
        actual_role = self.wait_element_present(ROLE_FIELD).get_attribute('value')

        assert actual_role == role, \
            "Role is wrong. Expected: %r; Actual: %r" % role % actual_role
        return UserProfilePage(self.driver)

    def verify_phone_equals(self, phone):
        print("Make sure 'Phone' equals to '%s'" % phone)
        actual_phone = self.wait_element_present(PHONE_FIELD).get_attribute('value')

        assert actual_phone == phone, \
            "Phone is wrong. Expected: %r; Actual: %r" % phone % actual_phone
        return UserProfilePage(self.driver)

    def click_change_password_button(self):
        print("Click 'Change Password' button")
        self.wait_element_present(CHANGE_PASSWORD_BUTTON).click()
        return UserProfilePage(self.driver)

    def enter_current_password(self, password):
        print("Enter '%s' into 'Current password' field" % password)
        self.wait_element_present(CURRENT_PASSWORD_FIELD).send_keys(password)
        return UserProfilePage(self.driver)

    def enter_new_password(self, password):
        print("Enter '%s' into 'New password' field" % password)
        self.wait_element_present(NEW_PASSWORD_FIELD).send_keys(password)
        return UserProfilePage(self.driver)

    def enter_retype_password(self, password):
        print("Enter '%s' into 'Retype password' field" % password)
        self.wait_element_present(RETYPE_PASSWORD_FIELD).send_keys(password)
        return UserProfilePage(self.driver)

    def click_update_password_button(self):
        print("Click 'Update Password' button")
        self.wait_element_present(UPDATE_PASSWORD_BUTTON).click()
        time.sleep(2)

        return UserProfilePage(self.driver)

    def side_panel(self):
        from main.pages.SidePanel import SidePanel
        return SidePanel(self.driver)

