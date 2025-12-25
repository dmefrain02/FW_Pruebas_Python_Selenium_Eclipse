import unittest
from behave import given, when, then
from Function.Functions import Functions as Selenium
from Function.Inicializar import Inicializar

@given('el usuario abre el navegador e ingresa a la seccion de Alerts en la página de DemoQA')
def step_open_browser(context):
    Selenium.obtener_archivo_json(context, 'Localizadores_Spotify')

@when('Se realiza click en el boton del alert')
def step_hacer_click_boton(context):
    Selenium.abrir_navegador(context,"Chrome")
    Selenium.get_url_driver(context,"https://demoqa.com/alerts")
    Selenium.WebdriverWait(context,2)
    Selenium.click_en_elemento(context, "btn-txt-ing")
    Selenium.esperar_elemento(context, 2)

@then('Se visualiza el mensaje Alert')
def step_mostrar_alert(context):
    Selenium.alert_navegadores(context,4,"","","You entered","texto-ing", "Test")
    Selenium.WebdriverWait(context,2)
    Selenium.cerrar_driver_navegador(context) 