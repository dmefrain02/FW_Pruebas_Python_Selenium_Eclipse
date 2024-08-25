# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
import unittest
import pytest #para hacer skip de las pruebas

class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.obtener_archivo_json(self, 'LocalizAdores_Spotify')

    def Test_001(self):
        Selenium.get_url_driver(self, 'https://www.spotify.com/cr/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2Fintl-es')
        Selenium.esperar_elemento(self, 3)
        Selenium.capturar_pantalla(self)
        
        Selenium.abrir_nuevo_tab(self,'tab2')
        Selenium.intercambio_tab(self, 1)
        Selenium.esperar_elemento(self, 3)
        Selenium.capturar_pantalla(self)
        
        Selenium.abrir_nuevo_tab(self,'tab3','https://www.google.co.cr')
        Selenium.intercambio_tab(self, 2)
        Selenium.esperar_elemento(self, 3)
        Selenium.capturar_pantalla(self)
        
        Selenium.escribir_texto(self, 'txt_busqueda_google', 'QA Tecnology CRC')
        Selenium.capturar_pantalla(self)
        Selenium.envio_teclas_especificas(self, 'txt_busqueda_google', 'Enter')
        Selenium.capturar_pantalla(self)
        Selenium.Realizar_Scroll_JS(self, "video_QA")
        Selenium.capturar_pantalla(self)
        self.assertEqual(Selenium.obtener_Texto(self, "video_QA"), "QA Technology", "Texto del link no coincide")
        Selenium.esperar_elemento(self,5)
        Selenium.capturar_pantalla(self)
        
        Selenium.intercambio_tab(self, 1)
        Selenium.capturar_pantalla(self)
        Selenium.get_url_driver(self,'https://www.mercadolibre.co.cr')
        Selenium.esperar_elemento(self, 3)
        Selenium.capturar_pantalla(self)
        
        Selenium.intercambio_tab(self, 0)
        Selenium.capturar_pantalla(self)
        Selenium.Realizar_Scroll_JS(self, 'Lista_Mes')
        Selenium.obtener_elemento_select_texto(self, 'Lista_Mes', 'Mayo')
        Selenium.esperar_elemento(self, 5)
        Selenium.capturar_pantalla(self)
        
        Selenium.abrir_nuevo_tab_en_nueva_ventana(self, 'https://www.facebook.com','tab4')
        Selenium.esperar_elemento(self, 3)
        Selenium.capturar_pantalla(self)
    
    def test_002(self):
        Selenium.get_url_driver(self, "https://the-internet.herokuapp.com/upload")
        Selenium.cargar_archivo(self, "carga_archivo")
        Selenium.click_en_elemento(self, "btn_carga_archivo")
        Selenium.esperar_elemento(self, 6)
        self.assertEquals(Selenium.obtener_Texto(self, "archivo_cargado"), "File Uploaded!", "No se muestra el texto correcto")
         
    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()