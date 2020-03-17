import allure
import pytest

from main.Platform import Platform
from main.common.Utils import Utils


class TestCluster:
    @pytest.mark.cluster
    @allure.testcase("To verify self connected cluster is shown for Admin user")
    def test_verify_self_connected_cluster_shown_admin_user(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .verify_cluster_present("DemoCluster", "Active")

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

    @pytest.mark.cluster
    @allure.testcase("To verify that connection link getting generated while connecting new cluster.")
    def test_verify_cluster_connection_link_generation(self, driver, url):
        prefix = Utils.random_string(5)
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .click_connect_new_cluster_button() \
            .enter_cluster_name(prefix + "Test") \
            .click_connect_button() \
            .verify_cluster_connection_link_present()

    # Below test case needs to be discussed because self connected cluster is getting disconnected
    @pytest.mark.cluster
    @allure.testcase("To verify self connected cluster should not get disconnected")
    def test_verify_popup_disconnect_message(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .click_delete_icon_for_cluster("DemoCluster-qlyuw") \
            .verify_cluster_delete_warning_message()

    @pytest.mark.cluster
    @allure.testcase("To verify cluster disconnect functionality")
    def test_verify_cluster_disconnect_function(self, driver, url):
        prefix = Utils.random_string(5)
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .click_connect_new_cluster_button() \
            .enter_cluster_name(prefix + "Test") \
            .click_connect_button() \
            .verify_cluster_connection_link_present() \
            .click_disconnect_cluster_link() \
            .open_clusters_page() \
            .click_delete_icon_for_cluster(prefix + "Test") \
            .verify_cluster_delete_warning_message() \
            .click_disconnect_button_for_cluster() \
            .verify_cluster_absent(prefix + "Test")
