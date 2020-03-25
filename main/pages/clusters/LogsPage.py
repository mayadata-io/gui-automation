from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

LOGS_FRAME = "iframe[src*='/kibana/app/kibana?projectid']"
LOADING_MESSAGE = (By.ID, "kbn_loading_message")
LOGS_DIAGRAM = (By.CSS_SELECTOR, "#kibana-body .app-wrapper")


class LogsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_logs_frame(self):
        print("Switch to 'Logs' container")
        self.sleep(10)
        self.switch_to_frame(LOGS_FRAME)
        self.wait_element_invisible(LOADING_MESSAGE)
        return LogsPage(self.driver)

    def verify_logs_diagram_present(self):
        print("Make sure 'Logs' diagram present")
        try:
            self.is_element_present(EMPTY_CARD_CONTAINER)
        except Exception:
            self.switch_to_logs_frame()
            self.wait_element_present(LOGS_DIAGRAM)

        return LogsPage(self.driver)
