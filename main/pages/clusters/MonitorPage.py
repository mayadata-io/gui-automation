from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

SEARCH_FIELD = (By.CSS_SELECTOR, "input[placeholder='Find a volume']")
AVAILABLE_VOLUMES = (By.CSS_SELECTOR, "table.table tr")
METRICS_FRAME = "iframe[src*='openebs_Volume=All']"
DASHBOARD_CONTAINER = (By.CSS_SELECTOR, ".dashboard-container")
GRAPHS_TITLES = (By.CSS_SELECTOR, ".panel-container .panel-title")

IS_EMPTY_PAGE = False


class MonitorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_volumes_present(self):
        print("Make sure volumes records present")
        try:
            if self.is_element_present(EMPTY_CARD_CONTAINER):
                IS_EMPTY_PAGE = True
        except Exception:
            self.wait_element_visible(SEARCH_FIELD)
            volumes = self.wait_elements_visible(AVAILABLE_VOLUMES)
            size = len(volumes)
            assert size > 0, "Number of volumes is wrong"

        return MonitorPage(self.driver)

    def verify_volume_present(self, name, status, cas_type):
        print("Make sure volume '%s' present" % name)
        try:
            self.is_element_present(EMPTY_CARD_CONTAINER)
        except Exception:
            is_exists = False
            self.wait_element_visible(SEARCH_FIELD)
            my_clusters = self.wait_elements_visible(AVAILABLE_VOLUMES)
            for my_cluster in my_clusters:
                text = my_cluster.text
                if name in text and status in text and cas_type in text:
                    is_exists = True
                    break
            assert is_exists is True, "Volume is absent"
        return MonitorPage(self.driver)

    def switch_to_metrics_frame(self):
        print("Switch to 'Metrics' container")
        try:
            self.is_element_present(EMPTY_CARD_CONTAINER)
        except Exception:
            self.sleep(10)
            self.switch_to_frame(METRICS_FRAME)
        return MonitorPage(self.driver)

    def verify_graph_present(self, name):
        print("Make sure graph '%s' present" % name)
        try:
            self.is_element_present(EMPTY_CARD_CONTAINER)
        except Exception:
            is_exists = False
            self.wait_element_visible(DASHBOARD_CONTAINER)
            titles = self.wait_elements_visible(GRAPHS_TITLES)

            for title in titles:
                text = title.text
                if name in text:
                    is_exists = True
                    break

            assert is_exists is True, "Graph is absent"
        return MonitorPage(self.driver)
