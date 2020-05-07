from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

VOLUME_TITLE = (By.XPATH, "//span[contains(text(),'Volume information')]")
REFRESH_BUTTON = (By.CSS_SELECTOR, "button.btn.navbar-button.navbar-button--refresh")
VOLUME_INFO = (By.ID, "volume-info")
DASHBOARD_CONTAINER = (By.CSS_SELECTOR, ".dashboard-container")
GRAPHS_TITLES = (By.CSS_SELECTOR, ".panel-container .panel-title")
REPORT_BUTTON = (By.CSS_SELECTOR, "a[href*='/reporter/']")


class VolumeTiledViewDashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_volume_tiled_view_dashboard_page(self):
        print("Open Volume tiled view dashboard page")
        # print(self.driver.current_url)
        self.driver.switch_to_window(self.driver.window_handles[1])
        return VolumeTiledViewDashboardPage(self.driver)

    def verify_title_text_present(self, title):
        print("Make sure title '%s' is visible" % title)
        self.driver.implicitly_wait(30)
        self.wait_elements_visible(VOLUME_TITLE)
        return VolumeTiledViewDashboardPage(self.driver)

    def verify_volume_info(self, pvc_name, cluster_name, replicas_count):
        print("Verify volume info for '%s' cluster" % cluster_name)
        try:
            self.is_element_present(EMPTY_CARD_CONTAINER)
        except Exception:
            is_exists = False
            self.wait_element_visible(VOLUME_TITLE)
            text = self.wait_element_present(VOLUME_INFO).text
            if pvc_name in text and cluster_name in text and replicas_count in text:
                is_exists = True
            assert is_exists is True, "Volume Info are wrong"
        return VolumeTiledViewDashboardPage(self.driver)

    def verify_graph_present(self, name):
        print("Make sure graph '%s' present" % name)
        is_exists = False
        self.wait_element_visible(DASHBOARD_CONTAINER)
        titles = self.wait_elements_visible(GRAPHS_TITLES)

        for title in titles:
            text = title.text
            if name in text:
                is_exists = True
                break

        assert is_exists is True, "Graph is absent"
        return VolumeTiledViewDashboardPage(self.driver)

    def click_report_button(self):
        print("Click 'report' button to generate report")
        self.wait_element_present(REPORT_BUTTON).click()
        return VolumeTiledViewDashboardPage(self.driver)

    def verify_file_download_button_url(self, cluster,  volume):
        print("Make sure report file volume-tiled-view-dashboard downloaded")
        self.driver.switch_to_window(self.driver.window_handles[2])
        is_exists = False
        url = self.driver.current_url
        if cluster in url and volume in url:
            is_exists = True
        assert is_exists is True, "Report download failed"
        return VolumeTiledViewDashboardPage(self.driver)
