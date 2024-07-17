from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_down_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    def enter_product_into_search_box_field(self,product):
        self.type_into_element(product,"search_box_field_name",self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click("search_button_xpath",self.search_button_xpath)
        return SearchPage(self.driver)

    def click_on_my_account_drop_down_menu(self):
        self.element_click("my_account_drop_down_xpath",self.my_account_drop_down_xpath)

    def select_login_option(self):
        self.element_click("login_option_link_text",self.login_option_link_text)
        return LoginPage(self.driver)

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_down_menu()
        return self.select_login_option()

    def select_register_option(self):
        self.element_click("register_option_link_text",self.register_option_link_text)
        return RegisterPage(self.driver)

    def search_for_product(self,product):
        self.enter_product_into_search_box_field(product)
        self.click_on_search_button()
        return SearchPage(self.driver)

