from src.Function.Functions import Functions as Selenium
import unittest
import HtmlTestRunner

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, 'Chrome')
        Selenium.obtener_archivo_json(self, 'Localizadores_Prueba_Tecnica')

    # Prueba para verificar el registro en la aplicación Angular-NGRX-NX RealWorld Example App
    def test_001(self):
        Selenium.get_url_driver(self,"https://angular-ngrx-nx-realworld-example-app-lyart.vercel.app/login")
        Selenium.esperar_elemento(self,3)
        Selenium.click_en_elemento(self,"Registro")
        Selenium.escribir_texto(self,"username","dmcace")
        Selenium.escribir_texto(self,"email","dm30@dm30.com")
        Selenium.escribir_texto(self,"password","115009585")
        Selenium.click_en_elemento(self,"btn_register")
        Selenium.esperar_elemento(self,3)
        #Selenium.Assert_True_IsDisplayer(self,"usernameperfil","El elemento no se muestra")
        
    def Test002(self):
        Selenium.get_url_driver(self,"https://angular-ngrx-nx-realworld-example-app-lyart.vercel.app/login")

    def Test_003(self):
        Selenium.get_url_driver(self,"https://angular-ngrx-nx-realworld-example-app-lyart.vercel.app/login")

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\dmefr\OneDrive\Escritorio\FW_Pruebas_Python_Selenium_VSCode\EnviromentQA\src\reportes htmlrunner\Resultado de mi test plan"))