from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class SentinelEventTrackingLog(GeneralViewTrackingLog):
    def __init__(self, driver):
        super.__init__(driver)
        self.sentinel_event_tracking_log_date_reported = self.driver.instance.find_element(By.XPATH, "//input[@name='reportDate']")
        self.sentinel_event_tracking_log_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@name='patientMrNumber']")
        self.sentinel_event_tracking_log_incident_accident = self.driver.instance.find_element(By.XPATH, "//input[@name='incidentAccident']")
        self.sentinel_event_tracking_log_harm_caused = self.driver.instance.find_element(By.XPATH, "//input[@name='harmCaused']")
        self.sentinel_event_tracking_log_follow_up = self.driver.instance.find_element(By.XPATH, "//input[@name='followUp']")
        self.sentinel_event_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.sentinel_event_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")
