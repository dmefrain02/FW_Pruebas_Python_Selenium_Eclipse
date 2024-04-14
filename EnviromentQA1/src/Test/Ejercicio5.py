from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.alert import Alert #Manejo de Alert
import time
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_005(self):
        self.driver.get("https://demoqa.com/slider")
        
        self.slider = self.driver.find_element(By.XPATH,'//*[@id="sliderContainer"]/div[1]/span/input')
        webdriver.ActionChains(self.driver).click_and_hold(self.slider).move_by_offset(100,0).perform()
        self.driver.implicitly_wait(10)
        webdriver.ActionChains(self.driver).click_and_hold(self.slider).move_by_offset(0,100).perform()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()