from Function.Functions import Functions as Selenium
import unittest
import HtmlTestRunner

class Test(unittest.TestCase):


    def setUp(self):
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
        Selenium.Assert_Equals_Comparar_Textos(self, 'text_drop', 'Dropped!', 'No se mostro el texto esperado')
        #Selenium.Assert_True_Validar_Texto(self, 'text_drop', 'Dropped!', 'No se mostro el texto esperado')
        #Selenium.AssertFalse_Validar_Texto(self, 'text_drop', 'Dropped!3', 'Es True que el valor esperado se cumple')
        Selenium.esperar_elemento(self)
        Selenium.capturar_pantalla(self)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\dmefr\\Desktop\\Carpeta MEGA\\Videos QA\\Curso Automatizacion Pruebas\\Framework Pruebas Automatizadas\\Entornos Virtuales\\EnviromentQA\\Framework Automatizacion Pruebas Python\\src\\reportes htmlrunner\\Resultado de mi test plan'))