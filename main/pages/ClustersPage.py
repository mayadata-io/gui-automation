import allure

from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

FIRST_NAME_FIELD = (By.XPATH, "//label[text()='First Name']/following-sibling::input")
LAST_NAME_FIELD = (By.XPATH, "//label[text()='Last Name']/following-sibling::input")
EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
COMPANY_FIELD = (By.XPATH, "//label[text()='Company']/following-sibling::input")
ROLE_FIELD = (By.XPATH, "//label[text()='Role']/following-sibling::input")
PHONE_FIELD = (By.XPATH, "//label[text()='Phone']/following-sibling::input")
CHANGE_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Change Password']")

COMPANY_FIELD = (By.XPATH, "//div[text()='Current password']/input")
COMPANY_FIELD = (By.XPATH, "//div[text()='Current password']/input")
COMPANY_FIELD = (By.XPATH, "//div[text()='Current password']/input")

class UserProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Make sure 'First name' equals to '{1}'")
    def verify_first_name_equals(self, first_name):
        actual_first_name = self.wait_element_present(FIRST_