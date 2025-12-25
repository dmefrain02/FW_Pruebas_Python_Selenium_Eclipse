from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from src.Function.Functions import Functions as Selenium
import unittest
import HtmlTestRunner

@given('el usuario abre el navegador')
def step_open_browser(context):
    Selenium.obtener_archivo_json(context,"Localizadores_Spotify")
    Selenium.abrir_navegador(context,"Chrome")
    Selenium.capturar_pantalla(context)
    Selenium.esperar_elemento(context)

@when('ingresa a la pagina de Google')
def step_open_google(context):
    Selenium.get_url_driver(context, "https://www.google.com/")
    Selenium.esperar_elemento(context)
    
@When('usuario digita el texto {busqueda}')
def step_txt_busqueda(context, busqueda):
    #Selenium.escribir_texto(context,"APjFqb",busqueda)
    context.driver.find_element(By.ID, "APjFqb").send_keys(busqueda)
    Selenium.esperar_elemento(context)
    Selenium.capturar_pantalla(context)

@then('presiona la tecla Enter')
def step_click_login(context):
    #Selenium.envio_teclas_especificas(context, "APjFqb", Keys.ENTER)
    context.driver.find_element(By.ID, "APjFqb").send_keys(Keys.ENTER)   
    Selenium.esperar_elemento(context)
    Selenium.capturar_pantalla(context)
    
@then('esperar los resultados de la búsqueda')
def step_wait_results(context):
    time.sleep(2)
    Selenium.cerrar_driver_navegador(context)
    print("Navegador cerrado correctamente.")