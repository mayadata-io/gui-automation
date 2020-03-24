from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

INVITE_USER_BUTTON = (By.XPATH, "//button[text()='Invite user']")
# FILTER_CARDS = (By.CSS_SELECTOR, ".card.card-kanban")
FILTER_CARDS = (By.CSS_SELECTOR, ".nav.nav-card")
AVAILABLE_CLUSTERS = (By.CSS_SELECTOR, ".app-contents table tbody tr")


class UserRolesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

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
