import pytest

from main.Platform import Platform
from main.common.Utils import Utils
from main.common import Config


class TestTeaming:
    @pytest.mark.teaming
    def test_project_owner_can_invite_others_join_project(self, driver, url):
        print("ProjectOwner can invite others in his/her Project.")
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectMember", "Administrator")

    @pytest.mark.teaming
    def test_verify_view_pending_users(self, driver, url):
        print("To view pending users")
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .open_user_roles_page() \
            .switch_to_filter_tab("Pending invites") \
            .find_user(prefix + "_test@putsbox.com") \
            .verify_user_present(prefix + "_test@putsbox.com", "Active")

    @pytest.mark.teaming
    def test_verify_accept_decline_invitation_request(self, driver, url):
        print("Only invitee can accept or reject invitation.")
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectMember", "Administrator")

    @pytest.mark.teaming
    def test_verify_decline_invitation_request(self, driver, url):
        print("To validate Decline invitation request")
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectMember", "Administrator") \
            .click_decline_invitation("DefaultProject", "ProjectMember", "Administrator") \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .switch_to_filter_tab("Pending invites") \
            .find_user(prefix + "_test@putsbox.com") \
            .verify_user_present(prefix + "_test@putsbox.com", "Rejected")

    @pytest.mark.teaming
    def test_verify_accept_invitation_request(self, driver, url):
        print("To validate Accept invitation request")
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectMember", "Administrator") \
            .click_accept_invitation("DefaultProject", "ProjectMember", "Administrator") \
            .open_projects_page() \
            .verify_project_present("DefaultProject", "ProjectMember", "Administrator") \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .switch_to_filter_tab("All users") \
            .find_user(prefix + "test" + " " + prefix + "auto") \
            .verify_user_present(prefix + "test" + " " + prefix + "auto", "ProjectMember") \
            .open_user_role_profile_page() \
            .delete_user()

    @pytest.mark.teaming
    def test_verify_user_role_update_by_project_owner(self, driver, url):
        print("To validate Accept invitation request")
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectMember", "Administrator") \
            .click_accept_invitation("DefaultProject", "ProjectMember", "Administrator") \
            .open_projects_page() \
            .verify_project_present("DefaultProject", "ProjectMember", "Administrator") \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .switch_to_filter_tab("All users") \
            .find_user(prefix + "test" + " " + prefix + "auto") \
            .open_user_role_profile_page() \
            .update_user_role("ProjectAdmin") \
            .verify_updated_user_role("ProjectAdmin") \
            .delete_user() \
            .verify_user_absent(prefix + "test" + " " + prefix + "auto")

    @pytest.mark.teaming
    def test_verify_user_role_update_by_non_project_owner(self, driver, url):
        print("To validate Accept invitation request")
        prefix = Utils.random_string(6)
        prefix_2 = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectAdmin") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectAdmin", "Administrator") \
            .click_accept_invitation("DefaultProject", "ProjectAdmin", "Administrator") \
            .open_projects_page() \
            .verify_project_present("DefaultProject", "ProjectAdmin", "Administrator") \
            .logout() \
            .click_create_account_link() \
            .enter_first_name(prefix_2 + "test") \
            .enter_last_name(prefix_2 + "auto") \
            .enter_email(prefix_2 + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix_2) \
            .click_continue_button() \
            .enter_cluster_name(prefix_2) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix_2 + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix_2 + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectMember", "Administrator") \
            .click_accept_invitation("DefaultProject", "ProjectMember", "Administrator") \
            .open_projects_page() \
            .verify_project_present("DefaultProject", "ProjectMember", "Administrator") \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_projects_page() \
            .select_project("DefaultProject") \
            .open_user_roles_page() \
            .switch_to_filter_tab("All users") \
            .find_user(prefix_2 + "test" + " " + prefix_2 + "auto") \
            .open_user_role_profile_page() \
            .update_user_role("ProjectAdmin") \
            .verify_updated_user_role("ProjectMember") \
            .delete_user()
            # .verify_error_message("Changerole Error", "Only [ProjectOwner] can change role.") \

    @pytest.mark.teaming
    def test_verify_project_owner_access(self, driver, url):
        print("To verify Project Owner access")
        prefix = Utils.random_string(6)
        prefix_2 = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .click_create_account_link() \
            .enter_first_name(prefix_2 + "test") \
            .enter_last_name(prefix_2 + "auto") \
            .enter_email(prefix_2 + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix_2) \
            .click_continue_button() \
            .enter_cluster_name(prefix_2) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix_2 + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix_2 + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject" + prefix, "ProjectMember", prefix + "test" + " " + prefix + "auto") \
            .click_accept_invitation("DefaultProject" + prefix, "ProjectMember", prefix + "test" + " " + prefix + "auto") \
            .open_projects_page() \
            .verify_project_present("DefaultProject", "ProjectMember", prefix + "test" + " " + prefix + "auto") \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_user_roles_page() \
            .switch_to_filter_tab("All users") \
            .find_user(prefix_2 + "test" + " " + prefix_2 + "auto") \
            .open_user_role_profile_page() \
            .update_user_role("ProjectAdmin") \
            .verify_updated_user_role("ProjectAdmin") \
            .delete_user() \
            .switch_to_filter_tab("All users") \
            .verify_user_absent(prefix_2 + "test" + " " + prefix + "auto")

    @pytest.mark.teaming
    def test_verify_project_admin_access(self, driver, url):
        print("To verify Project Owner access")
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectAdmin") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectAdmin", "Administrator") \
            .click_accept_invitation("DefaultProject", "ProjectAdmin", "Administrator") \
            .open_projects_page() \
            .verify_project_present("DefaultProject", "ProjectAdmin", "Administrator") \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_projects_page() \
            .verify_edit_icon_visible("DefaultProject") \
            .select_project("DefaultProject") \
            .open_clusters_page() \
            .click_connect_new_cluster_button() \
            .enter_cluster_name("TeamingTestCluster") \
            .click_connect_button() \
            .verify_cluster_connection_link_present() \
            .click_disconnect_cluster_link() \
            .open_clusters_page() \
            .click_delete_icon_for_cluster("TeamingTestCluster") \
            .verify_cluster_delete_warning_message() \
            .click_disconnect_button_for_cluster() \
            .verify_cluster_absent("TeamingTestCluster") \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_alerts_page() \
            .verify_alerts_present() \
            .acknowledge_alert() \


    @pytest.mark.teaming
    def test_verify_project_read_admin_access(self, driver, url):
        print("To verify Project Owner access")
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectReadAdmin") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectReadAdmin", "Administrator") \
            .click_accept_invitation("DefaultProject", "ProjectReadAdmin", "Administrator") \
            .open_projects_page() \
            .verify_edit_icon_invisible("DefaultProject") \
            .select_project("DefaultProject") \
            .open_clusters_page() \
            .verify_connect_new_cluster_button_invisible()

    @pytest.mark.teaming
    def test_verify_project_member_access(self, driver, url):
        print("To verify Project Owner access")
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .click_continue_button() \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email(prefix + "_test@putsbox.com") \
            .select_profile() \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_invitations_page() \
            .verify_received_invitations("DefaultProject", "ProjectMember", "Administrator") \
            .click_accept_invitation("DefaultProject", "ProjectMember", "Administrator") \
            .open_projects_page() \
            .verify_edit_icon_invisible("DefaultProject") \
            .verify_project_not_click_able("DefaultProject")
