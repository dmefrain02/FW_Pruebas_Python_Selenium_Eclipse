from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from src.Function.Functions import Functions as Selenium
from src.Function.Inicializar import Inicializar

@when('Prueba en Mercado Libre')
def step_open_browser(context):
    Selenium.obtener_archivo_json(context,"Localizadores_Mercado_Libre")
    #for Nav_Sel_Grid in Inicializar.Navegadores_Sel_Grid:
    Selenium.abrir_navegador(context,"Chrome")
    Selenium.esperar_elemento(context)
    
    Selenium.get_url_driver(context, 'https://www.mercadolibre.co.cr/')
    Selenium.esperar_elemento(context)
    Selenium.capturar_pantalla(context)
    
    Selenium.escribir_texto(context, "Busqueda_Mercado_Libre", "Consola PS5")
    Selenium.esperar_elemento(context)
    Selenium.capturar_pantalla(context)
    
    Selenium.envio_teclas_especificas(context, "Busqueda_Mercado_Libre", "Enter")
    Selenium.esperar_elemento(context)
    Selenium.capturar_pantalla(context)
    
    assert Selenium.obtener_elemento(context, "Producto_Buscado").is_displayed()
    Selenium.cerrar_driver_navegador(context)
    print("Navegador cerrado correctamente.")