from selenium.webdriver.common.by import By

from main.pages.BasePage import EMPTY_CARD_CONTAINER
from main.pages.SidePanel import SidePanel

COMPONENT_SEARCH_FIELD = (By.CSS_SELECTOR, ".input-search-icon_wrapper")
GRAFANA_APP = (By.CSS_SELECTOR, ".grafana-app")
DASHBOARD_FRAME = "iframe[src*='grafana/d/cluster-volume-metric-summary']"
ANALYTIC_GRAPHS = (By.CSS_SELECTOR, ".react-grid-item.panel.react-draggable")
GRAPH_PANEL = "div[class*='__chart']"
GRAPH_LEGEND = "div[class*='-legend']"
POOLS_CARDS = (By.CSS_SELECTOR, ".card.col")
CLUSTER_OVERVIEW_RECORDS = (By.CSS_SELECTOR, ".cluster-overview-table tr")

IS_EMPTY_PAGE = False


class ClusterOverviewPage(SidePanel):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_graph_container(self):
        print("Switch to 'Graph' container")
        self.sleep(5)
        try:
            if self.wait_element_visible(EMPTY_CARD_CONTAINER):
                self.verify_empty_card_container_text_equals("Looks like OpenEBS is not installed in this Cluster.")

        except Exception:
            frame_by = (By.CSS_SELECTOR, DASHBOARD_FRAME)
            self.wait_element_visible(frame_by)
            self.sleep(10)
            self.switch_to_frame(DASHBOARD_FRAME)

        return ClusterOverviewPage(self.driver)

    def verify_graph_present(self, name):
        print("Make sure graph '%s' present" % name)
        try:
            self.is_element_present(EMPTY_CARD_CONTAINER)

        except Exception:
            self.wait_element_visible(GRAFANA_APP)
            graphs = self.wait_elements_visible(ANALYTIC_GRAPHS)

            for graph in graphs:
                text = graph.text
                if name in text:
                    is_exists = True
                    is_graph_displayed = graph.find_element_by_css_selector(GRAPH_PANEL).is_displayed()
                    is_graph_legend_displayed = graph.find_element_by_css_selector(GRAPH_LEGEND).is_displayed()

                    assert is_exists is True, "Graph is absent"
                    assert is_graph_displayed is True, "Graph content is absent"
                    assert is_graph_legend_displayed is True, "Graph legend is absent"
                    break

        return ClusterOverviewPage(self.driver)

    def verify_pool_card_present(self, name):
        print("Make sure pool card '%s' present" % name)
        is_exists = False
        self.wait_element_visible(COMPONENT_SEARCH_FIELD)
        titles = self.wait_elements_visible(POOLS_CARDS)

        for title in titles:
            text = title.text
            if name in text:
                is_exists = True
                break

        assert is_exists is True, "Pool card is absent"
        return ClusterOverviewPage(self.driver)

    def verify_cluster_overview_info_present(self):
        print("Make sure cluster overview records present")
        self.wait_element_visible(COMPONENT_SEARCH_FIELD)
        clusters = self.wait_elements_visible(CLUSTER_OVERVIEW_RECORDS)
        size = len(clusters)

        assert size > 1, "Number of clusters is wrong"
        return ClusterOverviewPage(self.driver)
