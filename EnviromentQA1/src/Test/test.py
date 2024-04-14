'''
Created on 15 ene 2023
@author: dmefr
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):

        '''
        Comentario Multilinea
        '''
        #Comentario simple
        
        self.Numero1 = 25
        self.Numero2 = 30
        self.Contador = 0
        self.Texto = ' Hola Mundo, esto es un texto en Python'
        self.Lista = ['Hyundai','Honda','Ferrari','Lamborghini']
        self.Lista2 = ['Yamaha','Harley']
        self.ListaNum = [0,5,1,3,4]
        self.Dicc = dict() #Diccionario vacio inicializado con dict()
        self.DiccNum = {} #Diccionario vacio inicializado con {}
        
    def testName(self):
        self.Resultado = self.Numero1 + self.Numero2
        self.Resultado2 = str(self.Numero1) + self.Texto
        
        #Imprimir variables
        print(f'El resultado es: {self.Resultado}')
        print(f'El resultado es: ' + str(self.Resultado))
        print(f'El resultado es: {self.Resultado2}')
        print(f'El resultado es: ' + self.Resultado2)
        
        #Imprimir variables
        #self.Resultado1 = self.Numero1 + self.Texto
        #print(self.Resultado1)
        
        #Imprimir lista
        print(f'La lista es: {self.Lista}')
        #Imprimir elemento de lista
        print(f'El primer elemento en la lista es: {self.Lista[0]}')
        
        #Manejo de lista en un For e impresion de toda la lista
        for ElementoLista in self.Lista:
            print(ElementoLista)
        
        #Manejo de lista en un For e impresion de un elemento
        for ElementoLista in self.Lista:
            if ElementoLista == 'Hyundai':
                print(ElementoLista) 
                continue
            if ElementoLista == 'Honda':
                print(ElementoLista) 
                break
        
        #Manejo de lista en un For, agregar un elemento e impresion al final
        for ElementoLista in self.Lista:
            if ElementoLista == 'Ferrari':
                self.Lista.append('Geo')
                print(self.Lista)
                break
               
        #Manejo de lista en un For, agregar un elemento e impresion en posicion concreto
        for ElementoLista in self.Lista:
            if ElementoLista == 'Honda':
                self.Lista.insert(1,'Mitsubishi')
                print(self.Lista)
                break
                
        #Manejo de lista en un For, remover un elemento e impresion
        for ElementoLista in self.Lista:
            if ElementoLista == 'Ferrari':
                self.Lista.remove(self.Lista[0])
                print(self.Lista)
        
                
        #Sustituir un valor en la lista
        self.ListaNum[1] = 10
        print(self.Lista)
        
        #Eliminar un elemento de la lista por clave
        self.ListaNum.pop(2)
        print(self.ListaNum)
        
        self.ListaNum.pop()
        print(self.ListaNum)

        #Unir listas
        print(self.Lista + self.Lista2)
        
        #Multiplicar los valores de la lista   
        print(self.Lista2 *2)
        
        #Ordernar lista ascendenmente
        self.ListaNum.sort()
        self.Lista.sort()
        print(self.ListaNum)
        print(self.Lista)
        
        #Voltear la lista
        self.Lista.reverse()
        print(self.Lista)
        
        #Limpiar lista
        self.Lista.clear()
        self.Lista2.clear()
        self.ListaNum.clear()
        print(self.Lista)
        print(self.Lista2)
        print(self.ListaNum)
        
        #Uso del While
        while self.Contador <10:
            print(f'El Contador esta en: {self.Contador}')
            self.Contador = self.Contador + 1
            
        #Inicializacion de diccionarios con datos
        self.Dicc =  {'Texto':'Hola Mundo','Texto2':'Python'}
        self.DiccNum = {
            'Num1':'1',
            'Num2':'2'
        }
        
        #Imprimir Diccionarios
        print(self.Dicc['Texto'])
        print(self.DiccNum['Num1'])
        
        #Recorrer las keys del diccionario e imprimirlas
        for key in self.Dicc.keys():
            #self.Dicc['Texto3'] = 'Texto3'
            print(key)
        
        #Recorrer los values del diccionario e imprimirlos
        for values in self.DiccNum.values():
           print(values)
        
        #Recorrer los keys y values del diccionario e imprimirlos
        for key, values in self.Dicc.items():
            print(f'key: {key}, values: {values}')
            
        #Obtener un valor del diccionario por la key
        print(self.Dicc.get('Texto'))
        print(self.Dicc.get('ABC','Mundo'))
        
        #Convertir diccionario en lista para imprimir todas las claves del diccionario
        print(list(self.Dicc))
        
        #Obtener cantidad de elementos en el diccionario
        print(len(self.Dicc))
        
        #operador in y not in, para verificar si una clave esta o no dentro de un diccionario
        result = 'Texto' in self.Dicc
        print(result)
        
        result = 'ABC' not in self.Dicc
        print(result)
        
        #Limpiar diccionarios
        self.Dicc.clear()
        self.DiccNum.clear()
        print(self.Dicc)
        print(self.DiccNum)
        
    def tearDown(self):
        pass

    def testName_prueba(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()