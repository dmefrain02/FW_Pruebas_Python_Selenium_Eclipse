from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, 'Chrome')
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test001(self):
        Selenium.get_url_driver(self, "https://aeropost.com/SJO_es/")
        Selenium.Assert_True_IsDisplayer_Elemento(self, 'img_aeropost',f'No se muestra el elemento: {self.json_ValueToFind}')
        
    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()