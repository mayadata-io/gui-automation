import allure
import pytest

from main.Platform import Platform


class TestAuth:
    @pytest.mark.smoke
    @allure.testcase("To verify signup functionality in Local Auth")
    def test_verify_signup_func_in_local_auth(self, driver, url):
        Platform(driver).launch(url) \
            .click_create_account_link() \
            .enter_first_name() \
            .enter_last_name() \
            .enter_email() \
            .enter_password() \
            .click_signup_button()

    @pytest.mark.smoke
    @allure.testcase("To verify error message is shown if wrong password is provided")
    def test_verify_error_message_shown_for_wrong_password(self, driver, url):
        Platform(driver).launch(url) \
            .enter_email('rucinikolay@gmail.com') \
            .enter_password("12qwaaaaaaSZX!") \
            .click_login_button() \
            .verify_cluster_present("The email address or password you entered is incorrect.")

    @pytest.mark.smoke
    @allure.testcase("To verify error message is shown if wrong email ID is provided")
    def test_verify_error_message_shown_for_wrong_email(self, driver, url):
        Platform(driver).launch(url) \
            .enter_email('rucinikolay1111@gmail.com') \
            .enter_password("12qwaSZX!") \
            .click_login_button() \
            .verify_cluster_present("The email address or password you entered is incorrect.")