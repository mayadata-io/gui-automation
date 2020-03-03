import allure

from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

CONNECT_NEW_CLUSTER = (By.XPATH, "//button[text()='Connect a new cluster']")
AVAILABLE_CLUSTERS = (By.CSS_SELECTOR, ".app-contents table tbody tr")
SORT_CLUSTERS_BUTTON = (By.CSS_SELECTOR, ".mi-arrow-up-down")


class ClustersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_connect_new_cluster_button(self):
        print("Click 'Connect a new cluster' button")
        self.wait_element_present(CONNECT_NEW_CLUSTER).click()
        return ClustersPage(self.driver)

    @allure.step("Make sure 'Cluster' with name '{1}' and status '{2}' present")
    def verify_cluster_present(self, name, status):
        is_exists = False
        self.wait_element_visible(SORT_CLUSTERS_BUTTON)
        my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)

        for my_cluster in my_clusters:
            text = my_cluster.text
            if name in text and status in text:
                is_exists = True
                break

        assert is_exists is True, "Cluster is absent"