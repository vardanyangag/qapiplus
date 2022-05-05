from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QuarterlyReport:
    def __init__(self,driver):
        self.driver = driver
        self.quarterly_report_select_year = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_quarter_1 = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_quarter_2 = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_quarter_3 = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_quarter_4 = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_annual = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_january = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_february = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_march = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_entire_quarter = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_submit = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_cancel = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_print_this_page = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.quarterly_report_edit = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")