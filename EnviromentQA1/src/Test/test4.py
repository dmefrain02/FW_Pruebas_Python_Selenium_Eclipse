'''
Created on 18 feb 2023

@author: dmefr
'''
import unittest
import selenium

class Test(unittest.TestCase):


    def setUp(self):
        self.Num1 = 5
        self.Num2 = 15

    def test1(self):
        self.Resultado = self.Num1 + self.Num2
        
    def tearDown(self):
        self.assertTrue(self.Resultado == 20, f'EL resultado de la suma no es correcto, el resultado es: {self.Resultado}')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()