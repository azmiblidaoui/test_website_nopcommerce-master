import pytest
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setUp_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH,"//a[@class='ico-register']").click()
        self.driver.find_element(By.ID,"FirstName").send_keys("test")
        self.driver.find_element(By.ID,"LastName").send_keys("test")
        self.driver.find_element(By.ID,"Email").send_keys("tt5820724@gmail.com")
        self.driver.find_element(By.ID,"Password").send_keys("azerty@123")
        self.driver.find_element(By.ID,"ConfirmPassword").send_keys("azerty@123")
        self.driver.find_element(By.ID,"register-button").click()
        expected_heading_text = "Your registration completed"
        assert self.driver.find_element(By.XPATH,"//div[@class='result']").text.__eq__(expected_heading_text)

