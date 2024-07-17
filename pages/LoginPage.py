from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    login_warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self,email):
        self.type_into_element(email,"email_address_field_id",self.email_address_field_id)

    def enter_password(self,password):
        self.type_into_element(password,"password_field_id",self.password_field_id)

    def click_on_login_button(self):
        self.element_click("login_button_xpath",self.login_button_xpath)
        return AccountPage(self.driver)

    def login_to_application(self,email,password):
        self.enter_email_address(email)
        self.enter_password(password)
        return self.click_on_login_button()

    def verify_login_error_message(self,error_text):
        result = self.retrieve_element_text("login_warning_message_xpath",self.login_warning_message_xpath)
        return result.__contains__(error_text)
