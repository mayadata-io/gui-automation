import pytest

from main.Platform import Platform
from main.common.Utils import Utils


class TestProfile:

    @pytest.mark.profile
    def test_verify_profile_update_after_signup(self, driver, url):
        print("To verify profile can be updated just after signup ")

        prefix = Utils.random_string(6)
        phone = Utils.random_number(10)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .enter_email(prefix + "putsbox.com") \
            .enter_company_name(prefix + "Putbox.com") \
            .enter_role(prefix + "Automation") \
            .enter_phone_number(phone) \
            .click_continue_button() \
            .verify_onboarding_page_title_equals("We have created a project for you!")

    @pytest.mark.profile
    def test_verify_profile_details_same_with_onboarding_profile_details(self, driver, url):
        print("To verify the profile info is same as whatever provided during onboarding time")

        prefix = Utils.random_string(6)
        phone = Utils.random_number(10)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .enter_company_name(prefix + "Putbox.com") \
            .enter_role(prefix + "Automation") \
            .enter_phone_number(phone) \
            .click_continue_button() \
            .verify_onboarding_page_title_equals("We have created a project for you!") \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_user_profile_page() \
            .verify_first_name_equals(prefix + "test") \
            .verify_last_name_equals(prefix + "auto") \
            .verify_email_equals(prefix + "_test@putsbox.com") \
            .verify_company_equals(prefix + "Putbox.com")\
            .verify_role_equals(prefix + "Automation") \
            .verify_phone_equals(phone)

    @pytest.mark.profile
    def test_verify_first_and_last_name_update_in_profile_details(self, driver, url):
        print("To verify first and last name can be modified for local Auth user")

        prefix = Utils.random_string(6)
        phone = Utils.random_number(10)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .enter_company_name(prefix + "Putbox.com") \
            .enter_role(prefix + "Automation") \
            .enter_phone_number(phone) \
            .click_continue_button() \
            .verify_onboarding_page_title_equals("We have created a project for you!") \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_user_profile_page() \
            .enter_first_name("First") \
            .enter_last_name("Last") \
            .click_update_profile_button() \
            .side_panel() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_user_profile_page() \
            .verify_first_name_equals(prefix + "test" + "First") \
            .verify_last_name_equals(prefix + "auto" + "Last")

    @pytest.mark.profile
    def test_verify_company_role_phone_update_in_profile_details(self, driver, url):
        print("To verify company,Role and phone can be modified for local Auth user.")

        prefix = Utils.random_string(6)
        phone = Utils.random_number(10)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .enter_company_name(prefix + "Putbox") \
            .enter_role(prefix + "Automation") \
            .enter_phone_number(phone) \
            .click_continue_button() \
            .verify_onboarding_page_title_equals("We have created a project for you!") \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_user_profile_page() \
            .enter_company_field(".com") \
            .enter_role_field("_Test") \
            .enter_phone_field("9") \
            .click_update_profile_button() \
            .side_panel() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_user_profile_page() \
            .verify_company_equals(prefix + "Putbox" + ".com") \
            .verify_role_equals(prefix + "Automation" + "_Test") \
            .verify_phone_equals(phone + "9")

    @pytest.mark.profile
    def test_verify_admin_first_and_last_name_update_fail(self, driver, url):
        print("To verify First and last Name cannot be modified for local Auth Admin user")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_user_profile_page() \
            .enter_first_name("First") \
            .enter_last_name("Last") \
            .click_update_profile_button() \
            .verify_error_message("Please fill in all required fields")

    # There is an issue with DOP 1.8 regarding below test case, fix will be in 1.9 version
    @pytest.mark.profile
    def test_verify_email_update(self, driver, url):
        print("To verify Email id  can be modified for any user")

        prefix = Utils.random_string(6)
        phone = Utils.random_number(10)
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name(prefix + "test") \
            .enter_last_name(prefix + "auto") \
            .enter_email(prefix + "_test@putsbox.com") \
            .enter_password("123qweA!") \
            .click_signup_button() \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .enter_company_name(prefix + "Putbox.com") \
            .enter_role(prefix + "Automation") \
            .enter_phone_number(phone) \
            .click_continue_button() \
            .verify_onboarding_page_title_equals("We have created a project for you!") \
            .enter_project_name(prefix) \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .logout() \
            .login(prefix + "_test@putsbox.com", "123qweA!") \
            .open_user_profile_page() \
            .enter_email_field(prefix) \
            .click_update_profile_button() \
            .side_panel() \
            .logout() \
            .login(prefix + "_test@putsbox.com" + prefix, "123qweA!") \
            .open_user_profile_page()