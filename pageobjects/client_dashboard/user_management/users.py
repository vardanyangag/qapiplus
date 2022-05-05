from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Users:
    def __init__(self,driver):
        self.driver = driver
        self.users_show_deactivated_users = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")
        self.users_add_new_user = self.driver.instance.find_element(By.XPATH, "//*[@name='tenancyName']")

