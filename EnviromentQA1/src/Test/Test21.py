# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def Test_21(self):
        Selenium.get_url_driver(self, 'https://www.spotify.com/cr/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2Fintl-es')       
        Selenium.capturar_pantalla(self)
        Selenium.esperar_elemento(self, 3)
        
        Selenium.abrir_nuevo_tab(self,'tab2')
        Selenium.intercambio_tab(self, 1)
        Selenium.capturar_pantalla(self)
        Selenium.esperar_elemento(self, 3)
        Selenium.get_url_driver(self, 'https://www.google.co.cr')
        Selenium.abrir_nuevo_tab(self,'tab3','https://www.google.co.cr')
        Selenium.intercambio_tab(self, 1)
        Selenium.capturar_pantalla(self)
        Selenium.esperar_elemento(self, 3)
        Selenium.escribir_texto(self, 'txt_busqueda_google', 'QA Tecnology CRC Youtube')
        Selenium.capturar_pantalla(self)
        Selenium.envio_teclas_especificas(self, 'txt_busqueda_google', 'Enter')
        Selenium.capturar_pantalla(self)
        Selenium.Realizar_Scroll_JS(self, "video_QA")
        Selenium.capturar_pantalla(self)
        
        Selenium.Validar_Valor_Igual(self, "video_QA", "QA Technology CR 23", "Texto del link no coincide")
        #Selenium.Validar_Valor_Verdadero(self, "video_QA", "QA Technology CR", "Texto incorrecto")
        #Selenium.Validar_Valor_Falso(self, "video_QA", "QA Technology CR 2525", "Texto incorrecto")
        
        Selenium.esperar_elemento(self,5)
        Selenium.capturar_pantalla(self)
        
        Selenium.intercambio_tab(self, 1)
        Selenium.capturar_pantalla(self)
        Selenium.get_url_driver(self,'https://www.mercadolibre.co.cr')
        Selenium.esperar_elemento(self, 3)
        
        Selenium.intercambio_tab(self, 0)
        Selenium.capturar_pantalla(self)
        Selenium.Realizar_Scroll_JS(self, 'Lista_Mes')
        Selenium.obtener_elemento_select_texto(self, 'Lista_Mes', 'Mayo')
        Selenium.esperar_elemento(self, 5)

        Selenium.abrir_nuevo_tab_en_nueva_ventana(self, 'https://www.facebook.com','tab4')
        Selenium.esperar_elemento(self, 3)
        
    def Test_23(self):
        Selenium.get_url_driver(self, 'https://www.google.co.cr')
        Selenium.escribir_texto(self, 'txt_busqueda_google', 'QA Tecnology CRC Youtube')
        Selenium.capturar_pantalla(self)
        Selenium.envio_teclas_especificas(self, 'txt_busqueda_google', 'Enter')
        Selenium.capturar_pantalla(self)
    
        #Selenium.Validar_Valor_Igual(self, "video_QA", "QA Technology CR 23", "Texto del link no coincide")
        #Selenium.Validar_Valor_Verdadero(self, "video_QA", "QA Technology CR 23", "Texto incorrecto")
        Selenium.Validar_Valor_Falso(self, "video_QA", "QA Technology CR", "Texto incorrecto")
        
    def test_24(self):
        Selenium.get_url_driver(self, 'https://www.amazon.com/')
        Selenium.esperar_elemento(self, 3)
        Selenium.Mover_mouse(self, 'Primer_Nivel_Menu')
        Selenium.esperar_elemento(self, 3)
        Selenium.click_en_elemento(self,'Primer_Nivel_Menu')
        Selenium.capturar_pantalla(self)
        Selenium.Mover_mouse(self, 'Segundo_Nivel_Menu')
        Selenium.esperar_elemento(self, 3)
        Selenium.capturar_pantalla(self)
        Selenium.click_en_elemento(self, 'Segundo_Nivel_Menu')
        Selenium.esperar_elemento(self, 3)
        Selenium.Mover_mouse(self, 'Tercer_Nivel_Menu')
        Selenium.esperar_elemento(self, 3)
        Selenium.click_en_elemento(self, 'Tercer_Nivel_Menu')
        Selenium.esperar_elemento(self, 3)
        Selenium.Validar_Valor_Igual(self, 'Texto_H3_Amazon', 'Unlimited access to 100 million songs', 'Error: Texto Incorrecto, no coincide')
        Selenium.capturar_pantalla(self)
        
    def Test_22(self):
        Selenium.get_url_driver(self, 'https://the-internet.herokuapp.com/upload')       
        Selenium.cargar_archivo(self, "carga_archivo")
        Selenium.click_en_elemento(self, "btn_carga_archivo")
        Selenium.esperar_elemento(self, 6)
        self.assertEqual(Selenium.obtener_Texto(self, "archivo_cargado"), "File Uploaded!", "No se muestra el texto correcto")
        
    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()