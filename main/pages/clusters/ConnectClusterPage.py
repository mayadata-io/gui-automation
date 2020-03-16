from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

CLUSTER_NAME_FIELD = (By.XPATH, "//label[text()='Cluster name']/following-sibling::input")
VALIDATION_MESSAGE = (By.CSS_SELECTOR, ".font-italic.text-danger")
CONNECT_BUTTON = (By.XPATH, "//input[@value='CONNECT']")
CONNECT_CLUSTER_LINK = (By.XPATH, "//textarea[@class='ember-text-area form-control copy-block-text ember-view']")


class ConnectClusterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_cluster_name(self, name):
        print("Enter '%s' into 'Cluster name' field" % name)
        self.wait_element_present(CLUSTER_NAME_FIELD).send_keys(name)
        return ConnectClusterPage(self.driver)

    def click_connect_button(self):
        print("Click 'Connect' button")
        self.wait_element_present(CONNECT_BUTTON).click()
        return ConnectClusterPage(self.driver)

    def verify_error_message_present(self, message):
        print("Make sure validation message equals to '%s'" % message)
        text = self.wait_element_visible(VALIDATION_MESSAGE).text
        is_message_correct = message in text

        assert is_message_correct is True, "Validation message is wrong"
        return ConnectClusterPage(self.driver)

    def verify_cluster_connection_link_present(self):
        self.wait_element_visible(CONNECT_CLUSTER_LINK)
        return ConnectClusterPage(self.driver)