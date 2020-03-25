from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

HEADER_TITLE = (By.CSS_SELECTOR, ".table-volume tbody tr")


class PoolsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_pools_page_loaded(self):
        print("Make sure applications records present")
        try:
            self.is_element_present(EMPTY_CARD_CONTAINER)
        except Exception:
            text = self.wait_element_visible(HEADER_TITLE).text
            is_header_correct = "Search Pools" in text
            assert is_header_correct is True, "Pools page is not loaded"

        return PoolsPage(self.driver)
