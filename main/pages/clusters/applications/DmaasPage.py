from selenium.webdriver.common.by import By

from main.common import Config
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER

NEW_SCHEDULE_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")
# CLOUD_PROVIDER = (By.CSS_SELECTOR, ".tab-chooser")
CLOUD_PROVIDER = (By.CSS_SELECTOR, ".chooser-card")
CLOUD_PROVIDER_AVATAR = ".tab-chooser-logo"
ADD_CLOUD_CREDENTIAL = (By.CSS_SELECTOR, "button.btn.btn-outline-primary.btn-pill.btn-lg")
MODAL_DIALOG = (By.CSS_SELECTOR, ".modal-content.b-d")
CREDENTIAL_TITLE = (By.ID, "credential-title")
CREDENTIAL_ACCESS_KEY_ID = (By.ID, "credential-Accesskey-id")
CREDENTIAL_SECRET_KEY = (By.ID, "credential-secretkey")
CANCEL_BUTTON =(By.XPATH, "//button[@class='btn btn-outline-primary']")
SAVE_BUTTON = (By.XPATH, "//input[@value='Save']")
SELECT_PROVIDER_CREDENTIALS = (By.XPATH, "//div[@class='mr-5']//div[@class='form-group']")
SELECT_AWS_REGION = (By.XPATH, "//div[@class='form-group w-25']//select[@class='form-control']")
MINIO_URL_FIELD = (By.XPATH, "//input[@placeholder='http://minio.example.com']")
MINIO_HREF = (By.XPATH, "//a[contains(text(),'Get credential for Minio')]")
SELECT_INTERVAL_FIELD = (By.XPATH, "//div[@class='mt-0']//select[@class='form-control']")
SELECT_MINUTE_FIELD = (By.XPATH, "//span[contains(text(),'Minute(s)')]/preceding-sibling::select[1]")
SELECT_HOUR_FIELD = (By.XPATH, "//span[contains(text(),'Hour')]/preceding-sibling::select[1]")
SELECT_TIME_FIELD = (By.XPATH, "//input[@placeholder='Select time']")
SELECT_DAY_FIELD = (By.XPATH, "//div[@class='ml-4 d-flex justify-content-center align-items-center']//div//select[@class='form-control']")
SELECT_DROPDOWN_MINUTE = (By.XPATH, "//ul[@class='time-lists-minutes']")
SELECT_DROPDOWN_SECOND = (By.XPATH, "//ul[@class='time-lists-seconds']")
SELECT_TIME_OK_BUTTON = (By.XPATH, "//button[@class='btn btn-primary btn-sm']")
SELECT_CALENDER = (By.XPATH, "//div[@class='calendar-day-month-picker_wrapper']//ol")
SCHEDULE_NOW_BUTTON = (By.XPATH , "//input[@value='Schedule now']")
SCHEDULE_LIST = (By.CSS_SELECTOR, ".text-hyperlink")
SCHEDULE_STATUS = (By.CSS_SELECTOR, ".cluster-name")
SCHEDULE_REMOVE_ICON = (By.CSS_SELECTOR, ".mi.mi-trash.mi-1x")
SCHEDULE_RESTORE_ICON = (By.CSS_SELECTOR, ".mi.mi-cloud-reload.mi-1x")
SCHEDULE_DELETE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-danger")
SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Find a schedule']")
SCHEDULE_HREF = (By.XPATH, "//span[contains(., 'sch-')]")
LIST_OF_BACKUPS = (By.XPATH, "//table[@class='table table-sm']//tbody")
BACKUP_TABLE = (By.CSS_SELECTOR, "table.table.table-sm tbody tr")
BACK_BUTTON = (By.CSS_SELECTOR, ".mi.mi-arrow-left-curve.mi-1x")
MODAL_TITLE = (By.XPATH, "//h5[@class='modal-title']")
MODAL_YES_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")
CSTOR_SLIDER = (By.XPATH, "//span[@class='slider round']")
RETENTION_COUNT = (By.XPATH, "//input[@id='retention-count']")


class DmaasPage(BasePage):
    new_schedule_name = ""

    def __init__(self, driver):
        super().__init__(driver)

    def enter_title(self, title):
        print("Enter '%s' into 'Title' field" % title)
        self.wait_element_present(CREDENTIAL_TITLE).send_keys(title)
        return DmaasPage(self.driver)

    def enter_username(self, username):
        print("Enter username")
        self.wait_element_present(CREDENTIAL_ACCESS_KEY_ID).send_keys(username)
        return DmaasPage(self.driver)

    def enter_password(self, password):
        print("Enter password")
        self.wait_element_present(CREDENTIAL_SECRET_KEY).send_keys(password)
        return DmaasPage(self.driver)

    def click_save_button(self):
        print("Click 'Save' button")
        self.wait_element_present(SAVE_BUTTON).click()
        self.sleep(5)
        return DmaasPage(self.driver)

    def click_new_schedule_button(self):
        print("Click 'New Schedule' button")
        self.wait_element_present(NEW_SCHEDULE_BUTTON).click()
        return DmaasPage(self.driver)

    def click_add_cloud_credential_button(self):
        print("Click 'Add Cloud Credential' button")
        self.wait_element_present(ADD_CLOUD_CREDENTIAL).click()
        return DmaasPage(self.driver)

    def select_cloud_provider(self, name):
        print("Select cloud provider '%s'" % name)
        select_platform = self.wait_element_visible(CLOUD_PROVIDER)
        items = select_platform.find_elements_by_tag_name("li")
        for item in items:
            print(item.text)
            if name in item.text:
                print(item.text)
                item.click()
                break
        return DmaasPage(self.driver)

    def verify_modal_dialog_present(self, name):
        print("Make sure modal dialog '%s' present" % name)
        text = self.wait_element_visible(MODAL_DIALOG).text
        is_exists = False
        if name in text:
            is_exists = True
        assert is_exists is True, "Modal dialog is absent"
        return DmaasPage(self.driver)

    def select_provider_credential(self, name):
        print("Select Provider credential '%s'" % name)
        select = self.wait_element_present(SELECT_PROVIDER_CREDENTIALS)
        for option in select.find_elements_by_tag_name('option'):
            if name in option.text:
                option.click()
                break
        self.sleep(10)
        return DmaasPage(self.driver)

    def select_region(self, region):
        print("Select AWS region'%s' from list" % region)
        select = self.wait_element_present(SELECT_AWS_REGION)
        for option in select.find_elements_by_tag_name('option'):
            if option.text in region:
                option.click()
                break
        self.sleep(10)
        return DmaasPage(self.driver)

    def enter_minio_url(self, url):
        print("Enter '%s' into Minio URL field" % url)
        self.wait_element_present(MINIO_URL_FIELD).send_keys(url)
        return DmaasPage(self.driver)

    def select_interval(self, name):
        print("Select Interval '%s'" % name)
        select = self.wait_element_present(SELECT_INTERVAL_FIELD)
        for option in select.find_elements_by_tag_name('option'):
            if name in option.text:
                option.click()
                break
        return DmaasPage(self.driver)

    def select_minutes(self, minute):
        print("Select Minute '%s'" % minute)
        select = self.wait_element_present(SELECT_MINUTE_FIELD)
        for option in select.find_elements_by_tag_name('option'):
            if minute in option.text:
                option.click()
                break
        return DmaasPage(self.driver)

    def select_hour(self, hour):
        print("Select Hour '%s'" % hour)
        select = self.wait_element_present(SELECT_HOUR_FIELD)
        for option in select.find_elements_by_tag_name('option'):
            if hour in option.text:
                option.click()
                break
        return DmaasPage(self.driver)

    def click_schedule_now_button(self):
        print("Click 'Schedule now' button")
        self.sleep(5)
        self.wait_element_present(SCHEDULE_NOW_BUTTON).click()
        self.sleep(5)
        return DmaasPage(self.driver)

    def verify_dmass_schedule_present(self):
        print("Make sure that dmaas schedule is present")
        schedules = self.wait_elements_visible(SCHEDULE_LIST)
        is_exists = False
        for schedule in schedules:
            print(schedule.text)
            if schedule.text:
                DmaasPage.new_schedule_name = schedule.text
                is_exists = True
                break
        assert is_exists is True, "Schedule is absent"
        return DmaasPage(self.driver)

    def verify_dmass_schedule_absent(self):
        print("Make sure that dmaas schedule is absent")
        self.sleep(15)
        is_exists = False
        try:
            if self.is_element_present(EMPTY_CARD_CONTAINER):
                self.verify_empty_card_container_text_equals("Looks like you do not have any schedules yet")
        except Exception:
            schedules = self.wait_elements_visible(SCHEDULE_LIST)
            for schedule in schedules:
                if DmaasPage.new_schedule_name in schedule.text:
                    is_exists = True
                    break
        assert is_exists is False, "Schedule is present"
        return DmaasPage(self.driver)

    def search_dmaas_schedule(self):
        print("Enter schedule name '%s' in search field" % DmaasPage.new_schedule_name)
        self.wait_element_present(SEARCH_FIELD).send_keys(DmaasPage.new_schedule_name)
        return DmaasPage(self.driver)

    def click_on_remove_dmaas_schedule_icon(self):
        print("Click on Remove icon to remove Dmass schedule")
        self.wait_element_visible(SEARCH_FIELD)
        self.wait_element_present(SCHEDULE_REMOVE_ICON).click()
        return DmaasPage(self.driver)

    def verify_status_of_backups(self, status):
        print("Make sure that that status is '%s'" % status)
        wait_count = 0
        while wait_count < 50:
            if self.is_element_exist(EMPTY_CARD_CONTAINER):
                self.sleep(2)
                wait_count = wait_count + 1
                self.driver.refresh()
                self.click_dmaas_schedule("active")
            else:
                print("Backup present")
                break
        try:
            print(self.is_element_present(EMPTY_CARD_CONTAINER))
            self.is_element_present(EMPTY_CARD_CONTAINER)
            print("Backup list not generated.")
        except Exception:
            text = self.wait_element_visible(LIST_OF_BACKUPS).text
            is_exists = False
            count = 0
            while count < 300:
                if status in text:
                    is_exists = True
                    break
                else:
                    self.sleep(5)
                    count = count + 1
                    if "PartiallyFailed" in text:
                        print("backup is partially failed")
                        is_exists = False
                        break
                    text = self.wait_element_visible(LIST_OF_BACKUPS).text
            assert is_exists is True, "Status of backup is not completed"
        return DmaasPage(self.driver)

    def click_on_restore_dmaas_schedule_icon(self):
        print("Click on Restore icon to restore Dmass schedule")
        self.wait_element_present(SCHEDULE_RESTORE_ICON).click()
        self.sleep(10)
        from main.pages.dmaas.schedules.backup.RestorePage import RestorePage
        return RestorePage(self.driver)

    def click_delete_dmaas_schedule_button(self):
        print("Click on Delete button to delete Dmass schedule")
        self.wait_element_present(SCHEDULE_DELETE_BUTTON).click()
        self.sleep(10)
        return DmaasPage(self.driver)

    def select_minutes_second(self, minute, second):
        print("Click on 'Select Time' and select minute '%s' and second '%s'" % (minute, second))
        self.wait_element_present(SELECT_TIME_FIELD).click()
        select_minute = self.wait_element_visible(SELECT_DROPDOWN_MINUTE)
        items = select_minute.find_elements_by_tag_name("li")
        for item in items:
            if minute in item.text:
                item.click()
                break
        select_second = self.wait_element_visible(SELECT_DROPDOWN_SECOND)
        items = select_second.find_elements_by_tag_name("li")
        for item in items:
            if second in item.text:
                item.click()
                break
        self.wait_element_present(SELECT_TIME_OK_BUTTON).click()
        return DmaasPage(self.driver)

    def select_day(self, day):
        print("Select Day '%s'" % day)
        select = self.wait_element_present(SELECT_DAY_FIELD)
        for option in select.find_elements_by_tag_name('option'):
            if option.text == day:
                option.click()
                break
        return DmaasPage(self.driver)

    def select_date(self, date):
        print("Select Date '%s'" % date)
        select_date = self.wait_element_visible(SELECT_CALENDER)
        items = select_date.find_elements_by_tag_name("li")
        for item in items:
            if date in item.text:
                item.click()
                break
        return DmaasPage(self.driver)

    def click_dmaas_schedule(self, status):
        print("Click on '%s' dmaas schedule" % DmaasPage.new_schedule_name)
        text = self.wait_element_visible(SCHEDULE_STATUS).text
        count = 0
        while count < 30:
            if status in text:
                self.wait_element_present(SCHEDULE_HREF).click()
                break
            else:
                self.sleep(2)
                count = count + 1
                text = self.wait_element_visible(SCHEDULE_STATUS).text
        return DmaasPage(self.driver)

    def verify_incremental_backups(self):
        print("Make sure that backups are taken incrementally")
        self.sleep(90)
        try:
            if self.is_element_present(EMPTY_CARD_CONTAINER):
                print("Backup list is not generated.")

        except Exception:
            backups = self.wait_elements_visible(BACKUP_TABLE)
            size = len(backups)
            assert size > 2, "Backups are not taken incrementally"
        return DmaasPage(self.driver)

    def click_back_button(self):
        print("Click on back button")
        self.wait_element_present(BACK_BUTTON).click()
        return DmaasPage(self.driver)

    def confirm_aws_schedule(self):
        print("Click on 'Yes sure' button to to schedule new AWS backup")
        try:
            self.wait_element_visible(MODAL_TITLE)
            self.wait_element_present(MODAL_YES_BUTTON).click()
        except Exception:
            print("No modal box second time")
            pass
        return DmaasPage(self.driver)

    def set_cloud_credential(self, name, title):
        print("Add '%s' cloud credential" % name)
        self.enter_title(title)
        if name == 'AWS':
            self.enter_username(Config.get_value("default", "aws_access_key_id"))
            self.enter_password(Config.get_value("default", "aws_secret_access_key"))
        elif name == 'MINIO':
            self.enter_username(Config.get_value("minio", "user"))
            self.enter_password(Config.get_value("minio", "pwd"))
        else:
            self.enter_username(Config.get_value("default", "aws_access_key_id"))
            self.enter_password(Config.get_value("default", "aws_secret_access_key"))
        self.click_save_button()
        return DmaasPage(self.driver)

    def click_cstor_based_backup(self):
        print("Click 'cStor based' slider button")
        self.wait_element_present(CSTOR_SLIDER).click()
        return DmaasPage(self.driver)

    def enter_retention_count(self, count):
        print("Enter '%s' into 'Backup retention count' field" % count)
        self.wait_element_present(RETENTION_COUNT).send_keys(count)
        return DmaasPage(self.driver)
