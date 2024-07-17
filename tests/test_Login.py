import time
from datetime import datetime
import pytest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application("cucu@gmail.com","Pass@1234")
        assert account_page.display_status_of_edit_account_information()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address(f"new{self.generate_random_email_with_timestamp()}@gmail.com")
        login_page.enter_password("Pass@1234")
        login_page.click_on_login_button()
        expt_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.verify_login_error_message(expt_text)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("cucu@gmail.com","Pass@123")
        # password_text_box.send_keys(Keys.ENTER)    # Using Enter Keys from Selenium Import from "Keys"
        expt_txt = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.verify_login_error_message(expt_txt)

    def test_login_with_invalid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address(f"new{self.generate_random_email_with_timestamp()}@gmail.com")
        login_page.enter_password("Pass@123")
        login_page.click_on_login_button()
        expt_txt = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.verify_login_error_message(expt_txt)

    def generate_random_email_with_timestamp(self):
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return current_time
