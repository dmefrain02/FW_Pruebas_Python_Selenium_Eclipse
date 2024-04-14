import pytest,os
import logging

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()

#############################################################################

def setup_module(module):
    ''' Setup for the entire module '''
    mylogger.info('Preparando Configuraciones del Modulo para las pruebas')

def setup_function(func):
    ''' Setup for test functions '''
    if func == test_one:
        mylogger.info('Ejecutando pruebas')

def test_one():
    ''' Test One '''
    mylogger.info('Prueba 1')
    Num1 = 34
    Num2 = 35
    Resultado = Num1 + Num2
    assert Resultado == 69
    mylogger.info('Se ejecuto la prueba 1')

def test_two():
    ''' Test Two '''
    mylogger.info('Prueba 2')
    Num1 = 44
    Num2 = 45
    Resultado = Num1 + Num2
    assert Resultado == 89
    mylogger.info('Se ejecuto la prueba 2')

if __name__ == '__main__':
    mylogger.info(' Se inician las pruebas')
    pytest.main(args=[os.path.abspath(__file__)])
    mylogger.info(' Se finalizaron las pruebas ')