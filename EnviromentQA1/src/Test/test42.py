from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def Test001(self):
        Selenium.get_url_driver(self, 'https://aeropost.com/SJO_es/')
        Selenium.esperar_elemento(self)
        Selenium.obtener_cookie_nombre(self, '_ga_SVSSXL94CZ')
        
    def Test002(self):
        Selenium.get_url_driver(self, 'https://aeropost.com/SJO_es/')
        Selenium.esperar_elemento(self)
        Selenium.obtener_todas_las_cookies(self)
        
    def Test003(self):
        Selenium.get_url_driver(self, 'https://aeropost.com/SJO_es/')
        Selenium.esperar_elemento(self)
        Selenium.eliminar_cookie_x_nombre(self, '_ga_SVSSXL94CZ')
        Selenium.obtener_todas_las_cookies(self)
        
    def test004(self):
        Selenium.get_url_driver(self, 'https://aeropost.com/SJO_es/')
        Selenium.esperar_elemento(self)
        Selenium.eliminar_todas_las_cookies(self)
        Selenium.obtener_todas_las_cookies(self)
    
    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()