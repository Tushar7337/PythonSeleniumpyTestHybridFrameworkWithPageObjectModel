import random
import time
from datetime import datetime
import pytest
from pages.HomePage import HomePage
from utilities import RandomDataGenerator


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        register_page = home_page.select_register_option()
        unique_number = str(RandomDataGenerator.random_phone_number())
        register_page.register_an_account(RandomDataGenerator.random_first_name(),RandomDataGenerator.random_last_name(),f"new{self.generate_random_email_with_timestamp()}@gmail.com",unique_number,"Pass@1234","Pass@1234","no","select")
        expt_text = "Your Account Has Been Created!"
        assert register_page.verify_account_creation(expt_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        register_page = home_page.select_register_option()
        unique_number = str(RandomDataGenerator.random_phone_number())
        register_page.register_an_account(RandomDataGenerator.random_first_name(),RandomDataGenerator.random_last_name(),f"new{self.generate_random_email_with_timestamp()}@gmail.com",unique_number,"Pass@1234","Pass@1234","yes","select")
        expt_text = "Your Account Has Been Created!"
        assert register_page.verify_account_creation(expt_text)

    def test_register_with_duplicate_emailId(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        register_page = home_page.select_register_option()

        register_page.enter_first_name(RandomDataGenerator.random_first_name())
        register_page.enter_last_name(RandomDataGenerator.random_last_name())
        register_page.enter_email("cucu@gmail.com")
        unique_number = str(RandomDataGenerator.random_phone_number())
        register_page.enter_phone_number(unique_number)
        register_page.enter_password("Pass@1234")
        register_page.enter_confirm_password("Pass@1234")
        register_page.click_terms_and_condition_check_box()
        time.sleep(3)
        register_page.click_on_submit_button()

        expt_text = "Warning: E-Mail Address is already registered!"
        assert register_page.verify_error_message_for_duplicate_email(expt_text)

    def test_register_empty_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        register_page = home_page.select_register_option()

        register_page.enter_first_name("")
        register_page.enter_last_name("")
        register_page.enter_email("")
        register_page.enter_phone_number("")
        register_page.enter_password("")
        register_page.enter_confirm_password("")
        register_page.click_on_submit_button()

        expt_privacy_text = "Warning: You must agree to the Privacy Policy!"
        assert register_page.verify_error_message_for_privacy(expt_privacy_text)

        expt_first_name_txt = "First Name must be between 1 and 32 characters!"
        assert register_page.verify_error_for_first_name(expt_first_name_txt)

        expt_last_name_txt = "Last Name must be between 1 and 32 characters!"
        assert register_page.verify_error_for_last_name(expt_last_name_txt)

        expt_email_txt = "E-Mail Address does not appear to be valid!"
        assert register_page.verify_error_for_email(expt_email_txt)

        expt_phone_txt = "Telephone must be between 3 and 32 characters!"
        assert register_page.verify_error_for_phone_number(expt_phone_txt)

        expt_password_txt = "Password must be between 4 and 20 characters!"
        assert register_page.verify_error_for_password(expt_password_txt)

    def generate_random_email_with_timestamp(self):
        current_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        return current_time
