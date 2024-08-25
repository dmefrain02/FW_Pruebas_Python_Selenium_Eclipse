from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, 'Chrome')
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test_001(self):
        Selenium.get_url_driver(self,"https://the-internet.herokuapp.com/download")
        Selenium.download_file(self,'Descargar_Archivo')

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()