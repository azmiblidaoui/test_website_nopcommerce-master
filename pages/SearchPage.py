from selenium import webdriver
from selenium.webdriver.common.by import By
class SearchPage:
    def __init__(self,driver):
        self.driver = driver

    valid_Apple_product_link_text = "Apple MacBook Pro 13-inch"
    no_product_message_xpath = "//div[@class='no-result']"

    def display_status_of_product(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_Apple_product_link_text).is_displayed()
    def retrive_no_product_message(self):
        return self.driver.find_element(By.XPATH,self.no_product_message_xpath).text 
