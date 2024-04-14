'''
Created on 1 jun 2023

@author: dmefr
'''
import unittest


# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
from selenium.webdriver.common.keys import Keys #usar teclas del teclado
import unittest
import selenium


class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, "Chrome")

    def test001(self):
        Selenium.get_url_driver(self, "https://aeropost.com/site/es?gtw=sjo")
        Selenium.obtener_archivo_json(self, "Localizadores")
        Selenium.esperar_elemento(self, 3)
        Selenium.click_en_elemento(self, "Banner")

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()