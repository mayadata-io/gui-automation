from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage

DASHBOARD_FRAME = "iframe[src*='grafana/d/cluster-volumes-dashboard']"
GRAFANA_APP = (By.CSS_SELECTOR, ".grafana-app")
ANALYTIC_GRAPHS = (By.CSS_SELECTOR, ".react-grid-item.panel.react-draggable")
GRAPH_PANEL = "div[class*='__chart']"


class MonitoringPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_graph_container(self):
        print("Switch to 'Graph' container")
        frame_by = (By.CSS_SELECTOR, DASHBOARD_FRAME)
        self.wait_element_visible(frame_by)
        self.sleep(15)
        self.switch_to_frame(DASHBOARD_FRAME)
        return MonitoringPage(self.driver)

    def verify_graph_present(self, name):
        print("Make sure graph '%s' present" % name)
        self.wait_element_visible(GRAFANA_APP)
        graphs = self.wait_elements_visible(ANALYTIC_GRAPHS)

        for graph in graphs:
            text = graph.text
            if name in text:
                is_exists = True
                is_graph_displayed = graph.find_element_by_css_selector(GRAPH_PANEL).is_displayed()

                assert is_exists is True, "Graph is absent"
                assert is_graph_displayed is True, "Graph content is absent"
                break

        return MonitoringPage(self.driver)
