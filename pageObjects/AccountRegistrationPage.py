from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    rdo_gender_male_id="gender-male"
    rdo_gender_female_id = "gender-female"
    txt_Firstname_id="FirstName"
    txt_Lastname_id="LastName"
    txt_Email_id="Email"
    txt_Password_id="Password"
    txt_Confirmpassword_id = "ConfirmPassword"
    btn_Register_xpath="//input[@id='register-button']"
    text_msg_conf_xpath = "//div[@class='result']"

    def __init__(self,driver):
        self.driver=driver

    def selectGendermale(self):
        self.driver.find_element(By.ID,self.rdo_gender_male_id).click()

    def selectGenderfemale(self):
        self.driver.find_element(By.ID,self.rdo_gender_female_id).click()

    def setFirstname(self,fname):
        self.driver.find_element(By.ID,self.txt_Firstname_id).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.ID,self.txt_Lastname_id).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_Email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.txt_Password_id).send_keys(password)

    def setConfirmpassword(self,Cpassword):
        self.driver.find_element(By.ID,self.txt_Confirmpassword_id).send_keys(Cpassword)

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_Register_xpath).click()

    def getconfirmationmsg(self):
        try:
            return  self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None







