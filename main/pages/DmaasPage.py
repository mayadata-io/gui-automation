from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage
from main.pages.clusters.applications.DmaasPage import DmaasPage as dmass_schedule

HEADER_TITLE = (By.CSS_SELECTOR, ".section-header_title")
SCHEDULE_LIST = (By.CSS_SELECTOR, "a[href*='/dmaas/schedules/']")
FIND_SCHEDULE_FIELD = (By.XPATH, "//input[@placeholder='Find a Schedule..']")
EMPTY_CARD_CONTAINER = (By.CSS_SELECTOR, ".card_zero_result")


class DmaasPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_header_text_equals(self, header):
        print("Make sure header text equals to '%s'" % header)
        text = self.wait_element_visible(HEADER_TITLE).text
        is_header_correct = header in text
        assert is_header_correct is True, "Header is wrong"
        return DmaasPage(self.driver)

    def open_schedules_page(self):
        print("Click on schedules href")
        self.wait_element_present(SCHEDULE_LIST).click()
        from main.pages.dmaas.SchedulesPage import SchedulesPage
        return SchedulesPage(self.driver)

    def find_schedule(self):
        print("Make sure that schedule '%s' is present" % dmass_schedule.new_schedule_name)
        print(dmass_schedule.new_schedule_name)
        is_exists = False
        try:
            if self.is_element_present(EMPTY_CARD_CONTAINER):
                self.verify_empty_card_container_text_equals("Looks like you do not have any schedules yet")
        except Exception:
            schedules = self.wait_elements_visible(SCHEDULE_LIST)
            for schedule in schedules:
                if dmass_schedule.new_schedule_name in schedule.text:
                    is_exists = True
                    break
        assert is_exists is True, "Schedule is absent"
        return DmaasPage(self.driver)

    def enter_schedule(self):
        print("Enter schedule '%s' in search field" % dmass_schedule.new_schedule_name)
        print(dmass_schedule.new_schedule_name)
        self.wait_element_present(FIND_SCHEDULE_FIELD).send_keys(dmass_schedule.new_schedule_name)
        return DmaasPage(self.driver)
