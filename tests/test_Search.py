import pytest
from pages.HomePage import HomePage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        product_name = "HP"
        search_page = home_page.search_for_product(product_name)
        assert search_page.display_status_of_valid_product()

    def test_search_for_an_invalid_product(self):
        self.driver.get("https://tutorialsninja.com/demo/")
        home_page = HomePage(self.driver)
        product_name = "Patek"
        search_page = home_page.search_for_product(product_name)
        error_txt = "There is no product that matches the search criteria."
        assert search_page.display_status_of_invalid_product(error_txt)

    def test_search_without_entering_any_product_name(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("")
        error_txt = "There is no product that matches the search criteria."
        assert search_page.display_status_of_invalid_product(error_txt)
