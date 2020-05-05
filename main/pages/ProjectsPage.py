from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage

AVAILABLE_PROJECTS = (By.CSS_SELECTOR, ".app-contents table tbody tr")
OUTLET_HEADER = (By.CSS_SELECTOR, ".outlet-header__top-bar")
PROJECT_NAME = ".text-hyperlink"
EDIT_ICON = ".mi.mi-edit.mi-1x"


class ProjectsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_project_present(self, project_name, role, invited_by):
        print("Make sure that project '%s' is present" % project_name)
        self.sleep(5)
        is_exists = False
        self.wait_element_visible(OUTLET_HEADER)
        projects = self.wait_elements_visible(AVAILABLE_PROJECTS)

        for project in projects:
            text = project.text
            if project_name in text and role in text and invited_by in text:
                is_exists = True
                #self.sleep(10)
                break

        assert is_exists is True, "Project is absent"
        from main.pages.SidePanel import SidePanel
        return SidePanel(self.driver)

    def select_project(self, name):
        print("Click on project '%s'" % name)
        self.sleep(5)
        is_exists = False
        self.wait_element_visible(OUTLET_HEADER)
        projects = self.wait_elements_visible(AVAILABLE_PROJECTS)

        for project in projects:
            text = project.find_element_by_css_selector(PROJECT_NAME).text
            print(text)
            if name == text:
                is_exists = True
                project.find_element_by_css_selector(PROJECT_NAME).click()
                # self.sleep(10)
                break
        assert is_exists is True, "Project is absent"
        from main.pages.SidePanel import SidePanel
        return SidePanel(self.driver)

    def verify_edit_icon_visible(self, name):
        print("Make sure that project edit icon visible")
        is_exists = False
        is_visible = False
        self.wait_element_visible(OUTLET_HEADER)
        projects = self.wait_elements_visible(AVAILABLE_PROJECTS)

        for project in projects:
            text = project.find_element_by_css_selector(PROJECT_NAME).text
            if name == text:
                is_exists = True
                try:
                    project.find_element_by_css_selector(EDIT_ICON)
                    is_visible = True
                except Exception:
                    is_visible = False
                # self.sleep(10)
                break
        assert is_exists is True, "Project is absent"
        assert is_visible is True, "Edit icon is invisible"
        return ProjectsPage(self.driver)

    def verify_edit_icon_invisible(self, name):
        print("Make sure that project edit icon invisible")
        is_exists = False
        is_visible = False
        self.wait_element_visible(OUTLET_HEADER)
        projects = self.wait_elements_visible(AVAILABLE_PROJECTS)

        for project in projects:
            try:
                text = project.find_element_by_css_selector(PROJECT_NAME).text
                if name == text:
                    is_exists = True
                    try:
                        project.find_element_by_css_selector(EDIT_ICON)
                        is_visible = False
                    except Exception:
                        is_visible = True
                    # self.sleep(10)
                    break
            except Exception:
                print("Project name is not click able")
                text = project.text
                name = name + " "
                if name in text:
                    is_exists = True
                try:
                    project.find_element_by_css_selector(EDIT_ICON)
                    is_visible = False
                except Exception:
                    is_visible = True

        assert is_exists is True, "Project is absent"
        assert is_visible is True, "Edit icon is visible"
        return ProjectsPage(self.driver)

    def verify_project_not_click_able(self, name):
        print("Make sure that project '%s' is not click able" % name)
        is_exists = False
        projects = self.wait_elements_visible(AVAILABLE_PROJECTS)
        for project in projects:
            try:
                project.find_element_by_css_selector(PROJECT_NAME)
                is_exists = False
            except Exception:
                print("Project name is not click able")
                text = project.text
                name = name + " "
                if name in text:
                    is_exists = True
        assert is_exists is True, "Project is absent"
        return ProjectsPage(self.driver)