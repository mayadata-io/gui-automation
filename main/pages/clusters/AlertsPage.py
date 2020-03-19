from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

VIEW_ORDER_BUTTON = (By.XPATH, "//span[contains(text(), 'Alert period')]/following-sibling::button")
AVAILABLE_ALERTS = (By.CSS_SELECTOR, "table.table tbody tr")


class AlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_alerts_present(self):
        print("Make sure alerts present")
        self.wait_element_visible(VIEW_ORDER_BUTTON)
        volumes = self.wait_elements_visible(AVAILABLE_ALERTS)
        size = len(volumes)

        assert size > 0, "Number of alerts is wrong"
        return AlertsPage(self.driver)