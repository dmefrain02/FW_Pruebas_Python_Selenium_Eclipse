from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from src.Function.Functions import Functions as Selenium

@given('el usuario abre el navegador a DemoQA')
def step_open_browser(context):
    Selenium.obtener_archivo_json(context,"Localizadores_Spotify")
    Selenium.abrir_navegador(context,"Chrome")
    Selenium.esperar_elemento(context)

@when('ingresa a la pagina de DemoQA')
def step_open_google(context):
    Selenium.get_url_driver(context, 'https://demoqa.com/droppable')
    Selenium.esperar_elemento(context)
    Selenium.capturar_pantalla(context)
    
@When('usuario arrastra el elemento "Draggable" a la posición "100, 200"')
def step_mover_arrastrar(context):
    Selenium.Arrastrar_y_Soltar(context, 'draggable', 'droppable')
    Selenium.esperar_elemento(context)
    Selenium.capturar_pantalla(context)

@then('verifica que el elemento se ha movido a la nueva posición')
def step_click_login(context):
    #texto = Selenium.obtener_Texto(context,'text_drop')
    
    assert Selenium.obtener_Texto(context,'text_drop') == 'Dropped!', "El texto no coincide con lo esperado"
    Selenium.capturar_pantalla(context)

    Selenium.cerrar_driver_navegador(context)
    print("Navegador cerrado correctamente.")