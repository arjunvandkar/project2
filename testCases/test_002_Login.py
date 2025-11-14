import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
from utilities.screenshot_util import capture_screenshot


class Test_Login():
    base_url =ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("*** Starting test_002_login ***")
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isLoggedIn()
        if self.targetpage==True:
            assert True
        else:
            capture_screenshot(self.driver,"test_login")
            assert False

        self.driver.close()
        self.logger.info("*** End of test_002_login ***")



