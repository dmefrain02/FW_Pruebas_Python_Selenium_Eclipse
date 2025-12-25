import unittest
from Function.Functions import Functions as Selenium
from Function.Inicializar import Inicializar
import time
import subprocess
import threading

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')
        
    def Test_01(self):
        for Nav_Sel_Grid in Inicializar.Navegadores_Sel_Grid:
            Selenium.abrir_navegador(self,Nav_Sel_Grid, True)
            Selenium.get_url_driver(self,"https://demoqa.com/alerts")
            Selenium.WebdriverWait(self,2)
            Selenium.click_en_elemento(self, "btn-accept")
            Selenium.alert_navegadores(self,0,"You clicked a button","No se muestra el mensaje correcto")
            Selenium.WebdriverWait(self,2)
            Selenium.cerrar_driver_navegador(self)
        
    def Test_02(self):
        Selenium.abrir_navegador(self,"Chrome")
        Selenium.get_url_driver(self,"https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-time")
        Selenium.esperar_elemento(self, 5)
        Selenium.alert_navegadores(self,1,"This alert appeared after 5 seconds","No se muestra el mensaje correcto")
        Selenium.cerrar_driver_navegador(self)

    def Test_03(self):
        for Nav_Sel_Grid in Inicializar.Navegadores_Sel_Grid:
            Selenium.abrir_navegador(self,Nav_Sel_Grid, True)
            Selenium.get_url_driver(self,"https://demoqa.com/alerts")
            Selenium.WebdriverWait(self,2)
            Selenium.click_en_elemento(self, "btn-OK-cancel")
            Selenium.WebdriverWait(self,2)
            Selenium.alert_navegadores(self,2,"You selected Ok","No se muestra el mensaje correcto","","texto-OK")
            Selenium.esperar_elemento(self, 2)
            Selenium.cerrar_driver_navegador(self)
        
    def Test_04(self):
        for Nav_Sel_Grid in Inicializar.Navegadores_Sel_Grid:
            Selenium.abrir_navegador(self,Nav_Sel_Grid, True)
            Selenium.get_url_driver(self,"https://demoqa.com/alerts")
            Selenium.WebdriverWait(self,2)
            Selenium.click_en_elemento(self, "btn-OK-cancel")
            Selenium.WebdriverWait(self,2)
            Selenium.alert_navegadores(self,3,"You selected Cancel","No se muestra el mensaje correcto","","texto-Cancel")
            Selenium.WebdriverWait(self,2)
            Selenium.cerrar_driver_navegador(self)
        
    def Test_05(self):
        Selenium.abrir_navegador(self,"Chrome")
        Selenium.get_url_driver(self,"https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-txt-ing")
        Selenium.esperar_elemento(self, 2)
        Selenium.alert_navegadores(self,4,"","","You entered","texto-ing", "Test")
        Selenium.WebdriverWait(self,2)
        Selenium.cerrar_driver_navegador(self)
        
    def Test_06(self):
        for Nav_Sel_Grid in Inicializar.Navegadores_Sel_Grid:
            Selenium.abrir_navegador(self,Nav_Sel_Grid, True)
            Selenium.get_url_driver(self,"https://demoqa.com/alerts")
            Selenium.WebdriverWait(self,2)
            Selenium.click_en_elemento(self, "btn-accept")
            Selenium.alert_navegadores(self,0,"You clicked a button","No se muestra el mensaje correcto")
            Selenium.WebdriverWait(self,2)
            Selenium.cerrar_driver_navegador(self)

    def tearDown(self):
        #Selenium.cerrar_driver_navegador(self)
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()