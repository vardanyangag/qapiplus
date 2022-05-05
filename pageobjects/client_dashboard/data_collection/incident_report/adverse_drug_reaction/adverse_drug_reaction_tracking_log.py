from selenium.webdriver.common.by import By
from pageobjects.client_dashboard.data_collection.incident_report.general_view_tracking_log import GeneralViewTrackingLog

class AdverseDrugReactionTrackingLog(GeneralViewTrackingLog):
    def __init__(self,driver):
        super.__init__(driver)
        self.adverse_drug_reaction_tracking_log_report_date = self.driver.instance.find_element(By.XPATH, "//input[@name='reportDate']")
        self.adverse_drug_reaction_tracking_log_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@name='patientMrNumber']")
        self.adverse_drug_reaction_tracking_log_reaction_type = self.driver.instance.find_element(By.XPATH, "//input[@name='typeOfReaction']")
        self.adverse_drug_reaction_tracking_log_food_drug_interaction = self.driver.instance.find_element(By.XPATH, "//input[@name='foodDrugInteraction']")
        self.adverse_drug_reaction_tracking_log_action_taken = self.driver.instance.find_element(By.XPATH, "//input[@name='actionTaken']")
        self.adverse_drug_reaction_tracking_log_status = self.driver.instance.find_element(By.XPATH, "//input[@name='isActive']")
        self.adverse_drug_reaction_tracking_log_actions = self.driver.instance.find_element(By.XPATH, "//input[@name='actions']")