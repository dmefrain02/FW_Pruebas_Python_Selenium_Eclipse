# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
from selenium.webdriver.common.keys import Keys #usar teclas del teclado
from selenium.webdriver.common.by import By #By(tipo,valor)
import time
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        
    def test_001(self):
        self.Busqueda = 'python con selenium'
        Selenium.get_url_driver(self, "https://www.google.co.cr/")
        
        self.CampoBusqueda = self.driver.find_element(By.NAME, "q")
        self.CampoBusqueda.send_keys(self.Busqueda)
        self.CampoBusqueda.send_keys(Keys.ENTER)
        time.sleep(10)
        
        self.LinkBuscado = self.driver.find_element(By.XPATH,'//*[@id="rso"]/div[2]/div/div/div/div[1]/div/a/h3')
        self.LinkBuscado.click()

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()