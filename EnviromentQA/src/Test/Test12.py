# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
from selenium.webdriver.common.keys import Keys #usar teclas del teclado
import unittest
import selenium

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test001(self):
        Busqueda = 'Carros'
        Selenium.get_url_driver(self, "https://www.mercadolibre.co.cr/")
        Selenium.obtener_archivo_json(self, "Localizadores")
        elemento = Selenium.obtener_elemento(self, "TxtCampoBusqueda")
        elemento.send_keys(Busqueda)
        elemento.send_keys(Keys.ENTER)
        
        elemento = Selenium.obtener_elemento(self,"Link_Buscado")
        elemento.click()
        
        elemento = Selenium.obtener_elemento(self, "TextBuscado")
        self.assertEqual(elemento.text, "Transmisor Fm Bluetooth Mp3 Cargador", f"El texto mostrado no es el correcto")

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()