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
        Selenium.alert_navegadores(self,0,0)
        Selenium.WebdriverWait(self,2)
        
    def test_02(self):
        Selenium.abrir_navegador(self,"Chrome")
        self.driver.get("https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-time")
        Selenium.esperar_elemento(self, 5)
        Selenium.alert_navegadores(self,0,1)

    def test_03(self):
        Selenium.abrir_navegador(self,"Chrome")
        self.driver.get("https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-OK-cancel")
        Selenium.WebdriverWait(self,2)
        Selenium.alert_navegadores(self,0,2,"texto-OK")
        Selenium.esperar_elemento(self, 2)
        
    def test_04(self):
        Selenium.abrir_navegador(self,"Chrome")
        self.driver.get("https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-OK-cancel")
        Selenium.WebdriverWait(self,2)
        Selenium.alert_navegadores(self,0,3,"texto-Cancel")
        Selenium.WebdriverWait(self,2)
        
    def test_05(self):
        Selenium.abrir_navegador(self,"Chrome")
        self.driver.get("https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-txt-ing")
        Selenium.esperar_elemento(self, 2)
        Selenium.alert_navegadores(self,0,4,"result-txt-ing","TEST")
        Selenium.WebdriverWait(self,2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()