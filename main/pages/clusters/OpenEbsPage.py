from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

CONTROL_PLANE_TAB = (By.CSS_SELECTOR, "a[href$='/controlplanes']")
POOLS_TAB = (By.CSS_SELECTOR, "a[href$='resources/pools']")
VOLUMES_TAB = (By.CSS_SELECTOR, "a[href*='resources/applications']")
HEADER_TITLE = (By.CSS_SELECTOR, ".section-header_title")
AVAILABLE_RECORDS = (By.CSS_SELECTOR, "table.table tbody tr")

IS_EMPTY_PAGE = False


class OpenEbsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_open_ebs_page(self):
        try:
            if self.is_element_present(EMPTY_CARD_CONTAINER):
                IS_EMPTY_PAGE = True
        except Exception:
            self.click_control_plane_button()
            self.verify_header_text_equals("Control Plane")
            self.verify_records_present()
            self.click_pools_button()
            self.verify_header_text_equals("cStor Pool Clusters (CSPC)")
            self.click_volumes_button()
            self.verify_header_text_equals("Volumes grouped by applications")
            self.verify_records_present()

    def click_control_plane_button(self):
        print("Click 'Control plane' tab")
        self.wait_element_present(CONTROL_PLANE_TAB).click()
        self.sleep(5)

        return OpenEbsPage(self.driver)

    def click_pools_button(self):
        print("Click 'Pools' tab")
        self.wait_element_present(POOLS_TAB).click()
        self.sleep(5)

        return OpenEbsPage(self.driver)

    def click_volumes_button(self):
        print("Click 'Volumes' tab")
        self.wait_element_present(VOLUMES_TAB).click()
        self.sleep(5)

        return OpenEbsPage(self.driver)

    def verify_header_text_equals(self, header):
        print("Make sure header text equals to '%s'" % header)
        text = self.wait_element_visible(HEADER_TITLE).text
        is_header_correct = header in text

        assert is_header_correct is True, "Header is wrong"
        return OpenEbsPage(self.driver)

    def verify_records_present(self):
        print("Make sure records present")
        self.sleep(5)
        volumes = self.wait_elements_visible(AVAILABLE_RECORDS)
        size = len(volumes)

        assert size > 0, "Number of records is wrong"
        return OpenEbsPage(self.driver)
