import pytest
import time
import datetime
from Pages import LoginPage

class Test_002_Login:

    def test_incorrect_login(self, setup):

        self.username = "yash.chindalia@rsystems.com"
        self.password = "Tero!@34"

        self._driver = setup
        self.lp = LoginPage.Login(self._driver)

        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        time.sleep(10)

    def test_login(self, setup):

        self.username = "yash.chindalia@rsystems.com"
        self.password = "Hero!@34"

        self._driver = setup
        self.lp = LoginPage.Login(self._driver)

        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        time.sleep(10)