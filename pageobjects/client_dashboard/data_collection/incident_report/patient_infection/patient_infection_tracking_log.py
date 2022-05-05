from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class PatientInfectionTrackingLog(GeneralViewTrackingLog):
    def __init__(self, driver):
        super.__init__(driver)
        self.patient_infection_tracking_log_report_date = self.driver.instance.find_element(By.XPATH, "//input[@name='reportDate']")
        self.patient_infection_tracking_log_soc_date = self.driver.instance.find_element(By.XPATH, "//input[@name='socDate']")
        self.patient_infection_tracking_log_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@name='patientMRNumber']")
        self.patient_infection_tracking_log_infection_type = self.driver.instance.find_element(By.XPATH, "//input[@name='infectionType']")
        self.patient_infection_tracking_log_infection_sub_type = self.driver.instance.find_element(By.XPATH, "//input[@name='infectionSubType']")
        self.patient_infection_tracking_log_treated = self.driver.instance.find_element(By.XPATH, "//input[@name='isTreated']")
        self.patient_infection_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.patient_infection_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")
