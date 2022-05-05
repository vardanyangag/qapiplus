from selenium.webdriver.common.by import By


class ToDoList:
    def __init__(self,driver):
        self.driver = driver
        self.update_qapi_program = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_infection_control_program = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.update_emergancy_management_program = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.staff_in_service = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.leadership = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")