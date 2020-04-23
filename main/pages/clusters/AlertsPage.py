from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

# VIEW_ORDER_BUTTON = (By.XPATH, "//span[contains(text(), 'Alert period')]/following-sibling::button")
VIEW_ORDER_BUTTON = (By.XPATH, "//span[contains(text(), 'Time period')]/following-sibling::button")
AVAILABLE_ALERTS = (By.CSS_SELECTOR, "table.table tbody tr")
ALERTS_CHECKBOX = (By.XPATH, "//div[@class='custom-control custom-checkbox']")
ACKNOWLEDGE_BUTTON = (By.XPATH, "//a[@class='btn-icon table-action_link']")


class AlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_alerts_present(self):
        print("Make sure alerts present")
        self.wait_element_visible(VIEW_ORDER_BUTTON)

        try:
            if self.is_element_present(EMPTY_CARD_CONTAINER):
                self.verify_empty_card_container_text_equals("No new alerts yet!")
        except Exception:
            volumes = self.wait_elements_visible(AVAILABLE_ALERTS)
            size = len(volumes)
            assert size > 0, "Number of alerts is wrong"

        return AlertsPage(self.driver)

    def acknowledge_alert(self):
        print("Make sure alerts present")
        self.wait_element_visible(VIEW_ORDER_BUTTON)
        try:
            if self.is_element_present(EMPTY_CARD_CONTAINER):
                self.verify_empty_card_container_text_equals("No new alerts yet!")
        except Exception:
            alerts = self.wait_elements_visible(AVAILABLE_ALERTS)
            size = len(alerts)
            assert size > 0, "Number of alerts is wrong"
            self.wait_element_present(ALERTS_CHECKBOX).click()
            self.wait_element_present(ACKNOWLEDGE_BUTTON).click()

        return AlertsPage(self.driver)