from Function.Functions import Functions as Selenium
import unittest
import allure

@allure.feature(u'Pruebas')
@allure.story(u'Realizar Registro y Login')
@allure.testcase(u'Test Case')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(u"""Caso de prueba para verificar el</br>
login y </br>
registro en el aplicativo web de pruebas""")

class Test(unittest.TestCase):

    def setUp(self):
        with allure.step(u'Paso 1: Abrir el navegador y obtener el archivo JSON'):
            Selenium.abrir_navegador(self, 'Chrome')
            Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    #Registro
    def test_001(self):
        with allure.step(u'Paso 2: Ir al sitio de la aplicacion de pruebas'):
            Selenium.get_url_driver(self,"https://opencart.abstracta.us/index.php?route=account/register")
        
        with allure.step(u'Paso 3: Ingresar datos en el campo First Name del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.escribir_texto(self, 'First_Name', Selenium.leer_celda (self, 'C3', 'Datos Pruebas')) 
        
        with allure.step(u'Paso 4: Ingresar datos en el campo Last Name del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.escribir_texto(self, 'Last_Name', Selenium.leer_celda (self, 'C4', 'Datos Pruebas')) 
        
        with allure.step(u'Paso 5: Ingresar datos en el campo Email del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.escribir_texto(self, 'Email', Selenium.leer_celda (self, 'C5', 'Datos Pruebas')) 
        
        with allure.step(u'Paso 6: Ingresar datos en el campo Telefono del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.escribir_texto(self, 'Telefono', Selenium.leer_celda (self, 'C6', 'Datos Pruebas')) 
    
        with allure.step(u'Paso 7: Ingresar datos en el campo Password del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.escribir_texto(self, 'Password', Selenium.leer_celda (self, 'C7', 'Datos Pruebas')) 
        
        with allure.step(u'Paso 8: Ingresar datos en el campo Password Confirm del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.escribir_texto(self, 'Password_Conf', Selenium.leer_celda (self, 'C8', 'Datos Pruebas')) 
            Selenium.captura_pantalla_allure(self,'Formulario con datos')
        
        with allure.step(u'Paso 9: Marcar el campo Suscribe del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.Realizar_Scroll_JS(self, 'Suscribe')
            Selenium.click_en_elemento(self, 'Suscribe')
        
        with allure.step(u'Paso 10: Marcar el campo Privacy Policy del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.click_en_elemento(self, 'Privacy_Policy') 
        
        with allure.step(u'Paso 11: Presionar el boton Continuar para realizar el registro'):
            Selenium.esperar_elemento(self)
            Selenium.click_en_elemento(self, 'Btn_Continuar')  
        
        with allure.step(u'Paso 12: Validaciones en el registro: Elemento se muestra en pantalla'):
            Selenium.esperar_elemento(self)
            Selenium.Assert_True_IsDisplayer_Elemento(self, 'Register_Success', 'No se muestra el elemento')
        
        with allure.step(u'Paso 13: Validaciones en el registro: Registro Exitoso'):
            Selenium.Assert_Equals_Comparar_Textos(self, 'Register_Success', 'Congratulations! Your new account has been successfully created!', 'No se muestra el texto esperado')
            Selenium.captura_pantalla_allure(self,'Resultado del registro')
    #Login
    def test_002(self):
        with allure.step(u'Paso 1: Ir al sitio de la aplicacion de pruebas'):
            Selenium.get_url_driver(self,"https://opencart.abstracta.us/index.php?route=account/login")
        
        with allure.step(u'Paso 2: Ingresar datos en el campo Email_Usuario del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.escribir_texto(self, 'Email_Login', Selenium.leer_celda (self, 'C5', 'Datos Pruebas')) 
        
        with allure.step(u'Paso 3: Ingresar datos en el campo Password del formulario de registro'):
            Selenium.esperar_elemento(self)
            Selenium.escribir_texto(self, 'Password_Login', Selenium.leer_celda (self, 'C7', 'Datos Pruebas')) 
        
        with allure.step(u'Paso 4: Presionar el boton Login para realizar el registro'):
            Selenium.esperar_elemento(self)
            Selenium.click_en_elemento(self, 'Btn_Login')
        
        with allure.step(u'Paso 13: Validaciones luego de realizar el login'):
            Selenium.esperar_elemento(self)
            Selenium.Assert_True_IsDisplayer_Elemento(self, 'My_Account', 'No se muestra el elemento')
            Selenium.Assert_Equals_Comparar_Textos(self, 'My_Account', 'My Account', 'No se muestra el texto esperado')
    
    def tearDown(self):
        with allure.step(u'Paso 7: Cerrar instancia del navegador'):
            Selenium.cerrar_driver_navegador(self)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()