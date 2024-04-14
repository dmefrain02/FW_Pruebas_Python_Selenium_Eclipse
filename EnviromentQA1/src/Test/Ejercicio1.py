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

    def test_001(self):
        self.driver.get("https://demoqa.com/text-box")
        self.FullName = self.driver.find_element(By.XPATH, '//*[@id="userName"]')
        self.FullName.send_keys("Nombre")
        
        self.Email = self.driver.find_element(By.ID, 'userEmail')
        self.Email.send_keys("prueba@test.com")
        
        self.DirAct = self.driver.find_element(By.ID, 'currentAddress')
        self.DirAct.send_keys("Direccion Actual")
        
        self.DirFinal = self.driver.find_element(By.ID, 'permanentAddress')
        self.DirFinal.send_keys("Direccion Final")
        
        self.Btn_Submit = self.driver.find_element(By.XPATH, '//*[@id="submit"]')
        self.driver.implicitly_wait(10)
        self.Btn_Submit.click()
        
        self.Nombre = self.driver.find_element(By.ID, 'name')
        self.Correo = self.driver.find_element(By.ID, 'email')
        print(f'Datos Impresos en el resultado')
        print(self.Nombre.text)
        print(self.Correo.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()