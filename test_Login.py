import pytest
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setUp_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//a[@class='ico-login']").click()
        self.driver.find_element(By.ID,"Email").send_keys("tt5820724@gmail.com")
        self.driver.find_element(By.ID,"Password").send_keys("azerty@@123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
        assert self.driver.find_element(By.LINK_TEXT,"My account").is_displayed()
        self.driver.quit()
