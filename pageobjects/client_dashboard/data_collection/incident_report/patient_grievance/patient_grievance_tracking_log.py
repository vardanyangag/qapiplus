from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class PatienTGrievanceTrackingLog(GeneralViewTrackingLog):
    def __init__(self, driver):
        super.__init__(driver)
        self.patient_grievance_tracking_log_report_date = self.driver.instance.find_element(By.XPATH, "//input[@name='reportDate']")
        self.patient_grievance_tracking_log_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@name='patientMrNumber']")
        self.patient_grievance_tracking_log_complaint = self.driver.instance.find_element(By.XPATH, "//input[@name='complaint']")
        self.patient_grievance_tracking_log_resolved = self.driver.instance.find_element(By.XPATH, "//input[@name='resolved']")
        self.patient_grievance_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.patient_grievance_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")
