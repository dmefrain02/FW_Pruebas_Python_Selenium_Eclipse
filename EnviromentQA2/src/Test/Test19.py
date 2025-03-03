# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
import unittest
import pytest #para hacer skip de las pruebas
import allure

@allure.feature(u'Pruebas Mercado Libre')
@allure.story(u'Realizar busqueda de un producto')
@allure.testcase(u'Test Case:[el link del caso de prueba de alguna herramienta de pruebas]')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(u"""Caso de prueba para verificar si la</br>
búsqueda de un artículo en </br>
en Mercado Libre funciona""")

class Test(unittest.TestCase):

    def setUp(self):
        with allure.step(u'Paso 1: Abrir el navegador y obtener el archivo JSON'):
            Selenium.abrir_navegador(self)
            Selenium.obtener_archivo_json(self, 'Localizadores')

    def test_001(self):
        with allure.step(u'Paso 2: Ir al sitio de la aplicacion de pruebas'):
            Selenium.get_url_driver(self, 'https://www.mercadolibre.co.cr/')
            Selenium.capturar_pantalla(self)
            
        with allure.step(u'Paso 3: Obtener elemento en la aplicacion web para interactuar'):
            elemento = Selenium.obtener_elemento(self, 'TxtCampoBusquedaMercadoLibre')
        
        with allure.step(u'Paso 4: Escribir en elemento obtenido de la aplicacion web'):
            Selenium.escribir_texto(self, 'TxtCampoBusquedaMercadoLibre', 'Consola Video Juegos')
            Selenium.captura_pantalla_allure(self, 'Texto escrito en elemento de la pagina')
        
        with allure.step(u'Paso 5: Presionar tecla enter en la aplicacion para realizar busqueda'):
            Selenium.envio_teclas_especificas(self, 'TxtCampoBusquedaMercadoLibre', 'ENTER')
            Selenium.esperar_elemento(self, 5)
            Selenium.captura_pantalla_allure(self,'Resultado de la busqueda')
        
        with allure.step(u'Paso 6: Presionar click en elemento del resultado de la busqueda'):
            Selenium.click_en_elemento(self, 'Articulo_Buscado')
            Selenium.esperar_elemento(self,5)
            Selenium.captura_pantalla_allure(self,'Articulo Buscado')

    def tearDown(self):
        with allure.step(u'Paso 7: Cerrar instancia del navegador'):
            Selenium.cerrar_driver_navegador(self)        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()