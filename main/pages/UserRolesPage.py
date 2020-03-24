from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

INVITE_USER_BUTTON = (By.XPATH, "//button[text()='Invite user']")
EMAIL_FIELD = (By.CSS_SELECTOR, "form.mt-3 input[type='email']")
ROLE_DROPDOWN = (By.CSS_SELECTOR, "form.mt-3 div.ember-power-select-trigger")
AVAILABLE_ROLES = (By.CSS_SELECTOR, "ul.ember-power-select-options li")
SEND_INVITE_BUTTON = (By.CSS_SELECTOR, "form.mt-3 button")
# FILTER_CARDS = (By.CSS_SELECTOR, ".card.card-kanban")
FILTER_CARDS = (By.CSS_SELECTOR, ".nav.nav-card")
AVAILABLE_CLUSTERS = (By.CSS_SELECTOR, ".app-contents table tbody tr")


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

    def click_send_invite_button(self):
        print("Click 'Invite' button")
        self.wait_element_present(SEND_INVITE_BUTTON).click()
        self.sleep(3)
        return UserRolesPage(self.driver)

    def switch_to_filter_tab(self, name):
        print("Switch to '%s' filter tab" % name)
        is_exists = False
        self.wait_element_visible(INVITE_USER_BUTTON)
        items = self.wait_elements_visible(FILTER_CARDS)

        for item in items:
            text = item.text
            if name in text:
                is_exists = True
                item.click()
                break

        assert is_exists is True, "Cluster tab is absent"
        return UserRolesPage(self.driver)

    def verify_user_present(self, name, status):
        print("Make sure user '%s' present" % name)
        is_exists = False
        self.wait_element_visible(INVITE_USER_BUTTON)
        my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)

        for my_cluster in my_clusters:
            text = my_cluster.text
            if name in text and status in text:
                is_exists = True
                break

        assert is_exists is True, "Cluster is absent"
        return UserRolesPage(self.driver)
