from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage

HEADER_TITLE = (By.CSS_SELECTOR, ".section-header_title")


class DmaasPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_header_text_equals(self, header):
        print("Make sure header text equals to '%s'" % header)
        text = self.wait_element_visible(HEADER_TITLE).text
        is_header_correct = header in text

        assert is_header_correct is True, "Header is wrong"
        return DmaasPage(self.driver)