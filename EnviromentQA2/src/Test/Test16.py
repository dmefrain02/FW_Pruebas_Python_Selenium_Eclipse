# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
import unittest
from selenium.webdriver.common.keys import Keys
import allure
import pytest #para hacer skip de las pruebas

@allure.feature(u'Pruebas Mercado Libre')
@allure.story(u'Realizar busqueda de un producto')
@allure.testcase(u'Test Case 1:[el link del caso de prueba de alguna herramienta de pruebas]')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(u"""Caso de prueba para verificar si la</br>
búsqueda de un artículo en </br>
en Mercado Libre funciona""")

class Test(unittest.TestCase):


    def setUp(self):
        
        with allure.step(u'Paso 1: Abrir el navegador y obtener el archivo JSON'):
            Selenium.abrir_navegador(self)
            Selenium.obtener_archivo_json(self, 'Localizadores')
    
    def test001(self):
        
        with allure.step(u'Paso 2: Dirigiendonos a la aplicacion web a probar'):
            Selenium.get_url_driver(self, 'https://www.mercadolibre.co.cr/')
            Selenium.capturar_pantalla(self)
        
        with allure.step(u'Paso 3: Obtener Elemento Campo Busqueda de la aplicacion web'):
            elemento = Selenium.obtener_elemento(self, 'TxtCampoBusquedaMercadoLibre')
        
        with allure.step(u'Paso 4: Escribir texto en la caja de busqueda de la aplicacion web'):
            Selenium.escribir_texto(self, 'TxtCampoBusquedaMercadoLibre', 'Carros')
            Selenium.capturar_pantalla(self)
        
        with allure.step(u'Paso 5: Presionar tecla Enter para realizar busqueda en la aplicacion web'):
            elemento.send_keys(Keys.ENTER)
            Selenium.capturar_pantalla(self)
        
        with allure.step(u'Paso 6: Toma de Captura de pantalla para el reporte de Allure'):
            Selenium.captura_pantalla_allure(self, 'Resultado de la prueba')

    def tearDown(self):
        with allure.step(u'Paso 7: Cerrar instancia del navegador'):
            Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()