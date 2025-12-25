Feature: Busqueda en Google

  Scenario: Realizar una búsqueda en Google
    Given el usuario abre el navegador
    When ingresa a la pagina de Google
    When usuario digita el texto QA Tecnology CRC Youtube
    Then presiona la tecla Enter
    And esperar los resultados de la búsqueda
  #  And Verifica que en los resultados de la búsqueda se muestre "CRC Youtube"

  Scenario: Mover elemento en la pantalla
    Given el usuario abre el navegador a DemoQA
    When ingresa a la pagina de DemoQA
    When usuario arrastra el elemento "Draggable" a la posición "100, 200"
    Then verifica que el elemento se ha movido a la nueva posición

  Scenario: Busqueda de producto en Mercado Libre
    When Prueba en Mercado Libre