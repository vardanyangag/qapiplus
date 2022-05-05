from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Armine:
    def __init__(self, driver):
        self.driver = driver
        self.armine_date = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.armine_approve = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.armine_edit = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")

