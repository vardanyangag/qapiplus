from selenium.webdriver.common.by import By

class SentinelEvent:
    _wait_timeout = 20
    def __init__(self,driver):
        self.driver = driver
        self.sentinel_event_patient_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@id='PatientMrNumber']")
        self.sentinel_event_report_date = self.driver.instance.find_element(By.XPATH, "//input[@id='ReportDate']")
        self.sentinel_event_type_of_reaction = self.driver.instance.find_element(By.XPATH, "//input[@id='TypeOfReaction']")
        self.sentinel_event_was_adverse_reaction_due_to_a_food_or_drug_interaction_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='FoodDrugInteraction']")
        self.sentinel_event_was_adverse_reaction_due_to_a_food_or_drug_interaction_no = self.driver.instance.find_element(By.XPATH, "//input[@id='FoodDrugInteraction']")
        self.sentinel_event_was_adverse_reaction_due_to_a_food_or_drug_interaction_unknown = self.driver.instance.find_element(By.XPATH, "//input[@id='FoodDrugInteraction']")
        self.sentinel_event_explain = self.driver.instance.find_element(By.XPATH, "//input[@id='ExplainAdverseReactions']")
        self.sentinel_event_staff_member_present_when_incident_occured_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='StaffPresence']")
        self.sentinel_event_staff_member_present_when_incident_occured_no = self.driver.instance.find_element(By.XPATH, "//input[@id='StaffPresence']")
        self.sentinel_event_describe = self.driver.instance.find_element(By.XPATH, "//input[@id='DescribeStaffPresence']")
        self.sentinel_event_witness_other_than_staff_member_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='OtherThanStaffPresence']")
        self.sentinel_event_witness_other_than_staff_member_no = self.driver.instance.find_element(By.XPATH, "//input[@id='OtherThanStaffPresence']")
        self.sentinel_event_witness_name = self.driver.instance.find_element(By.XPATH, "//input[@id='WitnessName']")
        self.sentinel_event_witness_phone_number = self.driver.instance.find_element(By.XPATH, "//input[@id='WitnessPhoneNumber']")
        self.sentinel_event_relationship_to_patient = self.driver.instance.find_element(By.XPATH, "//input[@id='RelationshipToPatient']")
        self.sentinel_event_describe_incident_accident_adverse_event = self.driver.instance.find_element(By.XPATH, "//input[@id='DescibeIncident']")
        self.sentinel_event_harm_caused_to_patient = self.driver.instance.find_element(By.XPATH, "//input[@id='HarmCauseId']")
        self.sentinel_event_investigation_fallow_up = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowUp']")
        self.sentinel_event_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.sentinel_event_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.sentinel_event_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='AddSentinelEvent']")
        self.sentinel_event_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='AddSentinelEventCancel']")
        self.sentinel_event_view_tracking_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")