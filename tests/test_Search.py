import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        product_name = "HP"
        home_page.enter_product_into_search_box_field(product_name)
        home_page.click_on_search_button()
        assert search_page.display_status_of_valid_product()

    def test_search_for_an_invalid_product(self):
        self.driver.get("https://tutorialsninja.com/demo/")
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        product_name = "Patek"
        search_field = home_page.enter_product_into_search_box_field(product_name)
        home_page.click_on_search_button()
        #search_field.send_keys(Keys.ENTER)
        error_txt = "There is no product that matches the search criteria."
        assert search_page.display_status_of_invalid_product(error_txt)

    def test_search_without_entering_any_product_name(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        error_txt = "There is no product that matches the search criteria."
        assert search_page.display_status_of_invalid_product(error_txt)
