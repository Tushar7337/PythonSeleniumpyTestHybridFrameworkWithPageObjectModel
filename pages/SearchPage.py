from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    valid_HP_product_link_text = "HP LP3065"
    invalid_product_patek_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_valid_product(self):
        return self.check_display_status_of_element("valid_HP_product_link_text",self.valid_HP_product_link_text)

    def display_status_of_invalid_product(self,error_text):
        return self.retrieve_element_text("invalid_product_patek_xpath",self.invalid_product_patek_xpath)
