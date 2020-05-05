from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

SELECT_CLUSTER = (By.XPATH, "//select[@id='cluster-select']")
START_RESTORE_BUTTON = (By.XPATH, "//input[@value='Start restore']")
MODAL_HEADER_TITLE = (By.XPATH, "//h5[@class='modal-title']")
MODAL_CLOSE_ICON = (By.XPATH, "//span[@class='mi mi-x mi-1x float-right text-white']")
RESTORE_LINK = (By.XPATH, "//span[@class='text-hyperlink'][contains(text(),'Restore')]")


class RestorePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_restore_cluster(self, name):
        print("Select Restore cluster '%s'" % name)
        select = self.wait_element_present(SELECT_CLUSTER)
        for option in select.find_elements_by_tag_name('option'):
            if name in option.text:
                option.click()
                break
        return RestorePage(self.driver)

    def click_start_restore_button(self):
        print("Click on Start restore button")
        self.wait_element_present(START_RESTORE_BUTTON).click()
        self.sleep(5)
        return RestorePage(self.driver)

    def close_restore_modal_popup(self):
        print("Click on close button on popup")
        self.sleep(5)
        self.wait_element_visible(MODAL_HEADER_TITLE)
        self.wait_element_present(MODAL_CLOSE_ICON).click()
        from main.pages.SidePanel import SidePanel
        return SidePanel(self.driver)

    def click_restore_link(self):
        print("Click on Restore link to open activity page")
        self.sleep(5)
        self.wait_element_present(RESTORE_LINK).click()
        from main.pages.SidePanel import SidePanel
        return SidePanel(self.driver)


