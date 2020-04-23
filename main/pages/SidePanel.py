from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
from main.pages.UserProfilePage import UserProfilePage
from main.pages.InvitationsPage import InvitationsPage

PROJECT_LINK = (By.CSS_SELECTOR, ".sidebar-project-icon")
MANAGE_PROJECTS_LINK = (By.CSS_SELECTOR, "a[href='/projects']")
DASHBOARD_LINK = (By.CSS_SELECTOR, "a[href='/dashboard']")
CLUSTERS_LINK = (By.CSS_SELECTOR, "a[href='/clusters']")
MONITORING_LINK = (By.CSS_SELECTOR, "a[href='/monitor']")
USER_ROLES_LINK = (By.CSS_SELECTOR, "a[href='/settings/team/members']")
USER_PROFILE_ITEM = (By.CSS_SELECTOR, ".sidebar-links img[src*='https://ui-avatars.com']")
PROFILE_LINK = (By.CSS_SELECTOR, "a[href='/settings/profile']")
INVITES_LINK = (By.CSS_SELECTOR, "a[href='/invitations']")
LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")
APPLICATIONS_LINK = (By.CSS_SELECTOR, "a[href*='/applications']")
POOLS_LINK = (By.CSS_SELECTOR, "a[href*='/pools']")
VOLUMES_LINK = (By.CSS_SELECTOR, "a[href*='/volumes']")
TOPOLOGY_LINK = (By.CSS_SELECTOR, "a[href*='/viewtopology']")
MONITOR_LINK = (By.CSS_SELECTOR, "a[href*='/monitor']")
LOGS_LINK = (By.CSS_SELECTOR, "a[href$='/logging']")
CLUSTER_ALERTS_LINK = (By.CSS_SELECTOR, "a[href$='/alerts']")
OPEN_EBS_LINK = (By.CSS_SELECTOR, "a[href$='/openebs']")
DMAAS_LINK = (By.CSS_SELECTOR, "a[href='/dmaas']")
CLUSTER_MONITOR_LINK = (By.CSS_SELECTOR, "a[href*='/clusters/'][href*='/monitor']")


class SidePanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_dashboard_page(self):
        print("Open 'Dashboard' page")
        self.wait_element_present(DASHBOARD_LINK).click()
        self.sleep(15)
        from main.pages.DashboardPage import DashboardPage
        return DashboardPage(self.driver)

    def open_projects_page(self):
        print("Open 'Projects' page")
        self.wait_element_present(PROJECT_LINK).click()
        self.wait_element_present(MANAGE_PROJECTS_LINK).click()
        self.sleep(5)
        from main.pages.ProjectsPage import ProjectsPage
        return ProjectsPage(self.driver)

    def open_applications_page(self):
        print("Open 'Applications' page")
        self.wait_element_present(APPLICATIONS_LINK).click()
        from main.pages.clusters.ApplicationsPage import ApplicationsPage
        return ApplicationsPage(self.driver)

    def open_pools_page(self):
        print("Open 'Pools' page")
        self.wait_element_present(POOLS_LINK).click()
        from main.pages.clusters.PoolsPage import PoolsPage
        return PoolsPage(self.driver)

    def open_volumes_page(self):
        print("Open 'Volumes' page")
        self.wait_element_present(VOLUMES_LINK).click()
        self.sleep(3)
        from main.pages.clusters.VolumesPage import VolumesPage
        return VolumesPage(self.driver)

    def open_topology_page(self):
        print("Open 'Topology' page")
        self.wait_element_present(TOPOLOGY_LINK).click()
        from main.pages.clusters.TopologyPage import TopologyPage
        return TopologyPage(self.driver)

    def open_monitor_page(self):
        print("Open 'Monitor' page")
        self.wait_element_present(CLUSTER_MONITOR_LINK).click()
        from main.pages.clusters.MonitorPage import MonitorPage
        return MonitorPage(self.driver)

    def open_logs_page(self):
        print("Open 'Logs' page")
        try:
            from main.pages.clusters.ClustersPage import SKIP_CLUSTER_CONFIG_BUTTON
            self.wait_element_visible(SKIP_CLUSTER_CONFIG_BUTTON).click()
        except Exception:
            print("Modal dialog is absent")

        self.wait_element_present(LOGS_LINK).click()
        from main.pages.clusters.LogsPage import LogsPage
        return LogsPage(self.driver)

    def open_alerts_page(self):
        print("Open 'Alerts' page")
        self.wait_element_present(CLUSTER_ALERTS_LINK).click()
        from main.pages.clusters.AlertsPage import AlertsPage
        return AlertsPage(self.driver)

    def open_ebs_page(self):
        print("Open 'OpenEbs' page")
        self.wait_element_present(OPEN_EBS_LINK).click()
        from main.pages.clusters.OpenEbsPage import OpenEbsPage
        return OpenEbsPage(self.driver)

    def open_clusters_page(self):
        print("Open 'Clusters' page")
        self.wait_element_present(CLUSTERS_LINK).click()
        from main.pages.clusters.ClustersPage import ClustersPage
        return ClustersPage(self.driver)

    def open_dmaas_page(self):
        print("Open 'Dmaas' page")
        self.wait_element_present(DMAAS_LINK).click()
        from main.pages.DmaasPage import DmaasPage
        return DmaasPage(self.driver)

    def open_cross_cloud_monitoring_page(self):
        print("Open 'Cross Cloud Monitoring' page")
        self.wait_element_present(MONITORING_LINK).click()
        from main.pages.MonitoringPage import MonitoringPage
        return MonitoringPage(self.driver)

    def open_user_roles_page(self):
        print("Open 'User and Roles' page")
        self.wait_element_present(USER_ROLES_LINK).click()
        from main.pages.UserRolesPage import UserRolesPage
        return UserRolesPage(self.driver)

    def verify_user_profile_item_present(self):
        print("Make sure 'User profile' side panel link present")
        self.wait_element_present(USER_PROFILE_ITEM)
        return SidePanel(self.driver)

    def open_user_profile_page(self):
        print("Open 'User profile' page")
        self.wait_element_present(USER_PROFILE_ITEM).click()
        self.wait_element_present(PROFILE_LINK).click()
        self.sleep(10)
        return UserProfilePage(self.driver)

    def open_invitations_page(self):
        print("Open 'Invitations' page")
        self.wait_element_present(USER_PROFILE_ITEM).click()
        self.wait_element_present(INVITES_LINK).click()
        self.sleep(5)
        return InvitationsPage(self.driver)

    def logout(self):
        print("Logout")
        self.wait_element_present(USER_PROFILE_ITEM).click()
        self.wait_element_present(LOGOUT_LINK).click()
        from main.pages.LoginPage import LoginPage
        return LoginPage(self.driver)
