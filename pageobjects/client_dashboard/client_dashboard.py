from selenium.webdriver.common.by import By


class ClientDashboard:
    def __init__(self, driver):
        self.driver = driver
        self.user_info = self.driver.instance.find_element(By.XPATH,"//a[@id='headerDropDownId']")
        self.hi_username = self.driver.instance.find_element(By.XPATH,"//span[@id='userGreetingLbl']")
        self.pick_text = self.driver.instance.find_element(By.XPATH,"//span[@id='pickLblId']")
        self.data_collection = self.driver.instance.find_element(By.XPATH, "//a[@id='ClientDashboardBox1Id']")
        self.to_do_list = self.driver.instance.find_element(By.XPATH, "//a[@id='ClientDashboardBox2Id']")
        self.review_reports = self.driver.instance.find_element(By.XPATH, "//a[@id='ClientDashboardBox3Id']")
        self.user_management =self.driver.instance.find_element(By.XPATH, "//a[@id='ClientDashboardBox4Id']")
        self.my_profile =self.driver.instance.find_element(By.XPATH, "//a[@id='UserProfileChangePictureLink']")
        self.change_password =self.driver.instance.find_element(By.XPATH, "//a[@id='UserProfileChangePasswordLink']")
        self.logout =self.driver.instance.find_element(By.XPATH, "//a[@href ='/Account/Logout']")