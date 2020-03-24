from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage

AVAILABLE_RECORDS = (By.CSS_SELECTOR, "table.table tbody tr")


class NotificationsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_records_present(self):
        print("Make sure records present")
        self.sleep(10)
        volumes = self.wait_elements_visible(AVAILABLE_RECORDS)
        size = len(volumes)

        assert size > 0, "Number of records is wrong"
        return NotificationsPage(self.driver)