from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

RESTORE_HEADER_TITLE = (By.XPATH, "//span[contains(text(),'List of restores')]")
RESTORE_PAGE_LINK = (By.CSS_SELECTOR, "a[href*='/dmaas/restores/'][href*='/activity']")
RESTORE_LIST = (By.XPATH, "//table[@class='table']//tbody")


class SchedulesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_restore_activity_page(self):
        print("Click on restore link")
        self.sleep(15)
        self.wait_element_visible(RESTORE_HEADER_TITLE)
        self.wait_element_present(RESTORE_PAGE_LINK).click()
        from main.pages.dmaas.restores.ActivityPage import ActivityPage
        return ActivityPage(self.driver)

    def verify_restore_status(self, status):
        print("Make sure that status of restore is '%s'" % status)
        self.sleep(10)
        text = self.wait_element_visible(RESTORE_LIST).text
        print(text)
        is_exists = False
        count = 1
        while count > 0:
            if status in text:
                is_exists = True
                break
            else:
                count = count + 1
                text = self.wait_element_visible(RESTORE_LIST).text
        assert is_exists is True, "Status of backup is not completed"
        return SchedulesPage(self.driver)


