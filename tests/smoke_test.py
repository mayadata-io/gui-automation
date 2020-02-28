import allure
import pytest

from main.Platform import Platform


@allure.feature("Smoke suite")
class TestSmoke:
    @pytest.mark.smoke
    @allure.testcase("Ability to Log in with valid credentials")
    def test_ability_login_with_valid_credentials(self, driver, url):
        Platform(driver).launch(url) \
            .enter_email('rucinikolay@gmail.com') \
            .enter_password("12qwaSZX!") \
            .click_login_button() \
            .open_director_online_page() \
            .verify_user_profile_item_present()

    @pytest.mark.smoke
    @allure.testcase("Ability to Log out")
    def test_ability_to_logout(self, driver, url):
        Platform(driver).launch(url) \
            .enter_email('rucinikolay@gmail.com') \
            .enter_password("12qwaSZX!") \
            .click_login_button() \
            .open_director_online_page() \
            .logout() \
            .verify_email_field_present()

    @pytest.mark.smoke
    @allure.testcase("User info is properly displayed")
    def test_user_info_correct(self, driver, url):
        Platform(driver).launch(url) \
            .enter_email('rucinikolay@gmail.com') \
            .enter_password("12qwaSZX!") \
            .click_login_button() \
            .open_director_online_page() \
            .open_user_profile_page() \
            .verify_first_name_equals("Nik") \
            .verify_last_name_equals("Rusinko") \
            .verify_email_equals("rucinikolay@gmail.com") \
            .verify_company_equals("Home") \
            .verify_role_equals("Automation") \
            .verify_phone_equals("+12011234567")

    @pytest.mark.smoke
    @allure.testcase("Project info is properly displayed")
    def test_projects_page(self, driver, url):
        Platform(driver).launch(url) \
            .enter_email('rucinikolay@gmail.com') \
            .enter_password("12qwaSZX!") \
            .click_login_button() \
            .open_director_online_page() \
            .open_projects_page() \
            .verify_project_present("TestProject", "ProjectOwner")

    @pytest.mark.smoke
    @allure.testcase("Cluster info is properly displayed")
    def test_clusters_page(self, driver, url):
        Platform(driver).launch(url) \
            .enter_email('rucinikolay@gmail.com') \
            .enter_password("12qwaSZX!") \
            .click_login_button() \
            .open_director_online_page() \
            .open_clusters_page() \
            .verify_cluster_present("TestAutomation-de5b8", "Inactive")
