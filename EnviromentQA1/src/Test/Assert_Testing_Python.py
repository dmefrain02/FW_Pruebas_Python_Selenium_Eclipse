import unittest
import selenium

class Test(unittest.TestCase):


    def setUp(self):
        self.Numero1 = 575
        self.Numero2 = 575
        self.Numero3 = 857 #1432
        self.Texto = 'Esto es un texto en Python'
        self.Lista = ['Hyundai','Honda','Ferrari','Lamborghini']
        self.Lista2 = ['Hyundai','Lamborghini']
        self.Diccionario_Numero = {
            'Num1':'1',
            'Num2':'2',
            'Num3':'3'
        }
        self.Diccionario_Texto = {
            'Texto1':'Hola',
            'Texto2':'Python',
            'Texto3':'Diccionario'
        }

    def test_001(self):
        self.Resultado = self.Numero2 + self.Numero3

    def tearDown(self):
        #self.assertEqual(self.Numero2, self.Numero3, f'Los numeros no son iguales, los numeros son: {self.Numero2} y {self.Numero3}')
        #self.assertNotEqual(self.Numero1,self.Numero2, f'Los numeros son iguales, los numeros son: {self.Numero1} y {self.Numero2}')
        #self.assertTrue(self.Resultado == 1432, f'El resultado es incorrecto, el resultado es: {self.Resultado}')
        #self.assertFalse(self.Resultado == 1432, f'El resultado si es: {self.Resultado}')
        #self.assertIs(self.Texto, self.Lista[0], f'El valor del texto no es el mismo, el texto es: {self.Texto} y {self.Lista[0]}')
        #self.assertIsNot(self.Lista[0], self.Lista[1],f'Los valores son los mismos, los valores son: {self.Lista[0]} y {self.Lista[1]}')
        #self.assertIn(self.Texto, self.Lista, f'El valor {self.Texto} no se encuentra en la lista {self.Lista}')
        #self.assertNotIn(self.Lista[0], self.Lista, f'El valor {self.Lista[0]} se encuentra en la lista {self.Lista}')
        #self.assertListEqual(self.Lista, self.Lista, f'Las listas no son iguales')
        self.assertDictEqual(self.Diccionario_Texto, self.Diccionario_Texto, f'Los diccionarios no son iguales')
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()