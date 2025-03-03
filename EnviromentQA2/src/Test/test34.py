from Function.Functions import Functions as Selenium
import unittest
import HtmlTestRunner

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, 'Chrome')
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
        Selenium.capturar_pantalla(self)
        
    def test_002(self):
        Selenium.get_url_driver(self, 'https://demoqa.com/droppable')
        Selenium.esperar_elemento(self,3)
        Selenium.Arrastrar_y_Soltar(self, 'draggable', 'droppable')
        Selenium.esperar_elemento(self,3)
        Selenium.Validar_Assert_Equals(self, 'text_drop', 'Dropped!', 'No se mostro el texto esperado')
        Selenium.esperar_elemento(self,3)
        Selenium.capturar_pantalla(self)
    
    def test_003(self):
        Selenium.get_url_driver(self, "https://the-internet.herokuapp.com/upload")
        Selenium.cargar_archivo(self, "carga_archivo")
        Selenium.click_en_elemento(self, "btn_carga_archivo")
        Selenium.esperar_elemento(self, 6)
        self.assertEquals(Selenium.obtener_Texto(self, "archivo_cargado"), "File Uploaded!", "No se muestra el texto correcto")
        Selenium.capturar_pantalla(self)
        
    def test004(self):
        Selenium.get_url_driver(self, "https://aeropost.com/SJO_es/")
        Selenium.Is_Displayed_Element(self, 'img_aeropost')
        Selenium.esperar_elemento(self,2)
        
    def test005(self):
        Selenium.get_url_driver(self, "https://the-internet.herokuapp.com/download")
        Selenium.download_file(self, 'Descargar_Archivo')
        Selenium.esperar_elemento(self,5)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\dmefr\\Desktop\\Carpeta MEGA\\Videos QA\\Curso Automatizacion Pruebas\\Framework Pruebas Automatizadas\\Entornos Virtuales\\EnviromentQA\\Framework Automatizacion Pruebas\\src\\reportes htmlrunner\\Resultado de mi test plan'))