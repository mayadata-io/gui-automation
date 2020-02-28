import allure

from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
from main.pages.SidePanel import SidePanel

DIRECTOR_ONLINE_BUTTON = (By.CSS_SELECTOR, "a[href='https://director.mayadata.io']")


class PortalHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click 'Go to Director Online' button")
    def click_goto_director_online_button(self):
        self.wait_element_present(DIRECTOR_ONLINE_BUTTON).click()
        return SidePanel(self.driver)

    @allure.step("Opn 'Director Online' page")
    def open_director_online_page(self):
        self.wait_element_present(DIRECTOR_ONLINE_BUTTON)
        href = self.wait_element_visible(DIRECTOR_ONLINE_BUTTON).get_attribute('href')
        self.navigate_to(href)
        return SidePanel(self.driver)
