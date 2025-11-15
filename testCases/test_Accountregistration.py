    import pytest
from webdriver_manager.core import driver

from utilities.randomStringGenerator import random_email
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities.screenshot_util import capture_screenshot
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen      #for logging

class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()    #for logging

    @pytest.mark.sanity
    def test_account_reg(self,setup):
        self.logger.info("***Test_001_AccountRegistration started***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching application...")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("clicking on MyAccount--> Register")
        self.hp.clickRegister()

        self.logger.info("Providing customer details for registration")
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.selectGendermale()
        self.regpage.setFirstname("Akshu")
        self.regpage.setLastname("Gaikwad")
        self.regpage.setEmail(random_email())
        self.regpage.setPassword("Akshu1")
        self.regpage.setConfirmpassword("Akshu1")
        self.regpage.clickContinue()
        self.regpage.getconfirmationmsg()
        msg =self.regpage.getconfirmationmsg()
        try:
            assert "registration completed" in msg.lower()
            print(" Registration test passed.")
            self.logger.info("Account Registration test passed.")
        except AssertionError:
            self.logger.exception("Assertion failed in account registration.")
            capture_screenshot(self.driver, "test_account_reg")
            raise
        except Exception:
            self.logger.exception("Unexpected error during account registration.")
            capture_screenshot(self.driver, "test_account_reg")
            raise



