import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By 
@pytest.fixture()
def setUp_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    yield
    driver.quit()
def test_login_with_valid_credentials(setUp_and_teardown):
    driver.find_element(By.XPATH,"//a[@class='ico-login']").click()
    driver.find_element(By.ID,"Email").send_keys("tt5820724@gmail.com")
    driver.find_element(By.ID,"Password").send_keys("azerty@@123")
    driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
    assert driver.find_element(By.LINK_TEXT,"My account").is_displayed()
    driver.quit()
