import allure
import pytest

from main.Platform import Platform


class TestSmoke:
    @pytest.mark.cluster
    @allure.testcase("To verify self connected cluster is shown for Admin user")
    def test_verify_self_connected_cluster_shown_admin_user(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .verify_cluster_present("OpenEBSDirector", "Active")

    @pytest.mark.smoke
    @allure.testcase("To verify cluster name should not be less than 6 character and special characters not allowed")
    def test_verify_cluster_name_field(self, driver, url):
        Platform(driver).launch(url) \
            .enter_email('rucinikolay@gmail.com') \
            .enter_password("12qwaSZX!") \
            .click_login_button() \
            .open_director_online_page() \
            .open_clusters_page() \
            .verify_cluster_present("TestAutomation-de5b8", "Inactive")