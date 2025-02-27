# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
from selenium.webdriver.common.keys import Keys #usar teclas del teclado
import unittest
import selenium

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test001(self):
        self.Busqueda = 'Carros'
        Selenium.get_url_driver(self, 'https://www.mercadolibre.co.cr/')
        self.CampoBusqueda = Selenium._elementos_del_DOM_x_XPATH(self, "//input[@id='cb1-edit']")
        self.CampoBusqueda.send_keys(self.Busqueda)
        self.CampoBusqueda.send_keys(Keys.ENTER)
        
        self.linkBuscado = Selenium._elementos_del_DOM_x_XPATH(self,"//h2[@class='ui-search-item__title shops__item-title' and text()='Transmisor Fm Bluetooth Mp3 Cargador ']")
        self.linkBuscado.click()
        
        self.TextBuscado = Selenium._elementos_del_DOM_x_XPATH(self,"//h1[@class='ui-pdp-title' and text()='Transmisor Fm Bluetooth Mp3 Cargador ']")
        self.assertEqual(self.TextBuscado.text, "Transmisor Fm Bluetooth Mp3 Cargador", f"El texto mostrado no es el correcto")

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()