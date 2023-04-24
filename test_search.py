from selenium import webdriver
from selenium.webdriver.common.by import By
def test_search_for_a_valid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    driver.find_element(By.ID,"small-searchterms").send_keys("Apple")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    assert driver.find_element(By.LINK_TEXT,"Apple MacBook Pro 13-inch").is_displayed()
    driver.quit()
def test_search_for_an_invalid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    driver.find_element(By.ID,"small-searchterms").send_keys("mercedes")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    expected_text = "No products were found that matched your criteria."
    assert driver.find_element(By.XPATH,"//div[@class='no-result']").text.__eq__(expected_text)
    driver.quit()
    