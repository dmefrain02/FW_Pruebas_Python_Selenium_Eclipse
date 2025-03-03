
# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
import unittest
import allure
import pytest #para hacer skip de las pruebas

@allure.feature(u'Prueba Mercado Libre')
@allure.story(u'Realizar busqueda de un producto')
@allure.testcase(u'TestCase 1')#Se puede enlazar con el caso de prueba en alguna herramienta
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(u"""Caso de prueba para verificar si la</br>
búsqueda de un artículo en </br>
en Mercado Libre funciona""")

class test_18(unittest.TestCase):


    def setUp(self):
        #Paso 1
        with allure.step(u'Paso 1: Abrir el navegador'):
            Selenium.abrir_navegador(self)
            print('Se abrio la instancia del navegador: ' + str(Selenium.obtener_fecha_actual(self)) +' ' + str(Selenium.obtener_hora_actual(self)))
        
        with allure.step(u'Paso 2: Obtener Archivo Json'):
            Selenium.obtener_archivo_json(self, 'Localizadores')
        
    def test_001(self):
        with allure.step(u'Paso 3: Dirigirnos a la aplicación de prueba'):
            Selenium.get_url_driver(self, 'https://www.mercadolibre.co.cr/')
            print('Se ingreso a la pagina de pruebas: ' + str(Selenium.obtener_fecha_actual(self)) +' ' + str(Selenium.obtener_hora_actual(self)))
            Selenium.espera_explicita_elemento(self, 'TxtCampoBusquedaMercadoLibre')
            print('Se esta esperando el elemento en pantalla: ' + str(Selenium.obtener_fecha_actual(self)) +' ' + str(Selenium.obtener_hora_actual(self)))
        
        with allure.step(u'Paso 4: Se escribe texto de busqueda'):
            Selenium.escribir_texto(self, 'TxtCampoBusquedaMercadoLibre', 'Carros')
            print('Escribir texto en el elemento: ' + str(Selenium.obtener_fecha_actual(self)) +' ' + str(Selenium.obtener_hora_actual(self)))
        
        with allure.step(u'Paso 5: Se toma captura de pantalla'):
            Selenium.capturar_pantalla(self)
        
        with allure.step(u'Paso 6: Se limpia el valor escrito'):
            Selenium.limpiar_elemento(self, 'TxtCampoBusquedaMercadoLibre')
            print('Se limpio el elemento: ' + str(Selenium.obtener_fecha_actual(self)) +' ' + str(Selenium.obtener_hora_actual(self)))
        
        with allure.step(u'Paso 7: Se vuelve escribir valor de busqueda'):
            Selenium.escribir_texto(self, 'TxtCampoBusquedaMercadoLibre', 'Consola de VideoJuegos')
            print('Escribir texto en el elemento: ' + str(Selenium.obtener_fecha_actual(self)) +' ' + str(Selenium.obtener_hora_actual(self)))
        
        with allure.step(u'Paso 8: Se realiza la busqueda'):
            Selenium.envio_teclas_especificas(self, 'TxtCampoBusquedaMercadoLibre', 'Enter')
            print('Se presiono la tecla Enter: ' + str(Selenium.obtener_fecha_actual(self)) +' ' + str(Selenium.obtener_hora_actual(self)))
        
        with allure.step(u'Paso 9: Se toma captura de pantalla'):
            Selenium.espera_explicita_elemento(self,'TxtCampoBusquedaMercadoLibre')
            Selenium.capturar_pantalla(self)
        
    def tearDown(self):
        with allure.step(u'Paso 10: Se cierra el navegador'):
            Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()