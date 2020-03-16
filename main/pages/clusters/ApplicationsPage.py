from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage

SEARCH_FIELD = (By.CSS_SELECTOR, ".section-header input")
AVAILABLE_APPS = (By.CSS_SELECTOR, ".app-contents table tbody tr")


class ApplicationsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_applications_present(self):
        print("Make sure applications records present")
        is_exists = False
        self.wait_element_visible(SEARCH_FIELD)
        clusters = self.wait_elements_visible(AVAILABLE_APPS)
        size = len(clusters)

        assert size > 1, "Number of applications is wrong"
        return ApplicationsPage(self.driver)
