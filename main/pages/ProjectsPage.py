import allure

from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

AVAILABLE_PROJECTS = (By.CSS_SELECTOR, ".app-contents table tbody tr")


class ProjectsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Make sure 'Project' with name '{1}' and role '{2}' present")
    def verify_project_present(self, name, role):
        is_exists = False
        my_projects = self.wait_elements_visible(AVAILABLE_PROJECTS)

        for my_project in my_projects:
            text = my_project.text
            if name in text and role in text:
                is_exists = True
                break

        assert is_exists is True, "Project is absent"
