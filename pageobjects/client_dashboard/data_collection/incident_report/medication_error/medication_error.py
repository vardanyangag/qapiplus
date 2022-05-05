from selenium.webdriver.common.by import By


class MedicationError:
    def __init__(self,driver):
        self.driver = driver
        self.medication_error_patient_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@id='PatientMRNumber']")
        self.medication_error_report_date = self.driver.instance.find_element(By.XPATH, "//input[@id='ReportDate']")
        self.medication_error_medication_name = self.driver.instance.find_element(By.XPATH, "//input[@id='MedicationName']")
        self.medication_error_medication_dose = self.driver.instance.find_element(By.XPATH, "//input[@id='MedicationDose']")
        self.medication_error_medication_frequnecy = self.driver.instance.find_element(By.XPATH, "//input[@id='MedicationFrequency']")
        self.medication_error_type_of_error = self.driver.instance.find_element(By.XPATH, "//select[@id='ErrorId']")
        self.medication_error_possible_cause_of_error = self.driver.instance.find_element(By.XPATH, "//select[@id='ErrorCauseId']")
        self.medication_error_did_medication_error_cause_harm_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='IsMedicationHarmed']")
        self.medication_error_did_medication_error_cause_harm_no = self.driver.instance.find_element(By.XPATH, "//input[@id='IsMedicationHarmed']")
        self.medication_error_explain_error_cause = self.driver.instance.find_element(By.XPATH, "//input[@id='MedicationHarmDetails']")
        self.medication_error_did_medication_error_reported_to = self.driver.instance.find_element(By.XPATH, "//*[@id='MedicationErrorReportForm']/div[2]/div[7]/div[1]/div/div/button")
        self.medication_error_date_reported = self.driver.instance.find_element(By.XPATH, "//input[@id='DateReported']")
        self.medication_error_employee_involved_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='IsEmployeeInvolved']")
        self.medication_error_employee_involved_no = self.driver.instance.find_element(By.XPATH, "//input[@id='IsEmployeeInvolved']")
        self.medication_error_employee_involved_comment = self.driver.instance.find_element(By.XPATH, "//input[@id='InvolvedEmployeeComment']")
        self.medication_error_did_medication_order_change_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='IsMedicationOrderChanged']")
        self.medication_error_did_medication_order_change_no = self.driver.instance.find_element(By.XPATH, "//input[@id='IsMedicationOrderChanged']")
        self.medication_error_did_medication_order_change_explain = self.driver.instance.find_element(By.XPATH, "//input[@id='MedicationOrderChangedDetails']")
        self.medication_error_treatment = self.driver.instance.find_element(By.XPATH, "//input[@id='TreatmentId']")
        self.medication_error_date_of_fallow_up = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowUpDate']")
        self.medication_error_follow_up = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowUp']")
        self.medication_error_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.medication_error_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.medication_error_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='AddMedicationError']")
        self.medication_error_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='AddMedicationErrorCancel']")
        self.medication_error_view_tracking_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")
