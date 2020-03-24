from selenium.webdriver.common.by import By

from main.pages.AlertsPage import AlertsPage
from main.pages.BasePage import BasePage

DASHBOARD_CONTENT = (By.CSS_SELECTOR, ".app-contents .outlet-content>div.ember-view")
DASHBOARD_FRAME = "iframe[src*='grafana/d/project-cluster-metric-summary']"
DASHBOARD_CONTAINER = (By.CSS_SELECTOR, ".dashboard-container")
GRAPHS_TITLES = (By.CSS_SELECTOR, ".panel-container .panel-title")
NAVIGATION_ITEMS = (By.CSS_SELECTOR, ".nav-item")
CLUSTER_CARDS = (By.CSS_SELECTOR, ".card-body")
ALERT_LINK = "a[href*='/alerts']"
TEAM_MEMBERS = (By.CSS_SELECTOR, "div[class='content-section'] table tr")


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_graph_container(self):
        print("Switch to 'Graph' container")
        self.sleep(15)
        self.wait_element_visible(DASHBOARD_CONTENT)
        self.switch_to_frame(DASHBOARD_FRAME)
        return DashboardPage(self.driver)

    def verify_graph_present(self, name):
        print("Make sure graph '%s' present" % name)
        is_exists = False
        self.wait_element_visible(DASHBOARD_CONTAINER)
        titles = self.wait_elements_visible(GRAPHS_TITLES)

        for title in titles:
            text = title.text
            if name in text:
                is_exists = True
                break

        assert is_exists is True, "Graph is absent"
        return DashboardPage(self.driver)

    def switch_to_cluster_tab(self, name):
        print("Switch to '%s' clusters tab" % name)
        is_exists = False
        self.wait_element_visible(DASHBOARD_CONTENT)
        items = self.wait_elements_visible(NAVIGATION_ITEMS)

        for item in items:
            text = item.text
            if name in text:
                is_exists = True
                item.click()
                break

        assert is_exists is True, "Cluster tab is absent"
        return DashboardPage(self.driver)

    def verify_cluster_present(self, name):
        print("Make sure cluster '%s' present" % name)
        is_exists = False
        self.wait_element_visible(DASHBOARD_CONTENT)
        cards = self.wait_elements_visible(CLUSTER_CARDS)
        for card in cards:
            text = card.text
            if name in text:
                is_exists = True
                break

        assert is_exists is True, "Cluster is absent"
        return DashboardPage(self.driver)

    def open_alert_for_cluster(self, name):
        print("Open 'Alert' page for cluster '%s'" % name)
        self.wait_element_visible(DASHBOARD_CONTENT)
        cards = self.wait_elements_visible(CLUSTER_CARDS)
        for card in cards:
            text = card.text
            if name in text:
                card.find_element_by_css_selector(ALERT_LINK).click()
                self.sleep(10)
                break

        return AlertsPage(self.driver)

    def verify_clusters_inactive(self):
        print("Make sure all clusters are inactive")
        self.wait_element_visible(DASHBOARD_CONTENT)
        cards = self.wait_elements_visible(CLUSTER_CARDS)
        for card in cards:
            text = card.text
            is_inactive = "Inactive" in text or "Offline" in text
            assert is_inactive is True, "Cluster is active"

        return DashboardPage(self.driver)

    def verify_team_member_present(self, name, role):
        print("Make sure team member '%s' present" % name)
        is_exists = False
        self.wait_element_visible(DASHBOARD_CONTENT)
        titles = self.wait_elements_visible(TEAM_MEMBERS)

        for title in titles:
            text = title.text
            if name in text and role in text:
                is_exists = True
                break

        assert is_exists is True, "Team member is absent"
        return DashboardPage(self.driver)
