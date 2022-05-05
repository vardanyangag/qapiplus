from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class AbuseAndNeglectTrackingLog(GeneralViewTrackingLog):
    def __init__(self,driver):
        super().__init__(driver)
        self.abuse_and_neglect_tracking_log_report_date = self.driver.instance.find_element(By.XPATH, "//input[@name='reportDate']")
        self.abuse_and_neglect_tracking_log_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@name='patientMRNumber']")
        self.abuse_and_neglect_tracking_log_abuse_neglact_type = self.driver.instance.find_element(By.XPATH, "//input[@name='abuseAndNeglectType']")
        self.abuse_and_neglect_tracking_log_reported_to = self.driver.instance.find_element(By.XPATH, "//input[@name='reportedTo']")
        self.abuse_and_neglect_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.abuse_and_neglect_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")