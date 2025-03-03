
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        #Definicion de los diccionarios de datos
        self.Diccionario_Numero = dict()
        self.Diccinario_Texto = {}
        
    def testName(self):

        #Asignacion de Valores en los diccionarios
        self.Diccinario_Texto = {'Texto1':'Hola Mundo', 'Texto2':'Curso Automatizacion', 'Texto3': 'Python'}
        self.Diccionario_Numero = {
            'Num1':'1',
            'Num2':'2',
            'Num3':'3'
        }
        
        #Impresion de diccionarios
        print(self.Diccinario_Texto['Texto1'])
        print(self.Diccionario_Numero['Num3'])
        
        #Recorriendo los diccionarios
        for key in self.Diccinario_Texto.keys():
            print(key)
            
        for values in self.Diccionario_Numero.values():
            print(values)
            
        for key,values in  self.Diccinario_Texto.items():
            print(f'Key: {key}, values: {values}')
        
        #Obtener valor por la key
        print(self.Diccinario_Texto.get('Texto1'))
        print(self.Diccionario_Numero.get('Num4', 'No existe'))
    
        #Convertir en lista
        print(list(self.Diccinario_Texto))
        
        #Ontener cantidad de elementos
        print(len(self.Diccionario_Numero))
        
        #Operador not in e in
        result = 'Texto1' in self.Diccinario_Texto
        print(result)
        
        result = 'Num2' not in self.Diccionario_Numero
        print(result)
        
        self.Diccinario_Texto.clear()
        self.Diccionario_Numero.clear()
        print(self.Diccinario_Texto)
        print(self.Diccionario_Numero)

    def tearDown(self):
        pass
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()