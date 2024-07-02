from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self,driver):
        self.driver = driver

    edit_account_information_action_link_text = "Change your password"

    def display_status_of_edit_account_information(self):
        return self.driver.find_element(By.LINK_TEXT,self.edit_account_information_action_link_text).is_displayed()
