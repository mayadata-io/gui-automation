from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage

SEARCH_FIELD = (By.CSS_SELECTOR, ".section-header input")
AVAILABLE_APPS = (By.CSS_SELECTOR, ".app-contents table tbody tr")
APPLICATION_NAME_LABEL = (By.CSS_SELECTOR, ".table-avatar")


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

    def search_application(self, name):
        self.wait_element_present(SEARCH_FIELD).send_keys(name)
        return ApplicationsPage(self.driver)

    def click_on_application(self, app_name, app_type):
        print("Click on '%s' application" % app_name)
        self.wait_element_visible(SEARCH_FIELD)
        clusters = self.wait_elements_visible(AVAILABLE_APPS)
        for my_cluster in clusters:
            text = my_cluster.text
            if app_name in text and app_type in text:
                self.wait_element_present(APPLICATION_NAME_LABEL).click()
                break
        from main.pages.clusters.applications.VolumesPage import VolumesPage
        return VolumesPage(self.driver)
