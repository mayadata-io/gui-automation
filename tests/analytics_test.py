import allure
import pytest

from main.Platform import Platform
from main.common import Config


class TestAnalytics:
    @pytest.mark.analytics
    def test_verify_volumes_details(self, driver, url):
        print("To verify volumes details are shown")
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_monitor_page() \
            .verify_volume_present("demo-vol1", "Offline", "5G", "busybox", "default", "1", "Jiva")

    @pytest.mark.analytics
    def test_verify_component_status_of_volume(self, driver, url):
        print("To verify different component status of volume")
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_monitor_page() \
            .verify_volume_present("demo-vol1", "Offline", "5G", "busybox", "default", "1", "Jiva") \
            .click_volume_analytics("demo-vol1") \
            .open_volume_tiled_view_dashboard_page() \
            .verify_title_text_present("Volume information") \
            .verify_volume_info("demo-vol1-claim", Config.get("app", "cluster_name"), "0") \
            .verify_graph_present("Volume status") \
            .verify_graph_present("Replica count") \
            .verify_graph_present("Errors") \
            .verify_graph_present("IOPS") \
            .verify_graph_present("Latency") \
            .verify_graph_present("Total capacity") \
            .verify_graph_present("Storage usage") \
            .verify_graph_present("Throughput") \
            .verify_graph_present("Block size")

    @pytest.mark.analytics
    def test_verify_report_generation_functionality(self, driver, url):
        print("To verify the report generation functionality")
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_monitor_page() \
            .verify_volume_present("demo-vol1", "Offline", "5G", "busybox", "default", "1", "Jiva") \
            .click_volume_analytics("demo-vol1") \
            .open_volume_tiled_view_dashboard_page() \
            .verify_title_text_present("Volume information") \
            .verify_volume_info("demo-vol1-claim", Config.get("app", "cluster_name"), "0") \
            .click_report_button() \
            .verify_file_download_button_url("demo-vol1", "OpenEBS")
