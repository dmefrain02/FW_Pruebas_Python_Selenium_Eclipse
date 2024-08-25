# -*- coding: utf-8 -*-
from Function.Functions import Functions as Selenium
import unittest

from queue import Queue
from threading import Thread
from selenium import webdriver
import time

class Test(unittest.TestCase):

#USERNAME = "user@email.com"
#API_KEY = "12345"

# q = Queue(maxsize=0)
#
# browsers = [
#   {"os_api_name": "Win7x64-C2", "browser_api_name": "IE10", "name": "Python Parallel"},
#   {"os_api_name": "Win8.1", "browser_api_name": "Chrome43x64", "name": "Python Parallel"},
# ]
#
# # put all of the browsers into the queue before pooling workers
# for browser in browsers:
#     q.put(browser)
#
# num_threads = 10

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')

    def Test001(self):
        Selenium.get_url_driver(self, 'https://www.amazon.com/')
        Selenium.esperar_elemento(self, 3)
        Selenium.capturar_pantalla(self)
        
        Selenium.Mover_Mouse_x_App_Web(self, 'Primer_Nivel_Menu')
        Selenium.esperar_elemento(self, 3)
        Selenium.click_en_elemento(self, 'Primer_Nivel_Menu')
        Selenium.capturar_pantalla(self)
        
        Selenium.Mover_Mouse_x_App_Web(self, 'Segundo_Nivel_Menu')
        Selenium.esperar_elemento(self, 3)
        Selenium.click_en_elemento(self, 'Segundo_Nivel_Menu')
        Selenium.capturar_pantalla(self)
        
        Selenium.Mover_Mouse_x_App_Web(self, 'Tercer_Nivel_Menu')
        Selenium.esperar_elemento(self, 3)
        Selenium.click_en_elemento(self, 'Tercer_Nivel_Menu')
        Selenium.capturar_pantalla(self)
        
        Selenium.Validar_Assert_Equals(self, 'Texto_H3_Amazon', 'Unlimited access to 100 million songs', 'Texto no coincide')
        Selenium.capturar_pantalla(self)

        def Test_2(self):
            #while q.empty() is False:
            #    try:
            #        browser = q.get()
            #        print("%s: Starting" % browser["browser_api_name"])
            #        driver = webdriver.Remote(desired_capabilities=browser, command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (USERNAME, API_KEY) )
            #        print("%s: Getting page" % browser["browser_api_name"])
            #        driver.get("http://crossbrowsertesting.com")
            #        print("%s: Quitting browser and ending test" % browser["browser_api_name"])
            #    except:
            #        print("%s: Error" % browser["browser_api_name"])
            #    finally:
            #        driver.quit()
            #        time.sleep(15)
            #        q.task_done()
            #    for i in range(num_threads):
            #        worker = Thread(target=test_runner, args=(q,))
            #        worker.setDaemon(True)
            #        worker.start()   
            #    q.join()
                pass
    
    def test_3(self):
        Selenium.get_url_driver(self, 'https://demoqa.com/droppable')
        Selenium.esperar_elemento(self, 3)
        Selenium.Drap_and_Drop(self, 'draggable', 'droppable')
        Selenium.esperar_elemento(self, 3)
        Selenium.Validar_Assert_Equals(self, 'text_drop', 'Dropped!', 'No se mostro el texto esperado')
        Selenium.esperar_elemento(self, 3)
        
    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()