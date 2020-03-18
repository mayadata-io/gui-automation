from selenium.webdriver.common.by import By

from main.pages.BasePage import BasePage

SEARCH_FIELD = (By.CSS_SELECTOR, ".input-search")
AVAILABLE_VOLUMES = (By.CSS_SELECTOR, "table.table-volume tbody tr")


class VolumesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_volumes_present(self):
        print("Make sure volumes records present")
        self.wait_element_visible(SEARCH_FIELD)
        volumes = self.wait_elements_visible(AVAILABLE_VOLUMES)
        size = len(volumes)

        assert size > 0, "Number of volumes is wrong"
        return VolumesPage(self.driver)

    def verify_volume_present(self, name, status, cas_type, storage_class):
        print("Make sure volume '%s' present" % name)
        is_exists = False
        self.wait_element_visible(SEARCH_FIELD)
        my_clusters = self.wait_elements_visible(AVAILABLE_VOLUMES)
        for my_cluster in my_clusters:
            text = my_cluster.text
            if name in text and status in text and cas_type in text and storage_class in text:
                is_exists = True
                break
        assert is_exists is True, "Volume is absent"
        return VolumesPage(self.driver)
