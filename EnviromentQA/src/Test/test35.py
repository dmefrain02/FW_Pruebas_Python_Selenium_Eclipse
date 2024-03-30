from Function.Functions import Functions as Selenium
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, 'Chrome')
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test_002(self):
        Selenium.get_url_driver(self, 'https://demoqa.com/droppable')
        Selenium.esperar_elemento(self,3)
        Selenium.Arrastrar_y_Soltar(self, 'draggable', 'droppable')
        Selenium.esperar_elemento(self,3)
        #Selenium.Assert_Equals_Comparar_Textos(self, 'text_drop', 'Dropped!', 'No se mostro el texto esperado')
        #Selenium.Assert_True_Validar_Texto(self, 'text_drop', 'Dropped!', 'No se mostro el texto esperado')
        Selenium.AssertFalse_Validar_Texto(self, 'text_drop', 'Dropped!3', 'Es True que el valor esperado se cumple')
        Selenium.esperar_elemento(self,3)
        Selenium.capturar_pantalla(self)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()