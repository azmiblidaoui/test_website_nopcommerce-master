import pytest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.MyAccount import MyAccount
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setUp_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page =HomePage(self.driver)
        home_page.click_login()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("tt5820724@gmail.com")
        login_page.enter_passowrd("azerty@@123")
        login_page.click_on_login_button()
        my_account = MyAccount(self.driver)
        assert my_account.display_status_of_edit_your_account_information_option()
        
        
