from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class MedicationErrorTrackingLog(GeneralViewTrackingLog):
    def __init__(self, driver):
        super.__init__(driver)
        self.medication_error_tracking_log_report_date = self.driver.instance.find_element(By.XPATH, "//input[@name='reportDate']")
        self.medication_error_tracking_log_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@name='patientMRNumber']")
        self.medication_error_tracking_log_error_type = self.driver.instance.find_element(By.XPATH, "//input[@name='errorTypeName']")
        self.medication_error_tracking_log_harm_caused = self.driver.instance.find_element(By.XPATH, "//input[@name='IsMedicationHarmed']")
        self.medication_error_tracking_log_treatment = self.driver.instance.find_element(By.XPATH, "//input[@name='errorTreatmentName']")
        self.medication_error_tracking_log_employee_involved = self.driver.instance.find_element(By.XPATH, "//input[@name='isEmployeeInvolved']")
        self.medication_error_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.medication_error_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")
