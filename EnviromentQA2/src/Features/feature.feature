Feature: Manejo Alertas

  Scenario: Manejar Alerta con botones OK y Cancelar
    Given el usuario abre el navegador e ingresa a la seccion de Alerts en la página de DemoQA
    When Se realiza click en el boton del alert
    Then Se visualiza el mensaje Alert