from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    email_address_field_id = "input-email"
    password_field_xpath = "input-password"
    login_button_xpath = "//input[@value='Login']"
    login_warning_message_xpath = "//div[@id='account-login']/div[1]"


    def enter_email_address(self,email):
        self.driver.find_element(By.ID,self.email_address_field_id).click()
        self.driver.find_element(By.ID,self.email_address_field_id).clear()
        self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.password_field_xpath).click()
        self.driver.find_element(By.ID, self.password_field_xpath).clear()
        self.driver.find_element(By.ID, self.password_field_xpath).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def verify_login_error_message(self,error_text):
        return (self.driver.find_element(By.XPATH,self.login_warning_message_xpath).text
         .__contains__(error_text))