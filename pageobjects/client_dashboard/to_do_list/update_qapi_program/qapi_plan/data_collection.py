from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataCollection:
    def __init__(self, driver):
        self.driver = driver
        self.data_collection_date = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.data_collection_approve = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.data_collection_edit = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
