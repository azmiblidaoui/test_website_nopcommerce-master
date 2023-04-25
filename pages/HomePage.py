from selenium import webdriver
from selenium.webdriver.common.by import By
class HomePage:
    def __init__(self,driver):
        self.driver = driver
    
    search_box_field_ID = "small-searchterms"
    search_btn_xpath = "//button[@type='submit']"


    def enter_product_into_search_box_field(self,product_name):
        self.driver.find_element(By.ID,self.search_box_field_ID).clear()
        self.driver.find_element(By.ID,self.search_box_field_ID).send_keys(product_name)
    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_btn_xpath).click()
