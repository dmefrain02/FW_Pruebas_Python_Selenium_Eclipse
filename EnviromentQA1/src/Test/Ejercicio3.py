from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="..\\Drivers\\Chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
    def test_003(self):
        self.driver.get("https://demoqa.com/radio-button")
        self.btn_rdbtn = self.driver.find_element(By.XPATH, '//*[@id="yesRadio"]')
        self.txt_rdbtn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]')
        self.driver.implicitly_wait(20)
        
        if self.btn_rdbtn.is_displayed():
            self.btn_rdbtn.click()
            self.btn_rdbtn.is_selected()
        
        print(self.txt_rdbtn.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()