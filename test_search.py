import pytest
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setUp_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.ID,"small-searchterms").send_keys("Apple")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        assert self.driver.find_element(By.LINK_TEXT,"Apple MacBook Pro 13-inch").is_displayed()
    def test_search_for_an_invalid_product(self):
        self.driver.find_element(By.ID,"small-searchterms").send_keys("mercedes")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        expected_text = "No products were found that matched your criteria."
        assert self.driver.find_element(By.XPATH,"//div[@class='no-result']").text.__eq__(expected_text)
    
    