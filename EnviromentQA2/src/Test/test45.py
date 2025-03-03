from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):

    def setUp(self):
       Selenium.abrir_navegador(self,"Chrome")
       Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')
       self.out = Selenium.inicializar_video(self,1920, 1080,30,"prueba1.avi")
       
    def test001(self):
        
        while True:
            Selenium.get_url_driver(self, "https://www.bestday.com.mx/")
            self.out = Selenium.grabar(self, self.salida)
            Selenium.esperar_elemento(self,2)
            
            Selenium.Realizar_Scroll_JS(self, "DateTimeIda")
            self.out = Selenium.grabar(self, self.salida)
            
            Selenium.escribir_texto(self, "DateTimeIda", "San Jose, San Jose, Costa Rica")
            self.out = Selenium.grabar(self, self.salida)
            
            Selenium.escribir_texto(self,"DateTimeVuelta","Cancún, Quintana Roo, México")
            self.out = Selenium.grabar(self, self.salida)
            
            Selenium.Selects_Fechas_DTPickerDinamico(self, "AvanzarMes", 1, "FechaIda", "FechaVuelta", "DiaIda", "DiaVuelta")
            self.out = Selenium.grabar(self, self.salida)
                        
            Selenium.capturar_pantalla(self)
            Selenium.esperar_elemento(self)
            self.out = Selenium.grabar(self, self.salida)
            break
        
        Selenium.terminar_grabacion(self,self.salida)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()