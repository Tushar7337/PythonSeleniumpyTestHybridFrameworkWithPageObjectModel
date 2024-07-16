import time

from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self,driver):
        self.driver = driver

    first_name_field_xpath = "//input[@id='input-firstname']"
    last_name_field_xpath = "//input[@id='input-lastname']"
    email_field_xpath = "//input[@id='input-email']"
    phone_number_xpath = "//input[@id='input-telephone']"
    password_field_xpath = "//input[@id='input-password']"
    confirm_password_field_xpath = "//input[@id='input-confirm']"
    terms_and_condition_name = "agree"
    submit_button_xpath = "//input[@value='Continue']"
    account_created_successfully_text_xpath = "//div[@id='content']/h1"
    newsletter_yes_option_xpath = "//input[@name='newsletter'][@value='1']"

    error_message_while_account_creation_xpath = "//div[@id='account-register']/div[1]"
    terms_and_privacy_error_message = "//div[@id='account-register']/div[1]"
    first_name_error_message = "//input[@id='input-firstname']/following-sibling::div"
    last_name_error_message = "//input[@id='input-lastname']/following-sibling::div"
    email_error_message = "//input[@id='input-email']/following-sibling::div"
    phone_error_message = "//input[@id='input-telephone']/following-sibling::div"
    password_error_message = "//input[@id='input-password']/following-sibling::div"



    def enter_first_name(self,first_name):
        self.driver.find_element(By.XPATH,self.first_name_field_xpath).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.driver.find_element(By.XPATH,self.last_name_field_xpath).send_keys(last_name)

    def enter_email(self,email):
        self.driver.find_element(By.XPATH,self.email_field_xpath).send_keys(email)

    def enter_phone_number(self,phone):
        self.driver.find_element(By.XPATH,self.phone_number_xpath).send_keys(phone)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password_field_xpath).send_keys(confirm_password)

    def click_terms_and_condition_check_box(self):
        self.driver.find_element(By.NAME, self.terms_and_condition_name).click()

    def click_on_newsletter_yes_option(self):
        self.driver.find_element(By.XPATH,self.newsletter_yes_option_xpath).click()

    def click_on_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def register_an_account(self,first_name,last_name,email,phone,password,confirm_password,yes_or_no,privacy_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_phone_number(phone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        if yes_or_no.__eq__("yes"):
            self.click_on_newsletter_yes_option()
        if privacy_policy.__eq__("select"):
            self.click_terms_and_condition_check_box()
        time.sleep(10)
        self.click_on_submit_button()


    def verify_account_creation(self,expt_txt):
        return (self.driver.find_element(By.XPATH,self.account_created_successfully_text_xpath).text
         .__eq__(expt_txt))


    def verify_error_message_for_duplicate_email(self,expt_text):
        return (self.driver.find_element(By.XPATH,self.error_message_while_account_creation_xpath).text
         .__contains__(expt_text))

    def verify_error_message_for_privacy(self,expt_privacy_text):
        return (self.driver.find_element(By.XPATH,self.terms_and_privacy_error_message).text
         .__contains__(expt_privacy_text))

    def verify_error_for_first_name(self, expt_first_name_txt):
        return (self.driver.find_element(By.XPATH, self.first_name_error_message).text
                .__contains__(expt_first_name_txt))

    def verify_error_for_last_name(self, expt_last_name_txt):
        return (self.driver.find_element(By.XPATH, self.last_name_error_message).text
                .__contains__(expt_last_name_txt))

    def verify_error_for_email(self, expt_email_txt):
        return (self.driver.find_element(By.XPATH, self.email_error_message).text
                .__contains__(expt_email_txt))

    def verify_error_for_phone_number(self, expt_phone_txt):
        return (self.driver.find_element(By.XPATH, self.phone_error_message).text
                .__contains__(expt_phone_txt))

    def verify_error_for_password(self, expt_password_txt):
        return (self.driver.find_element(By.XPATH, self.password_error_message).text
                .__contains__(expt_password_txt))




