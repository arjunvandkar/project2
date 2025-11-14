from selenium.webdriver.common.by import By

class HomePage():

    button_register_xpath="//a[normalize-space()='Register']"
    button_login_cssselector=".ico-login"


    def __init__(self,driver):
        self.driver=driver

    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.button_register_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_login_cssselector).click()


