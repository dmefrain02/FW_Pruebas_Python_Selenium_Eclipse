from Function.Functions import Functions as Selenium
import unittest
import pyautogui
import cv2
import numpy as np

class Test(unittest.TestCase):

    def setUp(self):
       Selenium.abrir_navegador(self,"Chrome")
       Selenium.obtener_archivo_json(self, 'Localizadores_Spotify')
       #Selenium.inicializar_video(self, 1920, 1080, 30, 'Video Pruebas.mp4')
       
       self.screen_size = (1920, 1080)  # Change this to match your screen resolution
       self.fps = 30
       self.output_filename = "screen_record.avi"
       self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
       self.out = cv2.VideoWriter(self.output_filename, self.fourcc, self.fps, self.screen_size)
       
    def test001(self):
        while True:
            Selenium.get_url_driver(self, "https://www.bestday.com.mx/")
            
            # Capture screen content
            self.frame = pyautogui.screenshot()
            self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            self.out.write(self.frame)
            
            #Selenium.grabar(self)
            Selenium.esperar_elemento(self,2)
            Selenium.escribir_texto(self, "DateTimeIda", "San Jose, San Jose, Costa Rica")
            
                        # Capture screen content
            self.frame = pyautogui.screenshot()
            self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            self.out.write(self.frame)
            
            #Selenium.grabar(self)
            Selenium.escribir_texto(self,"DateTimeVuelta","Cancún, Quintana Roo, México")
            
            # Capture screen content
            self.frame = pyautogui.screenshot()
            self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            self.out.write(self.frame)
            #Selenium.grabar(self)
            Selenium.Selects_Fechas_DTPickerDinamico(self, "AvanzarMes", 1, "FechaIda", "FechaVuelta", "DiaIda", "DiaVuelta")
            
            
            # Capture screen content
            self.frame = pyautogui.screenshot()
            self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            self.out.write(self.frame)
            #Selenium.grabar(self)
            Selenium.capturar_pantalla(self)
            Selenium.esperar_elemento(self)
            
            
            # Capture screen content
            self.frame = pyautogui.screenshot()
            self.frame = np.array(self.frame)
            
            # Convert BGR format (used by OpenCV) to RGB format
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            # Write the frame to the video file
            self.out.write(self.frame)
            #Selenium.grabar(self)
            break
        
        self.out.release()
        cv2.destroyAllWindows()
        #Selenium.terminar_grabacion(self)

    def tearDown(self):
        Selenium.cerrar_driver_navegador(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()