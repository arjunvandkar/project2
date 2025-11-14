from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.common.by import By

class LoginPage(Browser):
    txt_email_id="Email"
    txt_password_id="Password"
    btn_login_xpath="//input[@class='button-1 login-button']"
    msg_welcome_xpath="//h2[@class='topic-html-content-header']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.txt_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def isLoggedIn(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_welcome_xpath).is_displayed()
        except:
            return False


