from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

HEADER_BAR = (By.CSS_SELECTOR, ".outlet-header-bar")
VOLUMES_BUTTON = (By.CSS_SELECTOR, "a[href*='/applications/'][href*='/volumes']")
DMAAS_BUTTON = (By.CSS_SELECTOR, "a[href*='/applications/'][href*='/dmaas']")
ANALYTICS_BUTTON = (By.CSS_SELECTOR, "a[href*='/applications/'][href*='/monitor']")
AVAILABLE_VOLUMES = (By.CSS_SELECTOR, ".table.table-hover tr")


class VolumesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_application_type(self, application_name, application_type):
        print("Make sure that application type is '%s'" % application_type)
        text = self.wait_element_visible(HEADER_BAR).text
        print(text)
        is_exists = False
        if application_name in text and application_type in text:
            is_exists = True
        assert is_exists is True, "Application type is wrong"
        return VolumesPage(self.driver)

    def verify_volume_cas_type(self, volume_name, volume_type):
        print("Make sure that application CAS type is '%s'" % volume_type)
        volumes = self.wait_elements_visible(AVAILABLE_VOLUMES)
        is_exist = False
        for volume in volumes:
            text = volume.text
            if volume_name in text and volume_type in text:
                is_exist = True
                break
        assert is_exist is True, "Volume type is wrong"
        return VolumesPage(self.driver)

    def click_dmass_button(self):
        print("Click 'Dmaas' button")
        self.wait_element_present(DMAAS_BUTTON).click()
        from main.pages.clusters.applications.DmaasPage import DmaasPage
        return DmaasPage(self.driver)


