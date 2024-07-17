from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    edit_account_information_action_link_text = "Change your password"

    def display_status_of_edit_account_information(self):
        return self.check_display_status_of_element("edit_account_information_action_link_text",self.edit_account_information_action_link_text)
