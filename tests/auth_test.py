import pytest

from main.Platform import Platform
from main.common.Utils import Utils


class TestAuth:
    @pytest.mark.auth
    def test_verify_admin_login(self, driver, url):
        print("To verify Administrator login")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .verify_user_profile_item_present()

    @pytest.mark.auth
    def test_verify_signup_func_in_local_auth(self, driver, url):
        print("To verify signup functionality in Local Auth")

        prefix = Utils.random_string(5)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile")

    @pytest.mark.auth
    def test_verify_error_message_shown_for_wrong_password(self, driver, url):
        print("To verify error message is shown if wrong password is provided")

        Platform(driver).launch(url) \
            .enter_email('Administrator') \
            .enter_password("paaaaaaaassword") \
            .click_login_button() \
            .verify_alert_present("The email address or password you entered is incorrect.")

    @pytest.mark.auth
    def test_verify_error_message_shown_for_wrong_email(self, driver, url):
        print("To verify error message is shown if wrong email ID is provided")

        Platform(driver).launch(url) \
            .enter_email('Administratorrrrr') \
            .enter_password("password") \
            .click_login_button() \
            .verify_alert_present("The email address or password you entered is incorrect.")

    @pytest.mark.auth
    def test_password_field(self, driver, url):
        print("Password for local authentication should be alpha numeric supported")

        prefix = Utils.random_string(5)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "test@putsbox.com") \
            .enter_password("test") \
            .click_signup_button() \
            .verify_alert_present("Password must be a mix of letters of different case, numbers and symbols of atleast 8 and utmost 20 characters")

    @pytest.mark.auth
    def test_verify_unique_email_for_each_user(self, driver, url):
        print("To verify unique Email ID for each user")
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
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button_for_validation() \
            .verify_error_message_present("Please use a different email as this email is already taken") \
            .enter_email(prefix + "auto@putsbox.com") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile")

    @pytest.mark.auth
    def test_verify_change_pwd_local_auth_account(self, driver, url):
        print("To verify the Change password functionality for local auth account")
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
            .open_user_profile_page() \
            .click_change_password_button() \
            .enter_current_password("123qweA!") \
            .enter_new_password("1333rteA!") \
            .enter_retype_password("1333rteA!") \
            .click_update_password_button() \
            .side_panel() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "1333rteA!") \
            .verify_user_profile_item_present()

    # TODO:below test case is marked as 'authentication' because it will change admin password which is used
    # in multiple test cases as entry point
    # @pytest.mark.auth
    # @allure.testcase("To verify the Change password functionality for Administrator account")
    # def test_verify_change_pwd_admin_auth_account(self, driver, url):
    #     Platform(driver).launch(url) \
    #         .login("Administrator", "password") \
    #         .open_user_profile_page() \
    #         .click_change_password_button() \
    #         .enter_current_password("password") \
    #         .enter_new_password("Password@123") \
    #         .enter_retype_password("Password@123") \
    #         .click_update_password_button() \
    #         .side_panel() \
    #         .logout() \
    #         .login("Administrator", "Password@123")

    @pytest.mark.authPlaceholder
    def test_verify_admin_login(self, driver, url):
        print("To verify username placeholder")
        Platform(driver).launch(url) \
            .verify_username_placeholder()
