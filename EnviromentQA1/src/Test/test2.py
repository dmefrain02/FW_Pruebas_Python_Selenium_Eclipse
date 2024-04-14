
import unittest
import selenium

class Test(unittest.TestCase):


    def setUp(self):
        self.Numero1 = 575
        self.Numero2 = 575 
        self.Numero3 = 875 #1450
        self.Texto = 'Esto es un texto en Python'
        self.Lista = ['Hyundai','Honda','Ferrari','Lamborghini']
        self.Diccionario_Numero = {
            'Num1':'1',
            'Num2':'2',
            'Num3':'3'
        }

    def test001(self):
        self.Resultado = self.Numero2 + self.Numero3

    def tearDown(self):
                
        self.assertEqual(self.Numero3,self.Numero2,
                            f"Los numeros no son iguales, los numeros son: {self.Numero3} y {self.Numero2}")
        #self.assertNotEqual(self.Numero1,self.Numero2,
                            #f"Los numeros son iguales, los numeros son: {self.Numero1} y {self.Numero2}")
        #self.assertTrue(self.Resultado == 1454,f"El resultado no es el esperado, el resultado es: {self.Resultado}")
        #self.assertFalse(self.Resultado == 1450,f"El resultado si es: {self.Resultado}")
        #self.assertIs(self.Texto, self.Texto, 
                            #f"Los valores no son iguales, los valores no son iguales : {self.Texto} y {self.Texto}")
        #self.assertIsNot(self.Texto, self.Lista[0], 
                            #f"Los valores son iguales, los valores no son iguales : {self.Texto} y {self.Lista[0]}")
        #self.assertIn('Hyundai',self.Lista,
                            #f"El valor no se encuentra en la lista, la lista es: {self.Lista}")
        #self.assertNotIn('Hyundai3',self.Lista,
                            #f"El valor se encuentra en la lista, la lista es: {self.Lista}")
        #self.assertListEqual(self.Lista, self.Lista, f"Las listas no son iguales")
        self.assertDictEqual(self.Diccionario_Numero, self.Diccionario_Numero, f"Los diccionarios no son iguales")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()