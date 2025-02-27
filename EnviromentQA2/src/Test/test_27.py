from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self,'Firefox')
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test_001(self):
        Selenium.get_url_driver(self, 'https://demoqa.com/droppable')
        Selenium.esperar_elemento(self,3)
        Selenium.Arrastrar_y_Soltar(self, 'draggable', 'droppable')
        Selenium.esperar_elemento(self,3)
        Selenium.Validar_Assert_Equals(self, 'text_drop', 'Dropped!', 'No se mostro el texto esperado')
        Selenium.esperar_elemento(self,3)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()