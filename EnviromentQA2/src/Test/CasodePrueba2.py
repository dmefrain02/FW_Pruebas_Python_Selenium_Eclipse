from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Usar teclas del teclado
from selenium.webdriver.common.by import By #By(tipo,valor)
from selenium.webdriver.common.alert import Alert #Alertas en el navegador
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
    '''Prueba Escribir y mostrar texto'''
    def test_001(self):
        self.driver.get("https://demoqa.com/text-box")
        
        self.FullName = self.driver.find_element(By.XPATH,'//*[@id="userName"]')
        self.FullName.send_keys("Nombre")
        
        self.Email = self.driver.find_element(By.ID,"userEmail")
        self.Email.send_keys("correo@correo.com")
        
        self.DireccionAct = self.driver.find_element(By.ID,"currentAddress")
        self.DireccionAct.send_keys("SJ,Cart,123")
        
        self.Direccion = self.driver.find_element(By.ID,"permanentAddress")
        self.Direccion.send_keys("Lim,Siq,123")
        
        self.Btn_Submit = self.driver.find_element(By.ID, "submit")
        
        #Es necesario un tiempo de espera aca para que en la pagina se dejen de ejecutar algunos JS que tiene
        #que entran en conflicto con el evento click del boton y que permite que se muestren los textos
        self.driver.implicitly_wait(10)
        self.Btn_Submit.click()
        
        self.Nombre = self.driver.find_element(By.ID, 'name')
        self.Correo = self.driver.find_element(By.ID, 'email')
        #Estos dos campos se muestran en la pagina con texto, pero al revisar los campos en el codigo (debuggeando) no trae valor
        #self.DirAct = self.driver.find_element(By.ID, 'currentAddress')
        #self.DirPer = self.driver.find_element(By.ID, 'permanentAddress')
            
        print(f'Datos impresos en el resultado')
        print(self.Nombre.text)
        print(self.Correo.text)
        '''Estos dos campos se muestran en la pagina con texto, pero al revisar los campos en el codigo (debuggeando) 
        no trae valor, selpero para mostrarse seria de la misma manera que con los otros dos campos'''
        #print(self.DirAct.text)
        #print(self.DirPer.text)
        
    '''Prueba Interacturar con Alert'''
    def test_002(self):
        self.driver.get("https://demoqa.com/alerts")
        
        #Click en el boton que dispara el mensaje de alerta
        self.btn_alert = self.driver.find_element(By.XPATH,'//*[@id="alertButton"]')
        self.btn_alert.click()      
        
        #Capturamos el alert que nos sale luego del click
        self.alert = Alert(self.driver)
        WebDriverWait(self.driver,5) 
        
        #Tomamos el texto del alert
        self. text_alert = self.alert.text
        
        #Imprimimos el mensaje del alert
        print('Mensaje de Alerta:' + self.text_alert)
        
        #Aceptamos el aler en el navegador para que se cierre
        self.alert.accept()
        
        #Verificamos que el mensaje del alert este correcto
        self.assertEqual(self.text_alert, 'You clicked a button', 'El texto de la alerta no se muestra correctamente')
        WebDriverWait(self.driver,5)
 
    '''Prueba Interactuar con Slider'''
    def test_003(self):
        self.driver.get("https://demoqa.com/slider")
        
        self.slider = self.driver.find_element(By.XPATH,'//*[@id="sliderContainer"]/div[1]/span/input')
        #Dar y Mantener el click sobre el slider para moverlo
        webdriver.ActionChains(self.driver).click_and_hold(self.slider).move_by_offset(100, 0).perform()
        self.driver.implicitly_wait(10)
        #Dar y Mantener el click sobre el slider para moverlo
        webdriver.ActionChains(self.driver).click_and_hold(self.slider).move_by_offset(0, 100).perform()
        self.driver.implicitly_wait(10)
 
    '''Marco radiobuttom concreto e imprimir texto del radiobutton'''
    def test_004(self):
        self.driver.get("https://demoqa.com/radio-button")
        self.btn_rdbtn = self.driver.find_element(By.XPATH,'//*[@id="yesRadio"]')
        self.txt_rdbtn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')
        self.driver.implicitly_wait(10)
        
        #Esperamos a que el elemento este presente en la pagina
        if self.btn_rdbtn.is_displayed():
            self.btn_rdbtn.click()
        
        #Imprimimos el mensaje del radio-button
        print(self.txt_rdbtn.text)
        
    '''Seleccion checkbox concreto dentro de varios chekcbox'''
    def test_005(self):
        self.driver.get("https://demoqa.com/checkbox")
        
        #Buscamos el elemento que despliega la lista de los checkbox y seguido lo clickamos
        self.btn_rdbtn = self.driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/span/button')
        self.btn_rdbtn.click()
        self.driver.implicitly_wait(10)
        
        #Clickamos el checkbox concreto de la lista de checkbox que queremos marcar
        self.btn_rdbtn1 = self.driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[1]')
        self.btn_rdbtn1.click()
        self.driver.implicitly_wait(50)
                    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()