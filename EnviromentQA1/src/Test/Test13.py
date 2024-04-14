# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium, Functions
from selenium.webdriver.common.keys import Keys #usar teclas del teclado
import unittest
import selenium
import time

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
    
    def test001(self):
        Selenium.get_url_driver(self, "https://aeropost.com/site/es?gtw=sjo")
        Selenium.obtener_archivo_json(self, "Localizadores")
        elemento = Selenium.obtener_Texto(self, "TextoAeroPost")
        self.assertEqual(elemento, "Compra lo que se te ocurra", "No se mostro el texto correcto")

    def tearDown(self):
        Functions.cerrar_driver_navegador(self)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()