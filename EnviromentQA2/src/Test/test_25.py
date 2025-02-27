# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test_1(self):
        Selenium.get_url_driver(self, 'https://www.google.co.cr')
        Selenium.escribir_texto(self, 'txt_busqueda_google', 'QA Tecnology CRC Youtube')
        Selenium.capturar_pantalla(self)
        Selenium.envio_teclas_especificas(self, 'txt_busqueda_google', 'enter')
        Selenium.capturar_pantalla(self)
        
        Selenium.Validar_Assert_Equals(self, 'video_QA', 'QA Technology CR', 'Texto incorrecto')
        #Selenium.Validar_Assert_True(self, 'video_QA', 'QA Technology CR', 'Texto incorrecto')
        #Selenium.Validar_Assert_False(self, 'video_QA', 'QA Technology CR 25', 'Texto incorrecto')
        
    
    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()