import pytest
from selenium import webdriver
@pytest.fixture()
def setUp_and_teardown(request):
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    request.cls.driver = driver
    yield
    driver.quit()