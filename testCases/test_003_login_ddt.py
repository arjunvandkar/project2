import time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.screenshot_util import capture_screenshot
import os


class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    path = os.path.join(os.getcwd(), "testdata", "Demo_Web_ShopDDT.xlsx")

    def test_login_ddt(self, setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []
        failure_rows = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2, self.rows + 1):
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            # normalize expected value to avoid whitespace/case issues
            self.exp = (XLUtils.readData(self.path, "Sheet1", r, 3) or "").strip().title()

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(2)
            self.targetpage = self.lp.isLoggedIn()

            row_id = f"row{r}_{self.email}"

            if self.exp == 'Valid':
                if self.targetpage:
                    lst_status.append('Pass')
                    # safe logout
                    try:
                        self.ma.clickLogout()
                    except Exception:
                        self.logger.warning(f"Logout not available after valid login for {row_id}")
                else:
                    lst_status.append('Fail')
                    failure_rows.append((r, self.email, "Expected Valid but login failed"))
                    capture_screenshot(self.driver, f"login_ddt_fail_{row_id}")
            elif self.exp == 'Invalid':
                if self.targetpage:
                    lst_status.append('Fail')
                    failure_rows.append((r, self.email, "Expected Invalid but login succeeded"))
                    # attempt safe logout so next iteration starts clean
                    try:
                        self.ma.clickLogout()
                    except Exception:
                        self.logger.warning(f"Logout not available after unexpected success for {row_id}")
                    capture_screenshot(self.driver, f"login_ddt_unexpected_success_{row_id}")
                else:
                    lst_status.append('Pass')
