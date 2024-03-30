
import unittest

class Test(unittest.TestCase):


    def setUp(self):
        self.Numero = 25
        self.Numero2 = 30
        self.Contador = 0
        self.Texto = ' Hola Mundo, esto es un texto en Python'
        self.Lista = ['Hyundai','Honda','Ferrari','Lamborghini']
        self.Lista2 = ['Yamaha','Harley']
        self.ListaNum = [0,5,1,3,4]
        
        '''
        Comenatario Multilinea
        '''
        #Comentario Simple
        """
        Comentario Multilinea
        """

    def testName(self):
        
        #Operaciones con Variables
        self.Resultado = self.Numero + self.Numero2
        self.Resultado2 = str(self.Numero) + self.Texto
        self.Resultado3 = str(self.Numero) + self.Texto
        
        #Imprimir Variables
        print('El resultado es: ' + str(self.Resultado))
        print(f'El resultado es: {self.Resultado2}')
        print(f'El resultado es: {self.Resultado3}')
        
        print(self.Lista)
        print(f'Esta es una lista: {self.Lista}')
        print(f'Este es un elemento de la lista: {self.Lista[0]}')
        print(self.Lista[1])
        
        #Uso de variables en For e If
        
        for ElementoLista in self.Lista:
            if ElementoLista == 'Hyundai':
                print(ElementoLista)
                continue
            if ElementoLista == 'Honda':
                print(ElementoLista)
                break
            
        for ElementoLista in self.Lista:
            if ElementoLista == 'Ferrari':
                self.Lista.append('Geo')
                print(self.Lista)
                break
            
        for ElementoLista in self.Lista:
            if ElementoLista == 'Honda':
                self.Lista.insert(1,'Mitsubishi')
                print(self.Lista)
                break
            
        for ElementoLista in self.Lista:
            if ElementoLista == 'Ferrari':
                self.Lista.remove(self.Lista[0])
                print(self.Lista)
                break
        
        #Sustituir un valor en la lista
        print(self.ListaNum)  
        self.ListaNum[1]=10
        print(self.ListaNum)
            
        #Reverse a la lista
        print(self.Lista)
        self.Lista.reverse()
        print(self.Lista)
        
        #Eliminar un elemento de la lista por clave
        print(self.ListaNum)
        self.ListaNum.pop(2)
        print(self.ListaNum)
        
        print(self.ListaNum)
        self.ListaNum.pop()
        print(self.ListaNum)
        
        #Unir listas
        print(self.Lista + self.Lista2)
        print(self.Lista + self.ListaNum + self.Lista)
        
        #Multiplicar los valores de la lista
        print(self.Lista2 *3)
        
        #Ordernar lista ascendenmente
        print(self.Lista)
        print(self.ListaNum)
        self.ListaNum.sort()
        self.Lista.sort()
        print(self.Lista)
        print(self.ListaNum)
        
        #Limpiar lista
        self.Lista.clear()
        self.Lista2.clear()
        self.ListaNum.clear()
        print(self.Lista)
        print(self.Lista2)
        print(self.ListaNum)
        
        #Uso del while
        while self.Contador <= 10:
            print(f'El contador se encuentra en: {self.Contador}')
            self.Contador = self.Contador + 1
        

    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()