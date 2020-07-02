from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage
from main.pages.clusters.applications.DmaasPage import DmaasPage as dmass_schedule

HEADER_TITLE = (By.CSS_SELECTOR, ".section-header_title")
SCHEDULE_LIST = (By.CSS_SELECTOR, "a[href*='/dmaas/schedules/']")
FIND_SCHEDULE_FIELD = (By.XPATH, "//input[@placeholder='Find a Schedule..']")
EMPTY_CARD_CONTAINER = (By.CSS_SELECTOR, ".card_zero_result")
SCHEDULES = (By.CSS_SELECTOR, ".app-contents table tbody tr")
SCHEDULE = "a[href*='/dmaas/schedules/']"
DELETE_ICON = (By.CSS_SELECTOR, ".mi.mi-trash.mi-1x")
DELETE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-danger")
NO_SCHEDULE_MESSAGE = (By.CSS_SELECTOR, ".text-center.pt-2")
RIGHT_NAVIGATION_ICON = (By.CSS_SELECTOR, ".mi.mi-chevron-right")


class DmaasPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_header_text_equals(self, header):
        print("Make sure header text equals to '%s'" % header)
        self.sleep(5)
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
        self.wait_element_present(FIND_SCHEDULE_FIELD).send_keys(dmass_schedule.new_schedule_name)
        return DmaasPage(self.driver)

    # Search schedule
    def search_schedule(self, name):
        print("Enter schedule '%s' in search field" % name)
        self.wait_element_present(FIND_SCHEDULE_FIELD).send_keys(name)
        self.sleep(5)
        return DmaasPage(self.driver)

    # Delete schedule
    def remove_schedule(self):
        print("Delete schedule")
        self.wait_element_present(DELETE_ICON).click()
        print("delete icon click")
        self.sleep(3)
        self.wait_element_present(DELETE_BUTTON).click()
        self.sleep(5)
        return DmaasPage(self.driver)

    # Verify schedule absent after deletion
    def verify_schedule_absent(self, name):
        print("Make sure that schedule '%s' is absent" % name)
        message = "We Couldn't find any resource"
        is_exists = False
        try:
            text = self.wait_element_visible(NO_SCHEDULE_MESSAGE).text
            if message in text:
                is_exists = True
        except Exception:
            pass
        assert is_exists is True, "Schedule is present"
        return DmaasPage(self.driver)

    # Delete dmaas schedules
    def delete_dmaas_schedules(self, name, namespace):
        print("Delete schedules '%s'" % name)
        try:
            if self.is_element_present(EMPTY_CARD_CONTAINER):
                self.verify_empty_card_container_text_equals("Looks like you do not have any schedules yet")
        except Exception:
            is_exists = False
            self.wait_element_visible(HEADER_TITLE)
            schedules_list = []
            # Capturing all schedule name to be deleted in a list
            while self.is_element_present(SCHEDULES):
                schedules = self.wait_elements_visible(SCHEDULES)
                for schedule in schedules:
                    text = schedule.text
                    if name in text and namespace in text:
                        is_exists = True
                        schedule_name = schedule.find_element_by_css_selector(SCHEDULE).text
                        schedules_list.append(schedule_name)
                try:
                    self.wait_element_present(RIGHT_NAVIGATION_ICON).click()
                except Exception:
                    break

            # For loop to delete schedules in above list
            for name in schedules_list:
                print("Deleting Schedule: '%s'" % name)
                self.driver.refresh()
                self.search_schedule(name)
                self.remove_schedule()
                self.driver.refresh()
        return DmaasPage(self.driver)


