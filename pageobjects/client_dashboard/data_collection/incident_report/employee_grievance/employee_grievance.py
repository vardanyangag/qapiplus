from selenium.webdriver.common.by import By


class EmployeeGrievance:
    def __init__(self,driver):
        self.driver = driver
        self.employee_grievance_name_of_employee = self.driver.instance.find_element(By.XPATH, "//input[@id='NameOfEmployee']")
        self.employee_grievance_report_date = self.driver.instance.find_element(By.XPATH, "//input[@id='ReportDate']")
        self.employee_grievance_grievance_complaint = self.driver.instance.find_element(By.XPATH, "//input[@id='Grievance']")
        self.employee_grievance_how_would_the_employee_like_this_issue_resolved = self.driver.instance.find_element(By.XPATH, "//input[@id='EmployeeLikeIssueResolved']")
        self.employee_grievance_was_the_issue_resolved_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='WasTheIssueResolved']")
        self.employee_grievance_was_the_issue_resolved_no = self.driver.instance.find_element(By.XPATH, "//input[@id='WasTheIssueResolved']")
        self.employee_grievance_explain = self.driver.instance.find_element(By.XPATH, "//input[@id='IssueResolvedExplain']")
        self.employee_grievance_next_step = self.driver.instance.find_element(By.XPATH, "//input[@id='NextSteps']")
        self.employee_grievance_follow_up = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowUp']")
        self.employee_grievance_referreed_to = self.driver.instance.find_element(By.XPATH, "//input[@id='ReferredToId']")
        self.employee_grievance_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.employee_grievance_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.employee_grievance_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='AddEmployeeGrievance']")
        self.employee_grievance_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='AddEmployeeGrievanceCancel']")
        self.employee_grievance_view_tracking_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")