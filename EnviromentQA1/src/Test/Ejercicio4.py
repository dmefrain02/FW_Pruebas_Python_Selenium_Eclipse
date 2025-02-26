from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert #Manejo de Alert
import time
import unittest
from Function.Functions import Functions as Selenium

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.obtener_archivo_json(self, 'Localizadores')
        self.driver.implicitly_wait(10)
        
    def test_04(self):
        self.driver.get("https://demoqa.com/alerts")
        
        self.btn_alert = self.driver.find_element(By.XPATH, '//*[@id="alertButton"]')
        self.btn_alert.click()
        self.alert = Alert(self.driver)
        WebDriverWait(self.driver,5)
        self.text_alert = self.alert.text
        
        print('Mensaje de alert: ' + self.text_alert)
        self.alert.accept()
        self.assertEqual(self.text_alert, "You clicked a button", "El texto de la alerta no se muestra correctamente")
        WebDriverWait(self.driver,5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()