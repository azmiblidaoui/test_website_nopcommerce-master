import pytest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setUp_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)

        home_page.enter_product_into_search_box_field("Apple")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_product()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("mercedes")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        expected_text = "No products were found that matched your criteria."
        assert search_page.retrive_no_product_message().__eq__(expected_text)
    
    