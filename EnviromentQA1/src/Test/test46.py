# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
import unittest
import pytest #para hacer skip de las pruebas
import allure
import pyodbc

class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self,"Edge")
        Selenium.obtener_archivo_json(self, 'Localizadores')

    def test_001(self):
        Selenium.get_url_driver(self, 'https://www.mercadolibre.co.cr/')
        Selenium.capturar_pantalla(self)         
        Selenium.obtener_elemento(self, 'TxtCampoBusquedaMercadoLibre')
        try: 
            Selenium.escribir_texto(self,'TxtCampoBusquedaMercadoLibre', Selenium.pyodbc_ConsultaBD(self,'QA', 'select DP.Valor_Dato_Prueba from Datos_Pruebas DP WHERE Id_Caso_Prueba = 15'))
            Selenium.capturar_pantalla(self)
            Selenium.envio_teclas_especificas(self, 'TxtCampoBusquedaMercadoLibre', 'Enter')
            Selenium.esperar_elemento(self, 3)
            Selenium.capturar_pantalla(self)
           
        except (pyodbc.OperationalError) as error:
            if pyodbc.OperationalError:
                print(error)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self) 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()