from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

VIEW_ORDER_BUTTON = (By.XPATH, "//span[contains(text(), 'Alert period')]/following-sibling::button")


class AlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_view_order_button_present(self):
        print("Make sure 'View order' button present")
        self.wait_element_present(VIEW_ORDER_BUTTON)
        return AlertsPage(self.driver)