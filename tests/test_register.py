import pytest
import time
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setUp_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        home_page=HomePage(self.driver)
        home_page.click_register()
        register_page = RegisterPage(self.driver)
    
        register_page.enter_first_name("test")
        
        register_page.enter_last_name("test")

        register_page.enter_email("tt5820724@gmail.com")
        register_page.enter_password("azerty@123")
        register_page.enter_confirm_password("azerty@123")
        register_page.click_register_button()

        expected_heading_text = "Your registration completed"
        assert self.driver.find_element(By.XPATH,"//div[@class='result']").text.__eq__(expected_heading_text)
