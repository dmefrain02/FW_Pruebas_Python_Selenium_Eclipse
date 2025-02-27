# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
from selenium.webdriver.common.keys import Keys #usar teclas del teclado
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.obtener_archivo_json(self, "Localizadores")

    def test001(self):
        busqueda = 'Facebook'
        Selenium.get_url_driver(self, "https://www.google.com/")
        Selenium.crear_libro_excel(self, "B2", "D2", "B5", "B2", "C2")
        Selenium.escribir_celda(self, "B3", "DataTest", busqueda)
        entidad = Selenium.obtener_elemento(self, "txt_busqueda_google")
        entidad.send_keys(Selenium.leer_celda(self, "B3", "DataTest"))
        Selenium.escribir_celda(self,"D3","DataTest",Selenium.leer_celda(self,"B3","DataTest"))
        entidad.send_keys(Keys.ENTER)
        entidad1 = Selenium.obtener_elemento(self, "Link_Facebook")
        entidad1.click()
        Selenium.escribir_celda(self, "C3", "Bitacora Pruebas", "Se hizo click en el enlace")
        Selenium.escribir_celda(self, "B6", "DataTest", "Se hizo click en el enlace")

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()