import unittest
from Function.Functions import Functions as Selenium

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def test_01(self):
        Selenium.abrir_navegador(self,"Chrome")
        self.driver.get("https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-accept")
        Selenium.alert_navegadores(self,0,"You clicked a button","No se muestra el mensaje correcto")
        Selenium.WebdriverWait(self,2)
        
    def test_02(self):
        Selenium.abrir_navegador(self,"Chrome")
        self.driver.get("https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-time")
        Selenium.esperar_elemento(self, 5)
        Selenium.alert_navegadores(self,1,"This alert appeared after 5 seconds","No se muestra el mensaje correcto")

    def test_03(self):
        Selenium.abrir_navegador(self,"Chrome")
        self.driver.get("https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-OK-cancel")
        Selenium.WebdriverWait(self,2)
        Selenium.alert_navegadores(self,2,"You selected Ok","No se muestra el mensaje correcto","","texto-OK")
        Selenium.esperar_elemento(self, 2)
        
    def test_04(self):
        Selenium.abrir_navegador(self,"Chrome")
        self.driver.get("https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-OK-cancel")
        Selenium.WebdriverWait(self,2)
        Selenium.alert_navegadores(self,3,"You selected Cancel","No se muestra el mensaje correcto","","texto-Cancel")
        Selenium.WebdriverWait(self,2)
        
    def test_05(self):
        Selenium.abrir_navegador(self,"Chrome")
        self.driver.get("https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-txt-ing")
        Selenium.esperar_elemento(self, 2)
        Selenium.alert_navegadores(self,4,"","","You entered","texto-ing", "Test")
        Selenium.WebdriverWait(self,2)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()