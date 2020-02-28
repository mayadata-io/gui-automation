import allure

from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

FIRST_NAME_FIELD = (By.XPATH, "//label[text()='First Name']/following-sibling::input")
LAST_NAME_FIELD = (By.XPATH, "//label[text()='Last Name']/following-sibling::input")
EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
COMPANY_FIELD = (By.XPATH, "//label[text()='Company']/following-sibling::input")
ROLE_FIELD = (By.XPATH, "//label[text()='Role']/following-sibling::input")
PHONE_FIELD = (By.XPATH, "//label[text()='Phone']/following-sibling::input")


class UserProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Make sure 'First name' equals to '{1}'")
    def verify_first_name_equals(self, first_name):
        actual_first_name = self.wait_element_present(FIRST_NAME_FIELD).get_attribute('value')

        assert actual_first_name == first_name, \
            "First name is wrong. Expected: %r; Actual: %r" % first_name % actual_first_name
        return UserProfilePage(self.driver)

    @allure.step("Make sure 'Last name' equals to '{1}'")
    def verify_last_name_equals(self, last_name):
        actual_last_name = self.wait_element_present(LAST_NAME_FIELD).get_attribute('value')

        assert actual_last_name == last_name, \
            "Last name is wrong. Expected: %r; Actual: %r" % last_name % actual_last_name
        return UserProfilePage(self.driver)

    @allure.step("Make sure 'Email' equals to '{1}'")
    def verify_email_equals(self, email):
        actual_email = self.wait_element_present(EMAIL_FIELD).get_attribute('value')

        assert actual_email == email, \
            "Email is wrong. Expected: %r; Actual: %r" % email % actual_email
        return UserProfilePage(self.driver)

    @allure.step("Make sure 'Company' equals to '{1}'")
    def verify_company_equals(self, company):
        actual_company = self.wait_element_present(COMPANY_FIELD).get_attribute('value')

        assert actual_company == company, \
            "Company is wrong. Expected: %r; Actual: %r" % company % actual_company
        return UserProfilePage(self.driver)

    @allure.step("Make sure 'Role' equals to '{1}'")
    def verify_role_equals(self, role):
        actual_role = self.wait_element_present(ROLE_FIELD).get_attribute('value')

        assert actual_role == role, \
            "Role is wrong. Expected: %r; Actual: %r" % role % actual_role
        return UserProfilePage(self.driver)

    @allure.step("Make sure 'Phone' equals to '{1}'")
    def verify_phone_equals(self, phone):
        actual_phone = self.wait_element_present(PHONE_FIELD).get_attribute('value')

        assert actual_phone == phone, \
            "Phone is wrong. Expected: %r; Actual: %r" % phone % actual_phone
        return UserProfilePage(self.driver)

