from selenium.webdriver.common.by import By


class DataCollection:
    def __init__(self, driver):
        self.driver = driver
        self.incident_report = self.driver.instance.find_element(By.XPATH, "//a[@id='DataCollectionBox1']")
        self.clinical_audit = self.driver.instance.find_element(By.XPATH, "//a[@id='DataCollectionBox2']")
        self.human_recource_audit = self.driver.instance.find_element(By.XPATH, "//a[@id='DataCollectionBox3']")
        self.supervisory_visits = self.driver.instance.find_element(By.XPATH,"//a[@id='DataCollectionBox3']" )
