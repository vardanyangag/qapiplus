from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class HospitalizationTrackingLog(GeneralViewTrackingLog):
    def __init__(self, driver):
        super.__init__(driver)
        self.hospitalization_tracking_log_hospitalization_date = self.driver.instance.find_element(By.XPATH, "//input[@name='dateOfHospitalization']")
        self.hospitalization_tracking_log_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@name='patientMrNumber']")
        self.hospitalization_tracking_log_soc_date = self.driver.instance.find_element(By.XPATH, "//input[@name='socDate']")
        self.hospitalization_tracking_log_reason = self.driver.instance.find_element(By.XPATH, "//input[@name='reason']")
        self.hospitalization_tracking_log_admision_detail = self.driver.instance.find_element(By.XPATH, "//input[@name='admissionDetailType']")
        self.hospitalization_tracking_log_type_of_service = self.driver.instance.find_element(By.XPATH, "//input[@name='typeOfServiceType']")
        self.hospitalization_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.hospitalization_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")
