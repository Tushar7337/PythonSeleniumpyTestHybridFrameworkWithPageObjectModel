from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self,driver):
        self.driver = driver

    valid_HP_product_link_text = "HP LP3065"
    invalid_product_patek_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_HP_product_link_text).is_displayed()

    def display_status_of_invalid_product(self,error_text):
        return (self.driver.find_element(By.XPATH,self.invalid_product_patek_xpath).text
         .__eq__(error_text))
