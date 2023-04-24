import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture()
def setUp_and_teardown():
    global driver
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    yield
    driver.quit()

def test_register_with_mandatory_fields(setUp_and_teardown):
    driver.find_element(By.XPATH,"//a[@class='ico-register']").click()
    driver.find_element(By.ID,"FirstName").send_keys("test")
    driver.find_element(By.ID,"LastName").send_keys("test")
    driver.find_element(By.ID,"Email").send_keys("tt5820724@gmail.com")
    driver.find_element(By.ID,"Password").send_keys("azerty@123")
    driver.find_element(By.ID,"ConfirmPassword").send_keys("azerty@123")
    driver.find_element(By.ID,"register-button").click()
    expected_heading_text = "Your registration completed"
    assert driver.find_element(By.XPATH,"//div[@class='result']").text.__eq__(expected_heading_text)

