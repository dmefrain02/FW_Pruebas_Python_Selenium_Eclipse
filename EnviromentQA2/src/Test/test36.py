from src.Function.Functions import Functions as Selenium
import unittest
import HtmlTestRunner
from src.Pages.HomePage_MercadoLibre import HomePage_MercadoLibre as MercadoLibre

class Test(unittest.TestCase):

    def setUp(self):
        #self.home = MercadoLibre(self)
        Selenium.abrir_navegador(self, 'Chrome')
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test_001(self):
        Selenium.get_url_driver(self,"https://the-internet.herokuapp.com/download")
        Selenium.download_file(self,'Descargar_Archivo')
        
    def test002(self):
        Selenium.get_url_driver(self, "https://aeropost.com/SJO_es/")
        Selenium.Assert_True_IsDisplayer_Elemento(self, 'img_aeropost','No se muestra el elemento')

    def test_003(self):
        Selenium.get_url_driver(self, 'https://demoqa.com/droppable')
        Selenium.esperar_elemento(self)
        Selenium.Arrastrar_y_Soltar(self, 'draggable', 'droppable')
        Selenium.esperar_elemento(self)
        Selenium.Assert_Equal(self, 'text_drop', 'Dropped!', 'No se mostro el texto esperado')
        #Selenium.Assert_True(self, 'text_drop', 'Dropped!', 'No se mostro el texto esperado')
        #Selenium.AssertFalse+Texto(self, 'text_drop', 'Dropped!3', 'Es True que el valor esperado se cumple')
        Selenium.esperar_elemento(self)
        Selenium.capturar_pantalla(self)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\dmefr\\OneDrive\\Escritorio\\FW_Pruebas_Python_Selenium_VSCode\\EnviromentQA\\src\\reportes htmlrunner\\Resultado de mi test plan"))