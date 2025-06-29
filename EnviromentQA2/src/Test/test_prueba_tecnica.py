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
        
        #Ir a la pagina de registro
        Selenium.click_en_elemento(self,"Registro")
        Selenium.esperar_elemento(self,3)
        
        #Escribir valores en los campos
        Selenium.escribir_texto(self,"username","dmcace75")
        Selenium.escribir_texto(self,"email","dm75@dm75.com")
        Selenium.escribir_texto(self,"password","140609999")
        
        #Crear la cuenta
        Selenium.click_en_elemento(self,"btn_register")
        Selenium.esperar_elemento(self,3)
        
        #Validacion del usuario con que se creó la cuenta
        Selenium.Assert_True_IsDisplayer(self,"usernameperfilcreado","El elemento no se muestra")
    
    # Prueba para iniciar sesion
    def test_002(self):
        Selenium.get_url_driver(self,"https://angular-ngrx-nx-realworld-example-app-lyart.vercel.app/login")
        Selenium.esperar_elemento(self,3)
        
        #Escribir valores en los campos
        Selenium.escribir_texto(self, "email", "dm75@dm75.com")
        Selenium.escribir_texto(self, "password", "140609999")
        Selenium.esperar_elemento(self,3)
        
        #Realizar inicio de sesion
        Selenium.click_en_elemento(self,"btn_login")
        Selenium.esperar_elemento(self,3)
        
        #Validacion del usuario con que se creó la cuenta
        Selenium.Assert_True_IsDisplayer(self,"usernameperfilexistente","El elemento no se muestra")
        
    # Prueba realizar un posteo
    def test_003(self):
        Selenium.get_url_driver(self,"https://angular-ngrx-nx-realworld-example-app-lyart.vercel.app/login")
        Selenium.esperar_elemento(self,3)
        
        #Escribir valores en los campos
        Selenium.escribir_texto(self, "email", "dm65@dm65.com")
        Selenium.escribir_texto(self, "password", "125609999")
        
        Selenium.click_en_elemento(self,"btn_login")
        Selenium.esperar_elemento(self,3)
        
        #Realizar inicio de sesion
        Selenium.click_en_elemento(self,"btn_new_post")
        Selenium.esperar_elemento(self,5)
        
        #Escribir Valores en los campos del posteo
        Selenium.escribir_texto(self, "article", "tecnologia")
        Selenium.escribir_texto(self, "desc_article", "nuevas tecnologias")
        Selenium.escribir_texto(self, "autor_article", "Microsoft")
        Selenium.escribir_texto(self, "tags_article", "Sistemas Operativos")
        
        #Publicar articulo
        Selenium.click_en_elemento(self,"btn_publish_article")
        Selenium.esperar_elemento(self,3)
        
        #Validacion del usuario con que se creó la cuenta
        Selenium.Assert_Equal(self, "titulo_articulo", "tecnologia", "No se muestra el texto esperado")
        Selenium.Assert_True_IsDisplayer(self,"titulo_articulo","El elemento no se muestra")

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\dmefr\\OneDrive\\Escritorio\\FW_Pruebas_Python_Selenium_Eclipse\\EnviromentQA2\\src\\reportes htmlrunner\\Resultado de mi test plan'))