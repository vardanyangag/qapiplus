from selenium.webdriver.common.by import By

class PatientInfection:
    def __init__(self,driver):
        self.driver = driver
        self.patient_infection_patient_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@id='PatientMRNumber']")
        self.patient_infection_reported_date = self.driver.instance.find_element(By.XPATH, "//input[@id='ReportDate']")
        self.patient_infection_soc_date = self.driver.instance.find_element(By.XPATH, "//input[@id='SOCDate']")
        self.patient_infection_diagnosis = self.driver.instance.find_element(By.XPATH, "//input[@id='Diagnosis']")
        self.patient_infection_treated_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='IsTreated']")
        self.patient_infection_treated_no = self.driver.instance.find_element(By.XPATH, "//input[@id='IsTreated']")
        self.patient_infection_reported_by = self.driver.instance.find_element(By.XPATH, "//input[@id='ReportedBy']")
        self.patient_infection_type_of_suspected_infection = self.driver.instance.find_element(By.XPATH, "//select[@id='InfectionTypeId']")
        self.patient_infection_infection_subtype = self.driver.instance.find_element(By.XPATH, "//select[@id='InfectionSubTypeId']")
        self.patient_infection_has_the_md_been_notified_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='IsMDNotified']")
        self.patient_infection_has_the_md_been_notified_no = self.driver.instance.find_element(By.XPATH, "//input[@id=''IsMDNotified']")
        self.patient_infection_notification_date = self.driver.instance.find_element(By.XPATH, "//input[@id='NotifiedDate']")
        self.patient_infection_is_this_a_reportable_infection_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportableInfection']")
        self.patient_infection_is_this_a_reportable_infection_no = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportableInfection']")
        self.patient_infection_discribe = self.driver.instance.find_element(By.XPATH, "//input[@id='ReportableInfectionExplanation']")
        self.patient_infection_new_orders_medications = self.driver.instance.find_element(By.XPATH, "//input[@id='OrdersOrMedications']")
        self.patient_infection_follow_up_resolution = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowupOrResolution']")
        self.patient_infection_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.patient_infection_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.patient_infection_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='AddPatientInfection']")
        self.patient_infection_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='AddPatientInfectionCancel']")
        self.patient_infection_view_tracking_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")
