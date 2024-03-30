from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')
    
    def test001(self):
        Selenium.get_url_driver(self, "https://www.bestday.com.mx/")
        Selenium.esperar_elemento(self)
        Selenium.escribir_texto(self, "DateTimeIda", "San Jose, San Jose, Costa Rica")
        Selenium.escribir_texto(self,"DateTimeVuelta","Cancún, Quintana Roo, México")
        Selenium.Select_Fecha_DTPickerDinamico(self,'AvanzarMes',1,'FechaIda','FechaVuelta','DiaIda','DiaVuelta')
        Selenium.esperar_elemento(self,2)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()