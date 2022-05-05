from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddSection:
    def __init__(self, driver):
        self.driver = driver
        self.add_section_section_header = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.add_section_input_text = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.add_section_save_changes = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.add_section_delete_section = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.add_section_cancel = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.add_section_date = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.add_section_approve = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.add_section_edit = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
