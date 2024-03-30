from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self,'Edge')
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test_001(self):
        Selenium.get_url_driver(self, 'https://en.wikipedia.org/wiki/Selenium_(software)')
        Selenium.esperar_elemento(self, 3)
        Selenium.Double_Click(self, 'texto_Selenium')
        Selenium.esperar_elemento(self,3)
        Selenium.Click_Derecho(self, 'texto_Selenium')
        Selenium.esperar_elemento(self,3)
        Selenium.Mover_Mouse(self, 'texto_Selenium', 'img_wikipedia')
        Selenium.esperar_elemento(self,3)
        Selenium.click_en_elemento(self, 'img_wikipedia')
        Selenium.esperar_elemento(self,3)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()