from selenium.webdriver.common.by import By


class EmployeeInfection:
    def __init__(self,driver):
        self.driver = driver
        self.employee_infection_employee_name = self.driver.instance.find_element(By.XPATH, "//input[@id='EmployeeName']")
        self.employee_infection_reported_date = self.driver.instance.find_element(By.XPATH, "//input[@id='ReportDate']")
        self.employee_infection_infection_type = self.driver.instance.find_element(By.XPATH, "//select[@id='InfectionTypeId']")
        self.employee_infection_treatment = self.driver.instance.find_element(By.XPATH, "//select[@id='TreatmentTypeId']")
        self.employee_infection_treated_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='IsTreated']")
        self.employee_infection_treated_no = self.driver.instance.find_element(By.XPATH, "//input[@id='IsTreated']")
        self.employee_infection_reported_to = self.driver.instance.find_element(By.XPATH, "//*[@id='EmployeeInfectionReportForm']/div[2]/div[4]/div[2]/div/div/button")
        self.employee_infection_follow_up_resolution = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowUp']")
        self.employee_infection_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.employee_infection_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.employee_infection_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='AddEmployeeInfection']")
        self.employee_infection_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='AddEmployeeInfectionCancel']")
        self.employee_infection_view_tracking_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")
