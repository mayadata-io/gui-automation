from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

OUTLET_HEADER = (By.XPATH, "//div[@class='outlet-header__top-bar-title']//span[contains(text(),'Restore')]")
RESTORE_COMPLETED = (By.XPATH, "//span[@class='h5 font-weight-bold'][text()='Restore Completed']")
OUTLET_NAVIGATION_BUTTON = (By.XPATH, "//button[@class='outlet-header-navigation_button']")


class ActivityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_restore_status(self):
        print("Make sure that that restore is success")
        self.wait_element_visible(OUTLET_HEADER)
        return ActivityPage(self.driver)

    def open_schedules_page(self):
        print("click on navigation button to switch to schedules page")
        self.wait_element_present(OUTLET_NAVIGATION_BUTTON).click()
        from main.pages.dmaas.SchedulesPage import SchedulesPage
        return SchedulesPage(self.driver)
