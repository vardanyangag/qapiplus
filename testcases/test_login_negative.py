import unittest
from webdriver import Driver
from values import strings
from pageobjects.login import Login


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)
        self.Qapiplus = Login(self.driver)

    def test_password_warning(self):
        self.Qapiplus.validate_password_error()

    def test_login_warning(self):
        self.Qapiplus.validate_username_error()

    def tearDown(self) -> None:
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
