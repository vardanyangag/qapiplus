from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class EmployeeGrievanceTrackingLog(GeneralViewTrackingLog):
    def __init__(self,driver):
        super.__init__(driver)
        self.employee_grievance_tracking_log_report_date = self.driver.instance.find_element(By.XPATH, "//input[@name='reportDate']")
        self.employee_grievance_tracking_log_name = self.driver.instance.find_element(By.XPATH, "//input[@name='nameOfEmployee']")
        self.employee_grievance_tracking_log_complaint = self.driver.instance.find_element(By.XPATH, "//input[@name='complaint']")
        self.employee_grievance_tracking_log_resolved = self.driver.instance.find_element(By.XPATH, "//input[@name='resolved']")
        self.employee_grievance_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.employee_grievance_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")
