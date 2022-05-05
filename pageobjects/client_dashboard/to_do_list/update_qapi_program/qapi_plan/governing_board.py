from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoverningBoard:
    def __init__(self, driver):
        self.driver = driver
        self.governing_board_date = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.governing_board_approve = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.governing_board_edit = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
