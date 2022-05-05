from selenium.webdriver.common.by import By


class PatientGrievance:
    def __init__(self,driver):
        self.driver = driver
        self.patient_grievance_report_date = self.driver.instance.find_element(By.XPATH, "//input[@id='ReportDate']")
        self.patient_grievance_name_of_caller = self.driver.instance.find_element(By.XPATH, "//input[@id='NameOfCaller']")
        self.patient_grievance_phone_number = self.driver.instance.find_element(By.XPATH, "//input[@id='PhoneNumber']")
        self.patient_grievance_relationship_to_patient = self.driver.instance.find_element(By.XPATH, "//input[@id='RelationshipToPatient']")
        self.patient_grievance_name_of_patient = self.driver.instance.find_element(By.XPATH, "//input[@id='NameOfPatient']")
        self.patient_grievance_patient_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@id='PatientMrNumber']")
        self.patient_grievance_grievance = self.driver.instance.find_element(By.XPATH, "//input[@id='Grievance']")
        self.patient_grievance_how_would_the_caller_like_this_issue_resolved = self.driver.instance.find_element(By.XPATH, "//input[@id='CallerLikeIssueResolved']")
        self.patient_grievance_was_the_issue_resolved_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='WasTheIssueResolved']")
        self.patient_grievance_was_the_issue_resolved_no = self.driver.instance.find_element(By.XPATH, "//input[@id='WasTheIssueResolved']")
        self.patient_grievance_was_the_issue_resolved_explain = self.driver.instance.find_element(By.XPATH, "//input[@id='IssueResolvedExplain']")
        self.patient_grievance_follow_up = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowUp']")
        self.patient_grievance_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.patient_grievance_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.patient_grievance_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='AddPatientGrievance']")
        self.patient_grievance_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='AddPatientGrievanceCancel']")
        self.patient_grievance_view_tracing_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")