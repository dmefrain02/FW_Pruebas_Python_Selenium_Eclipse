from Function.Functions import Functions as Selenium
import unittest
from Function.Inicializar import Inicializar
from threading import Thread,Barrier
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OpcionesChrome

class Pruebas_PaginaCompras(unittest.TestCase):

    def setUp(self):
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')
        self.numero_multitareas = 4
        self.barrier = Barrier(self.numero_multitareas)
        self.threads = []
        self.url = "https://www.mercadolibre.co.cr/"
    
    def Test001(self):
        Selenium.abrir_navegador(self,"Chrome")
        Selenium.get_url_driver(self, "https://www.bestday.com.mx/")
        Selenium.esperar_elemento(self)
        Selenium.Realizar_Scroll_JS(self, "DateTimeIda")
        Selenium.escribir_texto(self, "DateTimeIda", "San Jose, San Jose, Costa Rica")
        Selenium.escribir_texto(self,"DateTimeVuelta","Cancún, Quintana Roo, México")
        Selenium.Selects_Fechas_DTPickerDinamico(self,'AvanzarMes',1,'FechaIda','FechaVuelta','DiaIda','DiaVuelta')
        Selenium.capturar_pantalla(self)
        Selenium.esperar_elemento(self,2)
    
    def test002(self):
        def func(threads):
            Selenium.abrir_navegador(self, "Chrome")
            Selenium.get_url_driver(self, self.url)   
            threads.wait()
            Selenium.click_en_elemento(self, "Mercadolibre-Busqueda")
            Selenium.escribir_texto(self, "Mercadolibre-Busqueda", "ABC")
        for _ in range(self.numero_multitareas):
            i = Thread(target=func,args=(self.barrier,))
            i.start()
            self.threads.append(i)
        
        for _ in self.threads:
            i.joi      
            
    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()