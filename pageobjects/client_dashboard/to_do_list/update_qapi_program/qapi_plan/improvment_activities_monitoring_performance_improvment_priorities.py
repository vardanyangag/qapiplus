from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImprovementActivitiesMonitoringPerformanceImprovementPriorities:
    def __init__(self, driver):
        self.driver = driver
        self.improvement_activities_monitoring_performance_improvement_priorities_date = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.improvement_activities_monitoring_performance_improvement_priorities_approve = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.improvement_activities_monitoring_performance_improvement_priorities_edit = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
