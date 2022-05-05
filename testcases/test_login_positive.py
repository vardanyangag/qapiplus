import unittest
from webdriver import Driver
from values import strings
from pageobjects.login import Login
from selenium.webdriver.common.keys import Keys
import time


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)
        self.Qapiplus = Login(self.driver)

    def test_login_by_login_button(self):
        self.Qapiplus.validate_login_is_present()
        self.Qapiplus.login(strings.client_id, strings.username,
                            strings.password)
        time.sleep(10)
        assert "ClientDashboard" in self.driver.instance.current_url

    def test_login_by_pressing_enter(self):
        self.Qapiplus.fill_login_form(strings.client_id, strings.username,
                                      strings.password)
        self.Qapiplus.press_enter()
        time.sleep(10)
        assert "ClientDashboard" in self.driver.instance.current_url

    def test_validate_cursor_in_clientid(self):
        active_element = self.driver.instance.switch_to.active_element
        assert active_element == self.Qapiplus.client_id

    def test_validate_tab_key(self):
        time.sleep(1)
        active_element = self.driver.instance.switch_to.active_element
        assert active_element == self.Qapiplus.client_id
        active_element.send_keys(Keys.TAB)
        time.sleep(1)
        active_element = self.driver.instance.switch_to.active_element
        assert active_element == self.Qapiplus.username
        active_element.send_keys(Keys.TAB)
        time.sleep(1)
        active_element = self.driver.instance.switch_to.active_element
        assert active_element == self.Qapiplus.password
        active_element.send_keys(Keys.TAB)
        time.sleep(1)
        active_element = self.driver.instance.switch_to.active_element
        assert active_element == self.Qapiplus.remember_me
        active_element.send_keys(Keys.TAB)
        time.sleep(1)
        active_element = self.driver.instance.switch_to.active_element
        assert active_element == self.Qapiplus.login_button

    def tearDown(self) -> None:
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
