from selenium.webdriver.common.by import By


class UpdateQapiProgram:
    def __init__(self,driver):
        self.driver = driver
        self.update_qapi_program_home = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_to_do_list = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_qapi_plan = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_quarterly_report = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_qapi_report = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_pi_meeting = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_pi_project = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_introduction = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_data_collection = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_data_analysis = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_improvment_activities_monitoring_performance_improvment_priorities = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_pips = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_governing_board = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_new_section_added = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_armine = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_something = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_qapi_program_added_section = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")

