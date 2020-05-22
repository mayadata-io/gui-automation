from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
from main.pages.SidePanel import SidePanel

INVITE_USER_BUTTON = (By.XPATH, "//button[text()='Invite user']")
EMAIL_FIELD = (By.CSS_SELECTOR, "form.mt-3 input[type='email']")
ROLE_DROPDOWN = (By.CSS_SELECTOR, "form.mt-3 div.ember-power-select-trigger")
AVAILABLE_ROLES = (By.CSS_SELECTOR, "ul.ember-power-select-options li")
SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Find a user...']")
SEND_INVITE_BUTTON = (By.CSS_SELECTOR, "form.mt-3 button")
# FILTER_CARDS = (By.CSS_SELECTOR, ".card.card-kanban")
FILTER_CARDS = (By.CSS_SELECTOR, ".nav.nav-card")
AVAILABLE_INVITATIONS = (By.CSS_SELECTOR, ".app-contents table tbody tr")
PROFILE_DROPDOWN = (By.CSS_SELECTOR, ".typeahead-item")
PROFILE_UPDATE_ICON = (By.XPATH, "//i[@class='mi mi-eye mi-1x']")


class UserRolesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_invite_button(self):
        print("Click 'Invite' button")
        self.wait_element_present(INVITE_USER_BUTTON).click()
        return UserRolesPage(self.driver)

    def select_role(self, role):
        print("Select '%s' role" % role)
        self.wait_element_present(ROLE_DROPDOWN).click()
        roles = self.wait_elements_visible(AVAILABLE_ROLES)

        for u_role in roles:
            text = u_role.text
            if role in text:
                u_role.click()
                break

        return UserRolesPage(self.driver)

    def enter_email(self, email):
        print("Enter '%s' into 'Email' field" % email)
        self.wait_element_present(EMAIL_FIELD).send_keys(email)
        return UserRolesPage(self.driver)

    # def enter_user(self, email):
    #     print("Enter '%s' into 'Search' field" % email)
    #     self.wait_element_present(SEARCH_FIELD).send_keys(email)
    #     return UserRolesPage(self.driver)

    def select_profile(self):
        print("Select profile from dropdown" )
        self.wait_element_present(PROFILE_DROPDOWN).click()
        return UserRolesPage(self.driver)

    def click_send_invite_button(self):
        print("Click 'Invite' button")
        self.wait_element_present(SEND_INVITE_BUTTON).click()
        self.sleep(10)
        return SidePanel(self.driver)

    def switch_to_filter_tab(self, name):
        print("Switch to '%s' filter tab" % name)
        is_exists = False
        try:
            self.wait_element_visible(INVITE_USER_BUTTON)
        except Exception:
            self.wait_element_invisible(INVITE_USER_BUTTON)
        items = self.wait_elements_visible(FILTER_CARDS)

        for item in items:
            text = item.text
            if name in text:
                is_exists = True
                item.click()
                break

        assert is_exists is True, "Filter tab is absent"
        return UserRolesPage(self.driver)

    def verify_user_present(self, name, status):
        print("Make sure user '%s' present and status is '%s'" % (name, status))
        is_exists = False
        self.wait_element_visible(INVITE_USER_BUTTON)
        invitations = self.wait_elements_visible(AVAILABLE_INVITATIONS)

        for invitation in invitations:
            text = invitation.text
            if name in text and status in text:
                is_exists = True
                break

        assert is_exists is True, "Invitation is absent"
        return UserRolesPage(self.driver)

    def verify_user_absent(self, name):
        print("Make sure user '%s' is absent" % name)
        is_exists = True
        self.wait_element_visible(INVITE_USER_BUTTON)
        invitations = self.wait_elements_visible(AVAILABLE_INVITATIONS)

        for invitation in invitations:
            text = invitation.text
            if name in text:
                is_exists = False
                break

        assert is_exists is True, "User is present"
        return UserRolesPage(self.driver)

    def find_user(self, name):
        print("Enter '%s' into Find a user search field")
        self.wait_element_present(SEARCH_FIELD).send_keys(name)
        return UserRolesPage(self.driver)

    def open_user_role_profile_page(self):
        print("Click on update icon to update user profile")
        self.wait_element_present(PROFILE_UPDATE_ICON).click()
        self.sleep(3)
        from main.pages.UserRolesProfilePage import UserRolesProfilePage
        return UserRolesProfilePage(self.driver)
