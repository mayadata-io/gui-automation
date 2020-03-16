from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
from main.pages.UserProfilePage import UserProfilePage

PROJECT_LINK = (By.CSS_SELECTOR, ".sidebar-header-item-project_name")
DASHBOARD_LINK = (By.CSS_SELECTOR, "a[href='/dashboard']")
PROJECTS_LINK = (By.CSS_SELECTOR, "a[href='/projects']")
CLUSTERS_LINK = (By.CSS_SELECTOR, "a[href='/clusters']")
USER_ROLES_LINK = (By.CSS_SELECTOR, "a[href='/settings/team/members']")
USER_PROFILE_ITEM = (By.CSS_SELECTOR, ".sidebar-links img[src*='https://ui-avatars.com']")
PROFILE_LINK = (By.CSS_SELECTOR, "a[href='/settings/profile']")
LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")
APPLICATIONS_LINK = (By.CSS_SELECTOR, "a[href*='/applications']")


class SidePanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_dashboard_page(self):
        print("Open 'Dashboard' page")
        self.wait_element_present(DASHBOARD_LINK).click()
        from main.pages.DashboardPage import DashboardPage
        return DashboardPage(self.driver)

    def open_projects_page(self):
        print("Open 'Project' page")
        self.wait_element_present(PROJECTS_LINK).click()
        from main.pages.ProjectsPage import ProjectsPage
        return ProjectsPage(self.driver)

    def open_applications_page(self):
        print("Open 'Applications' page")
        self.wait_element_present(APPLICATIONS_LINK).click()
        from main.pages.clusters.ApplicationsPage import ApplicationsPage
        return ApplicationsPage(self.driver)

    def open_clusters_page(self):
        print("Open 'Clusters' page")
        self.wait_element_present(CLUSTERS_LINK).click()
        from main.pages.clusters.ClustersPage import ClustersPage
        return ClustersPage(self.driver)

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
        return UserProfilePage(self.driver)

    def logout(self):
        print("Logout")
        self.wait_element_present(USER_PROFILE_ITEM).click()
        self.wait_element_present(LOGOUT_LINK).click()
        from main.pages.LoginPage import LoginPage
        return LoginPage(self.driver)
