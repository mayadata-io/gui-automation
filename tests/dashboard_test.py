import allure
import pytest

from main.Platform import Platform


class TestDashboard:
    @pytest.mark.gada01
    @allure.testcase("To verify graphs are shown in Home dashboards")
    def test_verify_graphs_shown_home_dashboards(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_dashboard_page() \
            .switch_to_graph_container() \
            .verify_graph_present("Storage capacity") \
            .verify_graph_present("Total capacity of all clusters") \
            .verify_graph_present("IOPS of all clusters") \
            .verify_graph_present("Throughput of all clusters")

    @pytest.mark.dashboard
    @allure.testcase("To verify active clusters and other clusters lists are shown in home dashboard")
    def test_verify_clusters_shown_home_dashboards(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_dashboard_page() \
            .switch_to_cluster_tab("Active Cluster") \
            .verify_cluster_present("DemoCluster") \
            .switch_to_cluster_tab("Other Cluster") \
            .verify_clusters_inactive()

    @pytest.mark.dashboard
    @allure.testcase("To verify in Home dashboards project team members are shown")
    def test_verify_project_team_members_shown(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_dashboard_page() \
            .verify_team_member_present("Administrator", "ProjectOwner")

    @pytest.mark.dashboard
    @allure.testcase("To verify alerts are shown and clickable for Active clusters in Home dashboard")
    def test_verify_alerts_clickable_for_active_clusters(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_dashboard_page() \
            .switch_to_cluster_tab("Active Cluster") \
            .open_alert_for_cluster("DemoCluster") \
            .verify_view_order_button_present()

    @pytest.mark.dashboard
    @allure.testcase("To verify the cluster search functionality")
    def test_verify_cluster_search_functionality(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .enter_cluster_name("DemoCluster") \
            .verify_cluster_present("DemoCluster", "Active") \
            .verify_number_of_clusters_equals(1)

    @pytest.mark.dashboard
    @allure.testcase("Cluster dashboard should show the status of all the cluster connected to DOP")
    def test_verify_status_shown_for_each_cluster(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .verify_status_shown_for_each_cluster()

    @pytest.mark.dashboard
    @allure.testcase("Cluster dashboard should show the status of all the cluster connected to DOP")
    def test_verify_status_shown_for_each_cluster(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .verify_status_shown_for_each_cluster()

    @pytest.mark.dashboard
    @allure.testcase("To verify that disconnect text present for delete icon and the pop up message")
    def test_verify_disconnect_text_shown_for_each_delete_icon(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .verify_delete_text_shown_for_each_disconnect_icon() \
            .click_delete_icon_for_cluster("DemoCluster") \
            .verify_modal_dialog_text_equals("Are you sure you want to disconnect DemoCluster-qlyuw cluster?") \
            .click_cancel_button_in_modal_dialog() \
            .open_clusters_page() \
            .click_delete_icon_for_cluster("clusterTest") \
            .verify_modal_dialog_text_equals("Are you sure you want to disconnect clusterTest-fblwd cluster?")

    @pytest.mark.dashboard
    @allure.testcase("To verify User and Roles dashboard view")
    def test_verify_user_roles_dashboard_view(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_user_roles_page() \
            .switch_to_filter_tab("All users") \
            .verify_user_present("Administrator", "ProjectOwner") \
            .switch_to_filter_tab("Pending invites") \
            .verify_user_present("mykola.rus@putsbox.com", "ProjectMember")

    @pytest.mark.gada02
    @allure.testcase("To verify Overview dashboard")
    def test_verify_overview_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details("DemoCluster", "Active") \
            .verify_pool_card_present("cSTOR POOLS") \
            .verify_pool_card_present("JIVA POOLS") \
            .verify_pool_card_present("LOCALPV DEVICE POOLS") \
            .verify_pool_card_present("LOCALPV HOSTPATH POOLS") \
            .verify_pool_card_present("ZFS POOLS") \
            .verify_cluster_overview_info_present() \
            .switch_to_graph_container() \
            .verify_graph_present("Storage capacity") \
            .verify_graph_present("Total capacity of all volumes") \
            .verify_graph_present("IOPS of all volumes") \
            .verify_graph_present("Throughput of all volumes")

    @pytest.mark.dashboard
    @allure.testcase("To verify Application dashboard")
    def test_verify_application_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details("DemoCluster", "Active") \
            .open_applications_page() \
            .verify_applications_present()

    @pytest.mark.dashboard
    @allure.testcase("To verify Pools dashboard")
    def test_verify_pools_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details("DemoCluster", "Active") \
            .open_pools_page() \
            .verify_pools_page_loaded()

    @pytest.mark.dashboard
    @allure.testcase("To verify Volumes dashboard")
    def test_verify_volumes_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details("DemoCluster", "Active") \
            .open_volumes_page() \
            .verify_volumes_present() \
            .verify_volume_present("demo-vol1-claim", "Healthy", "Jiva", "openebs-jiva-default")

    @pytest.mark.gato01
    @allure.testcase("To verify Topology dashboard")
    def test_verify_topology_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details("DemoCluster", "Active") \
            .open_topology_page() \
            .switch_to_topology_container() \
            .verify_connectivity_diagram_present()

    @pytest.mark.dashboard
    @allure.testcase("To verify Monitor dashboard")
    def test_verify_monitor_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details("DemoCluster", "Active") \
            .open_monitor_page() \
            .verify_volumes_present() \
            .verify_volume_present("demo-vol1-claim", "Healthy", "Jiva") \
            .switch_to_metrics_frame() \
            .verify_graph_present("Storage capacity") \
            .verify_graph_present("Total capacity of all volumes") \
            .verify_graph_present("IOPS of all volumes") \
            .verify_graph_present("Throughput of all volumes")

    @pytest.mark.galo01
    @allure.testcase("To verify Logs dashboard")
    def test_verify_logs_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details("DemoCluster", "Active") \
            .open_logs_page() \
            .switch_to_logs_frame() \
            .verify_logs_diagram_present()

    @pytest.mark.gaal01
    @allure.testcase("To verify Alerts dashboard")
    def test_verify_alerts_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details("DemoCluster", "Active") \
            .open_alerts_page() \
            .verify_alerts_present()

    @pytest.mark.dashboard
    @allure.testcase("To verify OpenEBS dashboard")
    def test_verify_openebs_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details("DemoCluster", "Active") \
            .open_ebs_page() \
            .click_control_plane_button() \
            .verify_header_text_equals("Control Plane") \
            .verify_records_present() \
            .click_pools_button() \
            .verify_header_text_equals("cStor Pool Clusters (CSPC)") \
            .click_volumes_button() \
            .verify_header_text_equals("Volumes grouped by applications") \
            .verify_records_present()

    @pytest.mark.dashboard
    @allure.testcase("Dmaas dashboard should show list of schedules and list of restores")
    def test_verify_dmaas_dashboard(self, driver, url):
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_dmaas_page() \
            .verify_header_text_equals("Data-Motion schedules")
