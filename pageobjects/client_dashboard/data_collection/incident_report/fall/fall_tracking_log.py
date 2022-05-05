from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class FallTrackingLog(GeneralViewTrackingLog):
    def __init__(self,driver):
        super.__init__(driver)
        self.fall_tracking_log_date_of_fall = self.driver.instance.find_element(By.XPATH, "//input[@name='dateOfFall']")
        self.fall_tracking_log_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@name='patientMRNumber']")
        self.fall_tracking_log_md_diagnosis = self.driver.instance.find_element(By.XPATH, "//input[@name='diagnosis']")
        self.fall_tracking_log_injury = self.driver.instance.find_element(By.XPATH, "//input[@name='injury']")
        self.fall_tracking_log_treatment = self.driver.instance.find_element(By.XPATH, "//input[@name='treatment']")
        self.fall_tracking_log_follow_up = self.driver.instance.find_element(By.XPATH, "//input[@name='followUp']")
        self.fall_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.fall_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")
