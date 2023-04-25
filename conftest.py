import pytest
from selenium import webdriver
from utilities import ReadConfigurations
@pytest.fixture()
def setUp_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info","browser")
    if browser.__eq__("chrome"):
        driver =webdriver.Chrome()
    elif browser.__eq__("firfox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("add browser name frome 'config file ', can you use ' chrome, firfox, edge '  ")

    driver.maximize_window()
    url = ReadConfigurations.read_configuration("basic info","url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()