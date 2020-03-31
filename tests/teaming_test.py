import pytest

from main.Platform import Platform


class TestTeaming:
    @pytest.mark.teaming
    def test_project_owner_can_invite_others_join_project(self, driver, url):
        print("ProjectOwner can invite others in his/her Project.")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email("mykola.rus@putsbox.com") \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .verify_email_present("mykola.rus@putsbox.com")

    @pytest.mark.teaming
    def test_verify_view_pending_users(self, driver, url):
        print("To view pending users")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email("view_pending@putsbox.com") \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .switch_to_filter_tab("Pending invites") \
            .verify_user_present("view_pending@putsbox.com", "ProjectMember")