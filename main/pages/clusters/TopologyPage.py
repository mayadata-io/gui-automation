from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage

TOPOLOGY_FRAME = "iframe[src*='volumes']"
CONNECTIVITY_DIAGRAM = (By.CSS_SELECTOR, ".nodes-chart-elements")


class TopologyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_topology_container(self):
        print("Switch to 'Topology' container")
        self.sleep(10)
        self.switch_to_frame(TOPOLOGY_FRAME)
        return TopologyPage(self.driver)

    def verify_connectivity_diagram_present(self):
        print("Make sure 'Connectivity' diagram present")
        self.wait_element_present(CONNECTIVITY_DIAGRAM)
        return TopologyPage(self.driver)
