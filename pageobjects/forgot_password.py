from selenium.webdriver.common.by import By


class ForgotPassword:
    def __init__(self,driver):
        self.driver = driver

        self.client_id = self.driver.instance.find_element(By.XPATH, "//input[@name='tenancyName']")
        self.email_address = self.driver.instance.find_element(By.XPATH, "//input[@name='EmailAddress']")
        self.submit_button = self.driver.instance.find_element(By.XPATH, "//button[@type='submit']")