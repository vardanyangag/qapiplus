from selenium.webdriver.common.by import By


class GeneralViewTrackingLog:
    def __init__(self, driver):
        self.driver = driver
        self.general_view_tracking_log_print_selected = self.driver.instance.find_element(By.XPATH, "//a[@id='lnkPrintSelectedRecords']")
        self.general_view_tracking_log_print_entire_table = self.driver.instance.find_element(By.XPATH, "//a[@id='Print']")
        self.general_view_tracking_log_back = self.driver.instance.find_element(By.XPATH, "//a[@id='backFromTraker']")
        self.general_view_tracking_log_from = self.driver.instance.find_element(By.XPATH, "//table[@class='table-condensed']")
        self.general_view_tracking_log_to = self.driver.instance.find_element(By.XPATH, "//table[@class='table-condensed']")
        self.general_view_tracking_log_quarter = self.driver.instance.find_element(By.XPATH, "//select[@id='Quarter']")
        self.general_view_tracking_log_year = self.driver.instance.find_element(By.XPATH, "//input[@id='Year']")
        self.general_view_tracking_log_search = self.driver.instance.find_element(By.XPATH, "//button[@id='Search']")
        self.general_view_tracking_log_clear = self.driver.instance.find_element(By.XPATH, "//button[@id='ClearSearch']")
        self.general_view_tracking_log_show_deactivated_records = self.driver.instance.find_element(By.XPATH,"//span[@class='slider round']")