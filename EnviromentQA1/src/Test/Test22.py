# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
import unittest
import pytest #para hacer skip de las pruebas


class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, 'Firefox')
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test001(self):
        Selenium.get_url_driver(self, 'https://www.spotify.com/cr/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2Fintl-es')
        Selenium.espera_explicita_elemento(self,'Lista_Mes')
        Selenium.capturar_pantalla(self)
        Selenium.Realizar_Scroll_JS(self, 'Lista_Mes')
        Selenium.capturar_pantalla(self)
        Selenium.click_en_elemento(self, 'Lista_Mes')
        Selenium.obtener_elemento_select_texto(self, 'Lista_Mes', 'Mayo')
        Selenium.capturar_pantalla(self)
    
    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()