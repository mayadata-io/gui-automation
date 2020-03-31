import pytest

from main.Platform import Platform
from main.common import Config
from main.common.Utils import Utils


class TestCluster:
    @pytest.mark.gacc01
    def test_verify_self_connected_cluster_shown_admin_user(self, driver, url):
        print("To verify self connected cluster is shown for Admin user")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .verify_cluster_present(Config.get("app", "cluster_name"), "Active")

    @pytest.mark.gacc01
    def test_verify_cluster_name_field(self, driver, url):
        print("To verify cluster name should not be less than 6 character and special characters not allowed")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .click_connect_new_cluster_button() \
            .enter_cluster_name("clust") \
            .click_connect_button() \
            .verify_error_message_present("Cluster name should be greater than 6 and less than 25 characters and should not contain any special characters.")

    @pytest.mark.gacc01
    def test_verify_cluster_connection_link_generation(self, driver, url):
        print("To verify that connection link getting generated while connecting new cluster.")

        prefix = Utils.random_string(5)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .click_connect_new_cluster_button() \
            .enter_cluster_name(prefix + "Test") \
            .click_connect_button() \
            .verify_cluster_connection_link_present()

    # Below test case needs to be discussed because self connected cluster is getting disconnected
    # and one active self connected cluster needed for other test case
    @pytest.mark.gacc01
    def test_verify_popup_disconnect_message(self, driver, url):
        print("To verify self connected cluster should not get disconnected")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .click_delete_icon_for_cluster(Config.get("app", "cluster_name")) \
            .verify_cluster_delete_warning_message()

    @pytest.mark.gacc01
    def test_verify_cluster_disconnect_function(self, driver, url):
        print("To verify cluster disconnect functionality")

        prefix = Utils.random_string(5)
        Platform(driver).launch(url) \
            .login_as_admin() \
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
