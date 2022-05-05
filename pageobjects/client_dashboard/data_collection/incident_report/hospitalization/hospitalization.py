from selenium.webdriver.common.by import By


class Hospitalization:
    def __init__(self,driver):
        self.driver = driver

        self.hospitalization_patient_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@id='PatientMrNumber']")
        self.hospitalization_date_of_hospitalization = self.driver.instance.find_element(By.XPATH, "//input[@id='DateOfHospitalization']")
        self.hospitalization_soc_date = self.driver.instance.find_element(By.XPATH, "//input[@id='SocDate']")
        self.hospitalization_reason_for_hospitalization = self.driver.instance.find_element(By.XPATH, "//input[@id='ReasonForHospitalization']")
        self.hospitalization_admission_detail = self.driver.instance.find_element(By.XPATH, "//select[@id='AdmissionDetailId']")
        self.hospitalization_type_of_service = self.driver.instance.find_element(By.XPATH, "//select[@id='TypeOfServiceId']")
        self.hospitalization_follow_up = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowUp']")
        self.hospitalization_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.hospitalization_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.hospitalization_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='AddHospitalization']")
        self.hospitalization_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='AddHospitalizationCancel']")
        self.hospitalization_view_tracking_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")
