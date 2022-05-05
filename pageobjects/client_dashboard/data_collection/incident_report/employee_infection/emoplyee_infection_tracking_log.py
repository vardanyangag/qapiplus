from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class EmoplyeeInfectionTrackingLog(GeneralViewTrackingLog):
    def __init__(self,driver):
        super.__init__(driver)
        self.employee_infection_tracking_log_reported_date = self.driver.instance.find_element(By.XPATH, "//input[@name='reportDate']")
        self.employee_infection_tracking_log_name = self.driver.instance.find_element(By.XPATH, "//input[@name='employeeName']")
        self.employee_infection_tracking_log_treatment = self.driver.instance.find_element(By.XPATH, "//input[@name='treatment']")
        self.employee_infection_tracking_log_infection_type = self.driver.instance.find_element(By.XPATH, "//input[@name='infectionType']")
        self.employee_infection_tracking_log_treated = self.driver.instance.find_element(By.XPATH, "//input[@name='isTreated']")
        self.employee_infection_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.employee_infection_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")