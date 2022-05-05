from selenium.webdriver.common.by import By


class AdverseDrugReaction:
    def __init__(self,driver):
        self.driver = driver
        self.adverse_drug_reaction_patient_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@id='PatientMrNumber']")
        self.adverse_drug_reaction_report_date = self.driver.instance.find_element(By.XPATH, "//input[@name='ReportDate']")
        self.adverse_drug_reaction_type_of_reaction = self.driver.instance.find_element(By.XPATH, "//input[@id='TypeOfReaction']")
        self.adverse_drug_reaction_was_adverse_reaction_due_to_a_food_or_drug_interaction_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='FoodDrugInteraction']")
        self.adverse_drug_reaction_was_adverse_reaction_due_to_a_food_or_drug_interaction_no = self.driver.instance.find_element(By.XPATH, "//input[@id='FoodDrugInteraction']")
        self.adverse_drug_reaction_was_adverse_reaction_due_to_a_food_or_drug_interaction_unknown = self.driver.instance.find_element(By.XPATH, "//input[@id='FoodDrugInteraction']")
        self.adverse_drug_reaction_explain = self.driver.instance.find_element(By.XPATH, "//input[@id='ExplainAdverseReactions']")
        self.adverse_drug_reaction_reaction_reported_to = self.driver.instance.find_element(By.XPATH, "//*[@id='AdverseDrugReactionReportForm']/div[2]/div[4]/div/div/div/button")
        self.adverse_drug_reaction_date_reported = self.driver.instance.find_element(By.XPATH, "//input[@name='DateReported']")
        self.adverse_drug_reaction_action_taken = self.driver.instance.find_element(By.XPATH, "//select[@id='ActionTakenId']")
        self.adverse_drug_reaction_investigation_follow_up = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowUp']")
        self.adverse_drug_reaction_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.adverse_drug_reaction_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.adverse_drug_reaction_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='AddAdverseDrugReaction']")
        self.adverse_drug_reaction_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='AddAdverseDrugReactionCancel']")
        self.adverse_drug_reaction_view_tracking_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")
