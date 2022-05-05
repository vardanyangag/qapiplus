from selenium.webdriver.common.by import By


class AbuseAndNeglect:
    def __init__(self,driver):
        self.driver = driver
        self.abuse_and_neglect_patient_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@id='PatientMRNumber']")
        self.abuse_and_neglect_date_reported = self.driver.instance.find_element(By.XPATH, "//input[@id='ReportDate']" )
        self.abuse_and_neglect_type_of_suspected_abuse_neglect = self.driver.instance.find_element(By.XPATH, "//select[@id='SuspectedTypeId']")
        self.abuse_and_neglect_brief_description_of_abuse = self.driver.instance.find_element(By.XPATH, "//input[@id='BriefDescriptionofAbuse']")
        self.abuse_and_neglect_when_did_abuse_occur = self.driver.instance.find_element(By.XPATH, "//input[@id='WhenDidAbuseOccur']")
        self.abuse_and_neglect_who_was_responsible_for_the_abuse = self.driver.instance.find_element(By.XPATH, "//input[@id='ResponsibleForAbuse']")
        self.abuse_and_neglect_occurances_may_include = self.driver.instance.find_element(By.XPATH, "//input[@id='OccurancesMayInclude']")
        self.abuse_and_neglect_signs_of_fear_related_to_any_caregiver_or_family_member_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='CaregiverFear']")
        self.abuse_and_neglect_signs_of_fear_related_to_any_caregiver_or_family_member_no = self.driver.instance.find_element(By.XPATH, "//input[@id='CaregiverFear']")
        self.abuse_and_neglect_signs_of_fear_related_to_any_caregiver_or_family_member_not_applicable = self.driver.instance.find_element(By.XPATH, "//input[@id='CaregiverFear']")
        self.abuse_and_neglect_describe_1 = self.driver.instance.find_element(By.XPATH, "//input[@id='CareGiverDescribe']")
        self.abuse_and_neglect_refusal_of_caregiver_to_leave_the_room_during_assessment_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='CaregiverRefusal']")
        self.abuse_and_neglect_refusal_of_caregiver_to_leave_the_room_during_assessment_no = self.driver.instance.find_element(By.XPATH, "//input[@id='CaregiverRefusal']")
        self.abuse_and_neglect_refusal_of_caregiver_to_leave_the_room_during_assessment_not_applicable = self.driver.instance.find_element(By.XPATH, "//input[@id='CaregiverRefusal']")
        self.abuse_and_neglect_describe_2 = self.driver.instance.find_element(By.XPATH, "//input[@id='CaregiverRefusalDescribe']")
        self.abuse_and_neglect_feeling_of_extreme_hoeplessness_or_helplessness_yes = self.driver.instance.find_element(By.XPATH, "//input[@id='FeelingHoeplessness']")
        self.abuse_and_neglect_feeling_of_extreme_hoeplessness_or_helplessness_no = self.driver.instance.find_element(By.XPATH, "//input[@id='FeelingHoeplessness']")
        self.abuse_and_neglect_feeling_of_extreme_hoeplessness_or_helplessness_not_applicable = self.driver.instance.find_element(By.XPATH, "//input[@id='FeelingHoeplessness']")
        self.abuse_and_neglect_describe_3 = self.driver.instance.find_element(By.XPATH, "//input[@id='FeelingHoeplessnessDescribe']")
        self.abuse_and_neglect_basic_needds_are_not_met = self.driver.instance.find_element(By.XPATH,"//*[@id='AbuseAndNeglectReportForm']/div[2]/div[10]/div[1]/div/div/button" )
        self.abuse_and_neglect_report_to = self.driver.instance.find_element(By.XPATH,"//*[@id='AbuseAndNeglectReportForm']/div[2]/div[10]/div[2]/div/div/button" )
        self.abuse_and_neglect_follow_up = self.driver.instance.find_element(By.XPATH, "//input[@id='FollowUp']")
        self.abuse_and_neglect_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.abuse_and_neglect_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.abuse_and_neglect_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='AddAbuseAndNeglect']")
        self.abuse_and_neglect_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='AddAbuseAndNeglectCancel']")
        self.abuse_and_neglect_view_tracking_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")

