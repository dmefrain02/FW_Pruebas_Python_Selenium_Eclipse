from Function.Functions import Functions as Selenium
import unittest
import pyautogui
import cv2
import numpy as np

class Test(unittest.TestCase):

    def setUp(self):
       Selenium.abrir_navegador(self,"Chrome")
       Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')
       self.salida = Selenium.inicializar_video(self,1920, 1080,30,"screen_record.avi")
       
    def test001(self):
        while True:
            Selenium.get_url_driver(self, "https://www.bestday.com.mx/")
            
            # Capture screen content
            #self.frame = pyautogui.screenshot()
            #self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            #self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            #self.out.write(self.frame)
            
            self.salida = Selenium.grabar(self, self.salida)
            Selenium.esperar_elemento(self,2)
            Selenium.escribir_texto(self, "DateTimeIda", "San Jose, San Jose, Costa Rica")
            
            # Capture screen content
            #self.frame = pyautogui.screenshot()
            #self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            #self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            #self.out.write(self.frame)
            
            self.salida = Selenium.grabar(self, self.salida)
            Selenium.escribir_texto(self,"DateTimeVuelta","Cancún, Quintana Roo, México")
            
            # Capture screen content
            #self.frame = pyautogui.screenshot()
            #self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            #self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            #self.out.write(self.frame)
            self.salida = Selenium.grabar(self, self.salida)
            Selenium.Selects_Fechas_DTPickerDinamico(self, "AvanzarMes", 1, "FechaIda", "FechaVuelta", "DiaIda", "DiaVuelta")
            
            
            # Capture screen content
            #self.frame = pyautogui.screenshot()
            #self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            #self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            #self.out.write(self.frame)
            Selenium.grabar(self, self.salida)
            Selenium.capturar_pantalla(self)
            Selenium.esperar_elemento(self)
            
            
            # Capture screen content
            #self.frame = pyautogui.screenshot()
            #self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            #self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            #self.out.write(self.frame)
            Selenium.grabar(self, self.salida)
            break
        
        #self.out.release()
        #cv2.destroyAllWindows()
        Selenium.terminar_grabacion(self,self.salida)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()