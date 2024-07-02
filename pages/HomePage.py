from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_down_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"


    def enter_product_into_search_box_field(self,product):
        self.driver.find_element(By.NAME,self.search_box_field_name).click()
        self.driver.find_element(By.NAME,self.search_box_field_name).clear()
        self.driver.find_element(By.NAME,self.search_box_field_name).send_keys(product)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def click_on_my_account_drop_down_menu(self):
        self.driver.find_element(By.XPATH,self.my_account_drop_down_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option_link_text).click()

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT,self.register_option_link_text).click()

