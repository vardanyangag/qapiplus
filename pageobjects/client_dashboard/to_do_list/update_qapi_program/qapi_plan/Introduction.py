from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Introduction:
    def __init__(self,driver):
        self.driver = driver
        self.introduction_text_area = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.introduction_date = self.driver.instance.find_element(By.XPATH, "/html/body/div[4]/div[1]/table")
        self.introduction_approve = self.driver.instance.find_element(By.XPATH, "//*[@id='btnApprove']")
        self.introduction_edit = self.driver.instance.find_element(By.XPATH, "//*[@id='btnEditMode']")
