from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Usar teclas del teclado
from selenium.webdriver.common.by import By #By(tipo,valor)
import time
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_001(self):
        self.Busqueda = 'Facebook'
        self.driver.get("https://www.google.co.cr")
        
        self.CampoBusqueda = self.driver.find_element(By.NAME,"q")
        self.CampoBusqueda.send_keys(self.Busqueda)
        self.CampoBusqueda.send_keys(Keys.ENTER)
        time.sleep(5)
        
        self.LinkBuscado = self.driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')
        self.LinkBuscado.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()