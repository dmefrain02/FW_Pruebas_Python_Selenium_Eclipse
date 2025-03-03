from Function.Inicializar import Inicializar
from selenium import webdriver

#Librerias Webdrivers Services de los navegadores
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
#Librerias Webdrivers options de los navegadores
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.firefox.options import Options as OpcionesFirefox
from selenium.webdriver.edge.options import Options as OpcionesEdge
#Librerias Webdrivers Manager de los navegadores
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverFactory():
    def __init__(self,navegador=Inicializar.Navegador, remote: bool = False, capabilities: bool = False, URL_Sel_Grid = Inicializar.URL_SeleniumGrid):
        self.Navegador = navegador.lower()
        self.Remote = remote #Si es un llamado por Selenium Grid o no
        self.Capabilities = capabilities #Si es llamado por Selenium Grid, se configuran las capabilities o no
        self.Grid_URL = URL_Sel_Grid # URL del llamado a Selenium Grid
        self.driver = None

    #Retorna el Driver de la instancia del navegador a utilizar en las pruebas.
    def get_driver(self):
        if self.driver is None:
            self.driver = self._create_driver(self.Navegador, self.Remote, self.Capabilities, self.Grid_URL)
        return self.driver
    
     #Crear y configurar el driver: local o remoto
    def _create_driver(self, browser: str, remote: bool, capabilities: bool, grid_url: str):       
        if remote:  #Instancia remota en Selenium Grid
            if capabilities:
                capabilities_nav = self._get_remote_capabilities(browser)
                driver = self._create_remote_driver(capabilities_nav, grid_url)
            else:
                if browser == "Chrome_Remote":
                    driver = self._create_chrome_remote_driver(grid_url)
                elif browser == "Edge_Remote":
                    driver = self._create_edge_remote_driver(grid_url)
            return driver
        else:  #Instancia Navegador Local
            if browser == "Chrome":
                self.driver = self._create_chrome_driver()
                return self.driver
            elif browser == "Firefox":
                driver = self._create_firefox_driver()
                return self.driver
            elif browser == "Edge":
                driver = self._create_edge_driver()
                return self.driver
            else:
                raise ValueError(f"Navegador {browser} no soportado.")
    
    #Crea y configura el driver de Chrome usando webdriver-manager
    def _create_chrome_driver(self):
        options = OpcionesChrome()
        prefs = {
             "profile.default_content_settings.popups": 0,
             "download.default_directory": Inicializar.Ruta_Descarga,
             "directory_upgrade":True ,
             "download.prompt_for_download": False,#Para que el navegador no pregunte al descargar
             #"plugins.always_open_pdf_externally": True}) # Para que el navegador no abra el PDF en una pestaña nueva
             #"plugins.plugins_disabled" : ["Chrome PDF Viewer"]
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument('start-maximized')
        #options.add_argument("headless")
        options.add_argument("--disable-extensions")#Deshabilita extensiones innecesarias
        
        chrome_driver_path = ChromeDriverManager().install() #Usa webdriver-manager para obtener la última versión compatible
        driver = webdriver.Chrome(service=ChromeService(chrome_driver_path), options=options)
        return driver
    
    #Crea y configura el driver de Firefox usando webdriver-manager
    def _create_firefox_driver(self):
        options = OpcionesFirefox()
        options.add_argument('--window-size=800,800')  # Maximiza la ventana
        driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()),options=options) #Usa webdriver-manager para obtener la última versión compatible
        return driver
    
    #Crea y configura el driver de Edge de manera local usando webdriver-manager
    def _create_edge_driver(self):
        options = OpcionesEdge()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(service =EdgeService(EdgeChromiumDriverManager().install()),options=options)
        #driver.maximize_window()
        return driver
    
    #Crea y configura el driver de Chrome Remote de Selenium Grid
    def _create_chrome_remote_driver(self, grid_url : str):
        options = OpcionesChrome()
        prefs = {
             "profile.default_content_settings.popups": 0,
             "download.default_directory": Inicializar.Ruta_Descarga,
             "directory_upgrade":True 
        }
        options.add_experimental_option("prefs",prefs)
        options.add_argument('start-maximized')
        
        driver = webdriver.Remote(grid_url,options=options)
        return driver 
    
    #Crea y configura el driver de Edge Remote de Selenium Grid
    def _create_edge_remote_driver(self, grid_url : str):
        options = OpcionesEdge();
        options.add_argument("start-maximized")
        options.add_argument("inprivate")
        #options.add_argument("headless")
    
        driver = webdriver.Remote(grid_url,options=options)
        return driver
    
    #Devuelve las capacidades del navegador para la conexión remota en Selenium Grid
    def _get_remote_capabilities(self, browser: str):
        if browser == "chrome":
            capabilities = DesiredCapabilities.CHROME.copy()
            capabilities['browserName'] = 'chrome'
            capabilities['platform'] = 'ANY'  # Puede ser Windows, Linux, etc.
        elif browser == "firefox":
            capabilities = DesiredCapabilities.FIREFOX.copy()
            capabilities['browserName'] = 'firefox'
            capabilities['platform'] = 'ANY'
        elif browser == "edge":
            capabilities = DesiredCapabilities.EDGE.copy()
            capabilities['browserName'] = 'MicrosoftEdge'
            capabilities['platform'] = 'ANY'
        else:
            raise ValueError(f"Navegador {browser} no soportado en Selenium Grid.")
        return capabilities

    #Crea el driver remoto conectado a Selenium Grid
    def _create_remote_driver(self, capabilities, grid_url: str):
        return webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)

    #Cierra el navegador
    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
        else:
            print("No hay un driver activo para cerrar.")
