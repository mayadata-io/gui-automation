from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
from main.pages.SidePanel import SidePanel

DELETE_USER_BUTTON = (By.CSS_SELECTOR, ".btn.btn-link.text-danger")
AVAILABLE_ROLE = (By.XPATH, "//button[@id='dropdownMenuButton']")
DELETE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-danger")
ROLE_DROPDOWN_MENU = (By.XPATH, "//div[@class='dropdown-menu show']")
ERROR_TITLE = (By.XPATH, "//span[@class='jnoty-title']")
ERROR_MESSAGE = (By.XPATH, "//div[@class='jnoty-message']")


class UserRolesProfilePage(SidePanel):
    def __init__(self, driver):
        super().__init__(driver)

    def update_user_role(self, name):
        print("Select User Role '%s'" % name)
        self.wait_element_present(AVAILABLE_ROLE).click()
        select = self.wait_element_present(ROLE_DROPDOWN_MENU)
        for option in select.find_elements_by_tag_name('span'):
            if option.text in name:
                option.click()
                break
        self.sleep(10)
        return UserRolesProfilePage(self.driver)

    def verify_updated_user_role(self, name):
        print("Make sure that current role is '%s'" % name)
        text = self.wait_element_visible(AVAILABLE_ROLE).text
        print(text)
        is_exists = False
        if name in text:
            is_exists = True
        assert is_exists is True, "Wrong role is present"
        return UserRolesProfilePage(self.driver)

    def verify_error_message(self, title, message):
        print("Make sure that Error title '%s' and message '%s' are present" % (title, message))
        error_title = self.wait_element_visible(ERROR_TITLE).text
        error_message = self.wait_element_visible(ERROR_MESSAGE).text
        is_exists = False
        if title in error_title and message in error_message:
            is_exists = True
        assert is_exists is True, "Error message box absent"
        return UserRolesProfilePage(self.driver)

    def delete_user(self):
        print("Click on 'Delete user' button to delete user")
        self.wait_element_present(DELETE_USER_BUTTON).click()
        self.sleep(3)
        self.wait_element_present(DELETE_BUTTON).click()
        self.sleep(5)
        from main.pages.UserRolesPage import UserRolesPage
        return UserRolesPage(self.driver)

