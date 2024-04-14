from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test001(self):
        Selenium.get_url_driver(self, 'https://aeropost.com/SJO_es/')
        Imagen = Selenium.obtener_elemento(self, 'Img_Aeropost_Logo')
        Selenium.cartura_de_imagen_cortada(self, Imagen)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()