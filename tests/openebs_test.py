import pytest

from main.Platform import Platform
from main.common.Utils import Utils


class TestOpenEbs:

    # Complete OEP user profile which got created through API and verify OpenEbs components version
    @pytest.mark.openebs
    def test_verify_openebs_components_version(self, driver, url):
        print("To verify profile completion for ORP user and OpenEbs components version check.")
        prefix = Utils.random_string(6)
        phone = Utils.random_number(4)
        Platform(driver).launch(url) \
            .login_as_oep_user("oep.user@mayadata.io", "OEPuser@123") \
            .wait_onboarding_page_loaded() \
            .verify_onboarding_page_title_equals("Update your profile") \
            .enter_company_name(prefix + "Putbox") \
            .enter_role(prefix + "Automation") \
            .enter_phone_number("201-555-" + phone) \
            .click_continue_button() \
            .verify_onboarding_page_title_equals("We have created a project for you!") \
            .enter_project_name("") \
            .click_continue_button() \
            .enter_cluster_name(prefix) \
            .click_connect_button() \
            .click_close_button() \
            .open_clusters_page() \
            .open_cluster_details("oep-cluster-cluster2", "active") \
            .open_ebs_page() \
            .verify_openebs_components_version("1.12.0-ee-RC1")

