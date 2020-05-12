from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER
from main.pages.clusters.ClusterOverviewPage import ClusterOverviewPage
from main.pages.clusters.ConnectClusterPage import ConnectClusterPage

CONNECT_NEW_CLUSTER = (By.XPATH, "//button[text()='Connect a new cluster']")
AVAILABLE_CLUSTERS = (By.CSS_SELECTOR, ".app-contents table tbody tr")
CLUSTER_NAME_LABEL = ".table-avatar-label"
SORT_CLUSTERS_BUTTON = (By.CSS_SELECTOR, ".mi-arrow-up-down")
SEARCH_FIELD = (By.CSS_SELECTOR, ".section-header input")
ALERT_LINK = ".cluster-name"
DISCONNECT_ICON = ".table-action_link"
DISCONNECT_WARNING_MESSAGE = (By.XPATH, "//div[@class='modal-header']")
DISCONNECT_BUTTON = (By.XPATH, "//button[@class='btn btn-danger']")
SKIP_CLUSTER_CONFIG_BUTTON = (By.CSS_SELECTOR, ".modal-container.modal-dialog button.btn-primary.btn-flat")


class ClustersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_connect_new_cluster_button(self):
        print("Click 'Connect a new cluster' button")
        self.wait_element_present(CONNECT_NEW_CLUSTER).click()
        return ConnectClusterPage(self.driver)

    def open_cluster_details(self, name, status):
        print("Open cluster '%s' details" % name)
        is_exists = False
        self.wait_element_visible(SORT_CLUSTERS_BUTTON)
        my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)

        for my_cluster in my_clusters:
            text = my_cluster.text
            if name in text and status in text:
                is_exists = True
                my_cluster.find_element_by_css_selector(CLUSTER_NAME_LABEL).click()
                self.sleep(10)

                break

        assert is_exists is True, "Cluster is absent"
        try:
            self.wait_element_visible(SKIP_CLUSTER_CONFIG_BUTTON).click()
        except Exception:
            print("Modal dialog is absent")

        return ClusterOverviewPage(self.driver)

    def verify_cluster_present(self, name, status):
        print("Make sure cluster '%s' present" % name)
        is_exists = False
        self.wait_element_visible(SORT_CLUSTERS_BUTTON)
        my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)
        for my_cluster in my_clusters:
            text = my_cluster.text
            if name in text and status in text:
                is_exists = True
                break
        assert is_exists is True, "Cluster is absent"
        return ClustersPage(self.driver)

    def verify_cluster_absent(self, name):
        print("Make sure cluster '%s' absent" % name)
        is_exists = False
        my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)

        for my_cluster in my_clusters:
            text = my_cluster.text
            if name in text:
                is_exists = True
                break
            assert is_exists is False, "Cluster is present"
        return ClustersPage(self.driver)

    def verify_number_of_clusters_equals(self, number):
        print("Make sure number of clusters equals to '%s'" % number)
        self.wait_element_visible(SORT_CLUSTERS_BUTTON)
        my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)
        size = len(my_clusters)

        assert size == number, "Number of clusters is wrong"
        return ClustersPage(self.driver)

    def verify_status_shown_for_each_cluster(self):
        print("Verify status is shown for each cluster")
        self.wait_element_visible(SORT_CLUSTERS_BUTTON)
        my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)

        for cluster in my_clusters:
            status = cluster.find_element_by_css_selector(ALERT_LINK)
            is_displayed = status.is_displayed()
            status_text = status.text
            is_status_correct = "Active" in status_text or "Inactive" in status_text or "Offline" in status_text

            assert is_status_correct is True, "Status text is wrong"
            assert is_displayed is True, "Status is not shown"

        return ClustersPage(self.driver)

    def verify_kub_version_shown_for_active_offline_clusters(self):
        print("Verify K8s version is shown for each cluster")
        try:
            self.wait_element_visible(EMPTY_CARD_CONTAINER)
        except Exception:
            self.wait_element_visible(SORT_CLUSTERS_BUTTON)
            my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)

            for cluster in my_clusters:
                cluster_text = cluster.text
                if("Active" in cluster_text or "Offline" in cluster_text) is True:
                    assert ("v1." in cluster_text) is True, "K8s version is missed"
                else:
                    assert ("v1." in cluster_text) is False, "K8s version is present"

        return ClustersPage(self.driver)

    def verify_delete_text_shown_for_each_disconnect_icon(self):
        print("Verify delete text is shown for each disconnect icon")
        self.wait_element_visible(SORT_CLUSTERS_BUTTON)
        my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)

        for cluster in my_clusters:
            status = cluster.find_element_by_css_selector(DISCONNECT_ICON)
            title = status.get_attribute("tooltip")
            print(title)
            is_title_correct = "Disconnect" in title

            assert is_title_correct is True, "Title text is wrong"

        return ClustersPage(self.driver)

    def click_delete_icon_for_cluster(self, name):
        print("Click 'Delete' icon for '%s' cluster" % name)
        self.wait_element_visible(SORT_CLUSTERS_BUTTON)
        my_clusters = self.wait_elements_visible(AVAILABLE_CLUSTERS)

        for my_cluster in my_clusters:
            text = my_cluster.text
            if name in text:
                my_cluster.find_element_by_css_selector(DISCONNECT_ICON).click()
                break

        return ClustersPage(self.driver)

    def click_disconnect_button_for_cluster(self):
        print("Click 'Disconnect' button to remove cluster")
        self.wait_element_present(DISCONNECT_BUTTON).click()
        self.sleep(10)
        return ClustersPage(self.driver)

    def verify_cluster_delete_warning_message(self):
        print("Warning message to be displayed")
        text = self.wait_element_visible(DISCONNECT_WARNING_MESSAGE).text
        message = "Disconnect cluster"
        is_message_correct = message in text
        assert is_message_correct is True, "Warning message is wrong"
        return ClustersPage(self.driver)

    def enter_cluster_name(self, password):
        print("Enter '%s' into 'Search' field" % password)
        self.wait_element_present(SEARCH_FIELD).send_keys(password)
        return ClustersPage(self.driver)

    def verify_connect_new_cluster_button_invisible(self):
        print("Make sure that 'Connect a new cluster' button invisible")
        self.wait_element_invisible(CONNECT_NEW_CLUSTER)
        return ClustersPage(self.driver)
