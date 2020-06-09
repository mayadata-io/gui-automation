import pytest

from main.Platform import Platform
from main.common import Config
from main.common.Utils import Utils


class TestDashboard:
    @pytest.mark.dashboard
    def test_verify_graphs_shown_home_dashboards(self, driver, url):
        print("To verify graphs are shown in Home dashboards")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_dashboard_page() \
            .switch_to_graph_container() \
            .verify_graph_present("Storage capacity") \
            .verify_graph_present("Total capacity of all clusters") \
            .verify_graph_present("IOPS of all clusters") \
            .verify_graph_present("Throughput of all clusters")

    @pytest.mark.dashboard
    def test_verify_clusters_shown_home_dashboards(self, driver, url):
        print("To verify active clusters and other clusters lists are shown in home dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_dashboard_page() \
            .switch_to_cluster_tab("Active Cluster") \
            .verify_cluster_present(Config.get("app", "cluster_name")) \
            .switch_to_cluster_tab("Other Cluster") \
            .verify_clusters_inactive()

    @pytest.mark.dashboard
    def test_verify_project_team_members_shown(self, driver, url):
        print("To verify in Home dashboards project team members are shown")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_dashboard_page() \
            .verify_team_member_present(Config.get("app", "admin_user"), "ProjectOwner")

    @pytest.mark.dashboard
    def test_verify_alerts_clickable_for_active_clusters(self, driver, url):
        print("To verify alerts are shown and clickable for Active clusters in Home dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_dashboard_page() \
            .switch_to_cluster_tab("Active Cluster") \
            .open_alert_for_cluster(Config.get("app", "cluster_name")) \
            .verify_view_order_button_present()

    @pytest.mark.dashboard
    def test_verify_cluster_search_functionality(self, driver, url):
        print("To verify the cluster search functionality")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .enter_cluster_name(Config.get("app", "cluster_name")) \
            .verify_cluster_present(Config.get("app", "cluster_name"), "Active") \
            .verify_number_of_clusters_equals(1)

    @pytest.mark.dashboard
    def test_verify_status_shown_for_each_cluster(self, driver, url):
        print("Cluster dashboard should show the status of all the cluster connected to DOP")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .verify_status_shown_for_each_cluster()

    @pytest.mark.dashboard
    def test_verify_k8_version_shown_for_each_cluster(self, driver, url):
        print("To verify the k8s version for different active and offline clusters in DOP")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .verify_kub_version_shown_for_active_offline_clusters()

    @pytest.mark.dashboard
    def test_verify_disconnect_text_shown_for_each_delete_icon(self, driver, url):
        print("To verify that disconnect text present for delete icon and the pop up message")

        prefix = Utils.random_string(5)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .verify_delete_text_shown_for_each_disconnect_icon() \
            .click_delete_icon_for_cluster(Config.get("app", "cluster_name")) \
            .verify_modal_dialog_text_equals("Are you sure you want to disconnect OpenEBSDirector cluster?") \
            .click_cancel_button_in_modal_dialog() \
            .open_clusters_page() \
            .click_connect_new_cluster_button() \
            .enter_cluster_name(prefix + "Test") \
            .click_connect_button() \
            .verify_cluster_connection_link_present() \
            .click_disconnect_cluster_link() \
            .open_clusters_page() \
            .click_delete_icon_for_cluster(prefix + "Test") \
            .verify_modal_dialog_text_equals("Are you sure you want to disconnect %s" % (prefix + "Test"))

    @pytest.mark.dashboard
    def test_verify_user_roles_dashboard_view(self, driver, url):
        print("To verify User and Roles dashboard view")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_user_roles_page() \
            .click_invite_button() \
            .enter_email("mykola.rus@putsbox.com") \
            .select_role("ProjectMember") \
            .click_send_invite_button() \
            .open_user_roles_page() \
            .switch_to_filter_tab("All users") \
            .verify_user_present(Config.get("app", "admin_user"), "ProjectOwner") \
            .switch_to_filter_tab("Pending invites") \
            .verify_user_present("mykola.rus@putsbox.com", "ProjectMember")

    @pytest.mark.dashboard
    def test_verify_overview_dashboard(self, driver, url):
        print("To verify Overview dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
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
    def test_verify_application_dashboard(self, driver, url):
        print("To verify Application dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_applications_page() \
            .verify_applications_present()

    @pytest.mark.dashboard
    def test_verify_pools_dashboard(self, driver, url):
        print("To verify Pools dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_pools_page() \
            .verify_pools_page_loaded()

    @pytest.mark.dashboard
    def test_verify_volumes_dashboard(self, driver, url):
        print("To verify Volumes dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_volumes_page() \
            .verify_volumes_present()
            # .verify_volume_present("demo-vol1-claim", "Healthy", "Jiva", "openebs-jiva-default")

    @pytest.mark.dashboard
    def test_verify_topology_dashboard(self, driver, url):
        print("To verify Topology dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_monitor_page() \
            .open_topology_page() \
            .switch_to_topology_container() \
            .verify_connectivity_diagram_present()

    @pytest.mark.dashboard
    def test_verify_monitor_dashboard(self, driver, url):
        print("To verify Monitor dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_monitor_page() \
            .verify_volumes_present()
            # .verify_volume_present("csi-vol", "Healthy", "cStor")
            # .switch_to_metrics_frame() \
            # .verify_graph_present("Storage capacity") \
            # .verify_graph_present("Total capacity of all volumes") \
            # .verify_graph_present("IOPS of all volumes") \
            # .verify_graph_present("Throughput of all volumes")

    @pytest.mark.dashboard
    def test_verify_logs_dashboard(self, driver, url):
        print("To verify Logs dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_monitor_page() \
            .open_logs_page() \
            .verify_logs_diagram_present()

    @pytest.mark.dashboard
    def test_verify_alerts_dashboard(self, driver, url):
        print("To verify Alerts dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_alerts_page() \
            .verify_alerts_present()

    @pytest.mark.dashboard
    def test_verify_openebs_dashboard(self, driver, url):
        print("To verify OpenEBS dashboard")
        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_clusters_page() \
            .open_cluster_details(Config.get("app", "cluster_name"), "Active") \
            .open_ebs_page() \
            .verify_open_ebs_page()

    @pytest.mark.dashboard
    def test_verify_dmaas_dashboard(self, driver, url):
        print("Dmaas dashboard should show list of schedules and list of restores")

        Platform(driver).launch(url) \
            .login("Administrator", "password") \
            .open_dmaas_page() \
            .verify_header_text_equals("Data-Motion schedules")

    @pytest.mark.dashboard
    def test_verify_volume_monitoring_graphs_cross_cloud_monitoring_dashboard(self, driver, url):
        print("To verify volume monitoring graphs are shown in cross cloud monitoring dashboard")

        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_cross_cloud_monitoring_page() \
            .switch_to_graph_container() \
            .verify_graph_present("Storage Usage") \
            .verify_graph_present("IOPS(Reads)") \
            .verify_graph_present("IOPS(Writes)") \
            .verify_graph_present("Throughput(Reads)") \
            .verify_graph_present("Throughput(Writes)") \
            .verify_graph_present("Latency(Reads)") \
            .verify_graph_present("Latency(Writes)") \
            .verify_graph_present("Block Size(Reads)") \
            .verify_graph_present("Block Size(Writes)")
