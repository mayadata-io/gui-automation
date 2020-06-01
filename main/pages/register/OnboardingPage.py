from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage
from main.pages.SidePanel import SidePanel

ONBOARDING_HEADER = (By.CSS_SELECTOR, ".onboarding-content-header_title")
PROJECT_NAME_FIELD = (By.XPATH, "//label[text()='Rename your project']/following-sibling::span/input")
CONTINUE_BUTTON = (By.CSS_SELECTOR, ".onboarding-content input.btn")
CLUSTER_NAME_FIELD = (By.XPATH, "//label[text()='Cluster name']/following-sibling::input")
CONNECT_BUTTON = (By.XPATH, "//input[@value='CONNECT']")
# CLOSE_BUTTON = (By.XPATH, "//h5[contains(text(), 'Connect to Director')]/preceding::span[contains(@class, 'mi')]")
CLOSE_BUTTON = (By.XPATH, "//span[@class='mi mi-x mi-1x float-right text-white']")
EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
COMPANY_FIELD = (By.XPATH, "//label[text()='Company']/following-sibling::input")
ROLE_FIELD = (By.XPATH, "//label[text()='Role']/following-sibling::input")
PHONE_FIELD = (By.CSS_SELECTOR, "input[type='tel']")


class OnboardingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_onboarding_page_loaded(self):
        print("Wait 'Onboarding' page loaded")
        self.wait_loading_container_absent()
        return OnboardingPage(self.driver)

    def verify_onboarding_page_title_equals(self, title):
        print("Make sure 'Onboarding' page title equals '%s'" % title)
        self.sleep(5)
        actual_title = self.wait_element_present(ONBOARDING_HEADER).text
        assert title in actual_title, "Header is wrong"
        return OnboardingPage(self.driver)

    def click_continue_button(self):
        print("Click 'Continue' link")
        self.wait_element_present(CONTINUE_BUTTON).click()
        return OnboardingPage(self.driver)

    def enter_email(self, email):
        print("Enter '%s' into 'Email' field" % email)
        self.wait_element_present(EMAIL_FIELD).send_keys(email)
        return OnboardingPage(self.driver)

    def enter_company_name(self, company):
        print("Enter '%s' into 'Company name' field" % company)
        self.wait_element_present(COMPANY_FIELD).send_keys(company)
        return OnboardingPage(self.driver)

    def enter_role(self, role):
        print("Enter '%s' into 'Role' field" % role)
        self.wait_element_present(ROLE_FIELD).send_keys(role)
        return OnboardingPage(self.driver)

    def enter_phone_number(self, phone):
        print("Enter '%s' into 'Phone' field" % phone)
        self.wait_element_present(PHONE_FIELD).send_keys(phone)
        return OnboardingPage(self.driver)

    def enter_project_name(self, projectname):
        print("Enter '%s' into 'Project name' field" % projectname)
        self.wait_element_present(PROJECT_NAME_FIELD).send_keys(projectname)
        return OnboardingPage(self.driver)

    def enter_cluster_name(self, clustername):
        print("Enter '%s' into 'Cluster name' field" % clustername)
        self.wait_element_present(CLUSTER_NAME_FIELD).send_keys(clustername)
        return OnboardingPage(self.driver)

    def click_connect_button(self):
        print("Click 'Connect' link")
        self.wait_element_present(CONNECT_BUTTON).click()
        return OnboardingPage(self.driver)

    def click_close_button(self):
        print("Click 'Close' link")
        try:
            self.wait_elements_visible(CLOSE_BUTTON)[1].click()
        except Exception:
            self.wait_elements_visible(CLOSE_BUTTON)[0].click()

        return SidePanel(self.driver)
