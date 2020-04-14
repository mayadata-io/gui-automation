import allure
import pytest

from main.Platform import Platform
from main.common.Utils import Utils


class TestDmaas:
    @pytest.mark.dmaas
    @allure.testcase("Create dmaas schedule and check the status for deployment app(cstor)")
    def test_verify_creation_of_deployment_dmaas_schedule(self, driver, url):
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .click_add_cloud_credential_button() \
            .verify_modal_dialog_present("Create new cloud credentials") \
            .enter_title("demo-cred") \
            .enter_username("minio") \
            .enter_password("minio123") \
            .click_save_button() \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Minutely") \
            .select_minutes("05")\
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_on_remove_dmaas_schedule_icon() \
            .click_delete_dmaas_schedule_button() \
            .verify_dmass_schedule_absent()

    @pytest.mark.dmaas
    @allure.testcase("Create dmaas schedule and check the status for StatefulSet app(cstor)")
    def test_verify_creation_of_stateful_dmaas_schedule(self, driver, url):
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Minutely") \
            .select_minutes("05") \
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_on_remove_dmaas_schedule_icon() \
            .click_delete_dmaas_schedule_button() \
            .verify_dmass_schedule_absent()

    @pytest.mark.dmaas
    @allure.testcase("Delete dmaas schedule")
    def test_verify_deletion_of_dmaas_schedule(self, driver, url):
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Minutely") \
            .select_minutes("05") \
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_on_remove_dmaas_schedule_icon() \
            .click_delete_dmaas_schedule_button() \
            .verify_dmass_schedule_absent()

    @pytest.mark.dmaas
    @allure.testcase("Create dmaas schedule (Hourly) and check the status for deployment app(cstor)")
    def test_verify_creation_of_hourly_dmaas_schedule(self, driver, url):
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Hourly") \
            .select_minutes("05") \
            .select_hour("03") \
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_on_remove_dmaas_schedule_icon() \
            .click_delete_dmaas_schedule_button() \
            .verify_dmass_schedule_absent()

    @pytest.mark.dmaas
    @allure.testcase("Create dmaas schedule (Daily) and check the status for deployment app(cstor)")
    def test_verify_creation_of_daily_dmaas_schedule(self, driver, url):
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Daily") \
            .select_minutes_second("10", "15") \
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_on_remove_dmaas_schedule_icon() \
            .click_delete_dmaas_schedule_button() \
            .verify_dmass_schedule_absent()

    @pytest.mark.dmaas
    @allure.testcase("Create dmaas schedule (Weekly) and check the status for deployment app(cstor)")
    def test_verify_creation_of_weekly_dmaas_schedule(self, driver, url):
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Weekly") \
            .select_minutes_second("10", "15") \
            .select_day("Monday") \
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_on_remove_dmaas_schedule_icon() \
            .click_delete_dmaas_schedule_button() \
            .verify_dmass_schedule_absent()

    @pytest.mark.dmaas
    @allure.testcase("Create dmaas schedule (Monthly) and check the status for deployment app(cstor)")
    def test_verify_creation_of_monthly_dmaas_schedule(self, driver, url):
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Monthly") \
            .select_minutes_second("10", "15") \
            .select_date("16") \
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_on_remove_dmaas_schedule_icon() \
            .click_delete_dmaas_schedule_button() \
            .verify_dmass_schedule_absent()

    @pytest.mark.dmaas
    @allure.testcase("Check if the backups are taken incrementally")
    def test_verify_dmaas_schedule_backup_taken_incrementally(self, driver, url):
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Minutely") \
            .select_minutes("01") \
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_dmaas_schedule() \
            .verify_incremental_backups() \
            .click_back_button() \
            .search_dmaas_schedule() \
            .click_on_remove_dmaas_schedule_icon() \
            .click_delete_dmaas_schedule_button() \
            .verify_dmass_schedule_absent()

    @pytest.mark.dmaas
    @allure.testcase("Check the backups status")
    def test_verify_dmaas_schedule_backup_status(self, driver, url):
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Hourly") \
            .select_minutes("05") \
            .select_hour("03") \
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_dmaas_schedule() \
            .verify_status_of_backups("Completed") \
            .click_back_button() \
            .search_dmaas_schedule() \
            .click_on_remove_dmaas_schedule_icon() \
            .click_delete_dmaas_schedule_button() \
            .verify_dmass_schedule_absent()

    @pytest.mark.dmaas
    @allure.testcase("Restore dmaas schedule")
    def test_verify_restore_of_dmaas_schedule(self, driver, url):
        prefix = Utils.random_string(6)
        Platform(driver).launch(url) \
            .login_as_admin() \
            .open_clusters_page() \
            .open_cluster_details("OpenEBS", "Active") \
            .open_applications_page() \
            .search_application("minio-deployment") \
            .click_on_application("minio-deployment", "Deployment") \
            .verify_application_type("minio-deployment", "Deployment") \
            .verify_volume_cas_type("minio-pv", "cStor") \
            .click_dmass_button() \
            .click_new_schedule_button() \
            .select_cloud_provider("MINIO") \
            .select_provider_credential("demo-cred") \
            .enter_minio_url("http://147.75.101.91:32711") \
            .select_interval("Hourly") \
            .select_minutes("05") \
            .select_hour("03") \
            .click_schedule_now_button() \
            .verify_dmass_schedule_present() \
            .search_dmaas_schedule() \
            .click_dmaas_schedule() \
            .verify_status_of_backups("Completed") \
            .click_on_restore_dmaas_schedule_icon() \
            .select_restore_cluster("dmaasRestoreTest-nqsf8") \
            .click_start_restore_button() \
            .click_restore_link() \
            .open_dmaas_page() \
            .open_schedules_page() \
            .verify_restore_status("Success")


