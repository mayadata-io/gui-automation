from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage

CONTROL_PLANE_TAB = (By.CSS_SELECTOR, "a[href$='/controlplanes']")
POOLS_TAB = (By.CSS_SELECTOR, "a[href$='/pools']")
VOLUMES_TAB = (By.CSS_SELECTOR, "a[href*='resources/applications?version']")
HEADER_TITLE = (By.CSS_SELECTOR, ".section-header_title")


class OpenEbsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_connect_new_cluster_button(self):
        print("Click 'Connect a new cluster' button")
        self.wait_element_present(CONTROL_PLANE_TAB).click()
        return OpenEbsPage(self.driver)

    def click_connect_new_cluster_button(self):
        print("Click 'Connect a new cluster' button")
        self.wait_element_present(POOLS_TAB).click()
        return OpenEbsPage(self.driver)

    def click_connect_new_cluster_button(self):
        print("Click 'Connect a new cluster' button")
        self.wait_element_present(VOLUMES_TAB).click()
        return OpenEbsPage(self.driver)
