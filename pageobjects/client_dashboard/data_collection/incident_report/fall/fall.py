from selenium.webdriver.common.by import By


class Fall:
    def __init__(self,driver):
        self.driver = driver
        self.fall_patient_mr_number = self.driver.instance.find_element(By.XPATH, "//input[@id='PatientMRNumber']")
        self.fall_date_of_fall = self.driver.instance.find_element(By.XPATH, "//input[@id='DateOfFall']")
        self.fall_diagnosis = self.driver.instance.find_element(By.XPATH, "//input[@id='Diagnosis']")
        self.fall_date_reported_to_agency = self.driver.instance.find_element(By.XPATH, "//input[@id='AgencyReportedDate']")
        self.fall_was_the_fall_witnessed = self.driver.instance.find_element(By.XPATH, "//select[@id='WasFallWitnessedId']")
        self.fall_precipitating_event = self.driver.instance.find_element(By.XPATH, "//select[@id='PrecipitatingEventId']")
        self.fall_what_was_the_patient_doing_at_the_time_of_fall = self.driver.instance.find_element(By.XPATH, "//select[@id='WhatWasPatientDoingId']")
        self.fall_where_did_the_fall_occur = self.driver.instance.find_element(By.XPATH, "//select[@id='WhereFallOccurId']")
        self.fall_patient_residesAt = self.driver.instance.find_element(By.XPATH, "//select[@id='PatientResidesAtId']")
        self.fall_caregiver_presence = self.driver.instance.find_element(By.XPATH, "//select[@id='CaregiverPresenceId']")
        self.fall_injury_caused_by_fall = self.driver.instance.find_element(By.XPATH, "//select[@id='InjuryCausedByFallId']")
        self.fall_describe = self.driver.instance.find_element(By.XPATH, "//input[@id='InjuryCausedByFall']")
        self.fall_list_any_safety_hazards_that_may_have_caused_or_contributed_to_the_fall = self.driver.instance.find_element(By.XPATH, "//select[@id='SafetyHazardId']")
        self.fall_treatment_patient_received_for_the_fall = self.driver.instance.find_element(By.XPATH, "//*[@id='FallReportForm']/div[2]/div[11]/div[1]/div/div/button/span")
        self.fall_post_fall_follow_up = self.driver.instance.find_element(By.XPATH, "//select[@id='PostFallFollowUpId']")
        self.fall_follow_up_detail = self.driver.instance.find_element(By.XPATH, "//select[@id='FollowUpDetailId']")
        self.fall_comments = self.driver.instance.find_element(By.XPATH, "//input[@id='Comments']")
        self.fall_reported_to_qapi_committee = self.driver.instance.find_element(By.XPATH, "//input[@id='IsReportedToQAPICommitee']")
        self.fall_submit = self.driver.instance.find_element(By.XPATH, "//button[@id='btnAddFall']")
        self.fall_cancel = self.driver.instance.find_element(By.XPATH, "//button[@id='btnAddFallCancel']")
        self.fall_view_tracking_log = self.driver.instance.find_element(By.XPATH, "//a[@class='view-tracking-log']")
