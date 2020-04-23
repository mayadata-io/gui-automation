from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage

OUTLET_HEADER = (By.CSS_SELECTOR, ".outlet-header__top-bar")
AVAILABLE_INVITATIONS = (By.CSS_SELECTOR, ".app-contents table tbody tr")
ACCEPT_BUTTON = ".text-success"
DECLINE_BUTTON = ".text-danger"


class InvitationsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_received_invitations(self, project, role, invited_by):
        print("Make sure that invitation by '%s' is present" % invited_by)
        is_exists = False
        self.wait_element_visible(OUTLET_HEADER)
        invitations = self.wait_elements_visible(AVAILABLE_INVITATIONS)

        for invitation in invitations:
            text = invitation.text
            if project in text and role in text and invited_by in text:
                is_exists = True
                invitation.find_element_by_css_selector(DECLINE_BUTTON)
                invitation.find_element_by_css_selector(ACCEPT_BUTTON)
                #self.sleep(10)
                break

        assert is_exists is True, "Invitation is absent"
        return InvitationsPage(self.driver)

    def click_decline_invitation(self, project, role, invited_by):
        print("Make sure that invitation by '%s' is present and click on Decline button" % invited_by)
        is_exists = False
        self.wait_element_visible(OUTLET_HEADER)
        invitations = self.wait_elements_visible(AVAILABLE_INVITATIONS)

        for invitation in invitations:
            text = invitation.text
            if project in text and role in text and invited_by in text:
                is_exists = True
                invitation.find_element_by_css_selector(DECLINE_BUTTON).click()
                #self.sleep(10)
                break

        assert is_exists is True, "Invitation is absent"
        from main.pages.SidePanel import SidePanel
        return SidePanel(self.driver)

    def click_accept_invitation(self, project, role, invited_by):
        print("Make sure that invitation by '%s' is present and click on Accept button" % invited_by)
        is_exists = False
        self.wait_element_visible(OUTLET_HEADER)
        invitations = self.wait_elements_visible(AVAILABLE_INVITATIONS)

        for invitation in invitations:
            text = invitation.text
            if project in text and role in text and invited_by in text:
                is_exists = True
                invitation.find_element_by_css_selector(ACCEPT_BUTTON).click()
                #self.sleep(10)
                break

        assert is_exists is True, "Invitation is absent"
        from main.pages.SidePanel import SidePanel
        return SidePanel(self.driver)
