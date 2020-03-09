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

    @pytest.mark.cluster
    @allure.testcase("To verify cluster name should not be less than 6 character and special characters not allowed")
    def test_verify_cluster_name_field(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .click_connect_new_cluster_button() \
            .enter_cluster_name("clust") \
            .click_connect_button() \
            .verify_error_message_present("Cluster name should be greater than 6 and less than 25 characters and should not contain any special characters.")
