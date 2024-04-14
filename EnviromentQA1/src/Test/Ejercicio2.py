from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_002(self):
        self.driver.get("https://demoqa.com/checkbox")
        self.btn_abrir_lista_checkbox = self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
        self.btn_abrir_lista_checkbox.click()
        self.driver.implicitly_wait(10)
        self.btn_checkbox = self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[1]')
        self.btn_checkbox.click()
        self.driver.implicitly_wait(50)

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()