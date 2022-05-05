from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class Login:
    def __init__(self,driver):
        self.driver = driver
        self.qapiplus_img = self.driver.instance.find_element(By.XPATH,"//img[@id='logoImgId']")
        self.login_text = self.driver.instance.find_element(By.XPATH, "//div[@id='LoginInTopLbl']")
        self.client_id_text = self.driver.instance.find_element(By.XPATH,"//label[@id='ClientIdLbl']")
        self.client_id = self.driver.instance.find_element(By.XPATH, "//input[@name='tenancyName']")
        self.username_text = self.driver.instance.find_element(By.XPATH,"//label[@id='UserNameOrEmailLbl']")
        self.username = self.driver.instance.find_element(By.XPATH, "//input[@name='usernameOrEmailAddress']")
        self.password_text = self.driver.instance.find_element(By.XPATH,"//label[@id='PasswordLbl']")
        self.password = self.driver.instance.find_element(By.XPATH, "//input[@name='password']")
        self.remember_me = self.driver.instance.find_element(By.XPATH, "//input[@name='rememberMe']")
        self.login_button = self.driver.instance.find_element(By.XPATH, "//button[@id='loginBtn']")
        self.forgot_password = self.driver.instance.find_element(By.XPATH, "//a[@id='forget-password']")
        self.copyright = self.driver.instance.find_element(By.XPATH, "//div[@class='copyright']")

    def validate_login_is_present(self):
        assert self.login_button.is_displayed()

    def validate_username_error(self):
        self.login_button.click()
        self.username_error = self.driver.instance.find_element(By.XPATH, "//span[@id='usernameOrEmailAddress-error']")
        assert self.username_error.is_displayed()
        assert self.username_error.text == "This field is required."

    def validate_password_error(self):
        self.login_button.click()
        self.password_error = self.driver.instance.find_element(By.XPATH,"//span[@id='password-error']")
        assert self.password_error.is_displayed()
        assert self.password_error.text == "This field is required."

    def login(self, client_id, username, password):
        self.client_id.send_keys(client_id)
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()

    def fill_login_form(self, client_id, username, password):
        self.client_id.send_keys(client_id)
        self.username.send_keys(username)
        self.password.send_keys(password)

    def press_enter(self):
        self.client_id.send_keys(Keys.RETURN)




