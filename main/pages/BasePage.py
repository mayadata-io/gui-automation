import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

ALERT_CONTAINER = (By.CSS_SELECTOR, ".alert.alert-danger")
LOADING_CONTAINER = (By.CSS_SELECTOR, ".loading-container")
MODAL_DIALOG = (By.CSS_SELECTOR, ".modal-overlay.show.modal-open")
CANCEL_BUTTON_MODAL_DIALOG = (By.CSS_SELECTOR, ".modal-overlay.show.modal-open button.btn-outline-primary")
EMPTY_CARD_CONTAINER = (By.CSS_SELECTOR, ".card_zero_result")
USER_PROFILE_ITEM = (By.CSS_SELECTOR, ".sidebar-links img[src*='https://ui-avatars.com']")
LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, *locator):
        self.driver.implicitly_wait(10)
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(*locator)).is_displayed()

    def wait_element_present(self, *locator):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(*locator))
        return WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable(*locator))

    def wait_element_visible(self, *locator):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(*locator))
        return WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(*locator))

    def wait_elements_visible(self, *locator):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(*locator))
        return WebDriverWait(self.driver, 30).until(ec.presence_of_all_elements_located(*locator))

    def wait_element_invisible(self, *locator):
        try:
            self.driver.implicitly_wait(10)
            WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(*locator))
            WebDriverWait(self.driver, 60).until(ec.invisibility_of_element(*locator))
        except Exception:
            print("Element is not visible")

    def switch_to_frame(self, *locator):
        self.driver.implicitly_wait(10)
        iframe = self.driver.find_element_by_css_selector(*locator)
        return self.driver.switch_to.frame(iframe)

    def switch_to_parent_frame(self):
        self.driver.implicitly_wait(10)
        return self.driver.switch_to.parent_frame()

    @staticmethod
    def sleep(wait_time):
        time.sleep(wait_time)

    def find_element_by_id(self, locator):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_id(locator)

    def navigate_to(self, page):
        self.driver.get(page)

    def verify_alert_present(self, message):
        print("Make sure validation message equals to '%s'" % message)
        text = self.wait_element_visible(ALERT_CONTAINER).text
        is_message_correct = message in text

        assert is_message_correct is True, "Validation message is wrong"
        return BasePage(self.driver)

    def wait_loading_container_absent(self):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(LOADING_CONTAINER))
        return WebDriverWait(self.driver, 60).until(ec.invisibility_of_element(LOADING_CONTAINER))

    def verify_modal_dialog_text_equals(self, message):
        print("Make sure message in modal dialog equals to '%s'" % message)
        text = self.wait_element_visible(MODAL_DIALOG).text
        is_message_correct = message in text

        assert is_message_correct is True, "Message in modal dialog is wrong"
        return BasePage(self.driver)

    def click_cancel_button_in_modal_dialog(self, ):
        print("Click 'Cancel' button in modal dialog")
        self.wait_element_visible(CANCEL_BUTTON_MODAL_DIALOG).click()

        from main.pages.SidePanel import SidePanel
        return SidePanel(self.driver)

    def verify_empty_card_container_text_equals(self, message):
        print("Make sure message in empty card container equals to '%s'" % message)
        text = self.wait_element_visible(EMPTY_CARD_CONTAINER).text
        is_message_correct = message in text

        assert is_message_correct is True, "Message in modal dialog is wrong"
        return BasePage(self.driver)

    def verify_email_present(self, email):
        from main.common import EmailWrapper
        data = EmailWrapper.get_email(email)
        assert "test" in data

    def move_to_element(self, locator):
        element = self.wait_element_visible(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        # perform the operation on the element
        actions.perform()

