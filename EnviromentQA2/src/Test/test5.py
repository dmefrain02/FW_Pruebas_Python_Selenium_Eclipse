
import unittest
import re
import selenium

class Test(unittest.TestCase):

        #Expresiones Regulares en Python
        text = "ID 123456: Esto es un texto en Python"
        
        patron2 = r"(^\w+)"
        patron3 = r"\s"
        patron4 = r"\d+"
        patron5 = r"\D+"
        
        #Imprension de una busqueda con RegExp
        matching = re.findall('123456',text)
        print(matching)            
        
        matching2 = re.findall('Python',text)
        print(matching2)       
        
        matching3 = re.findall('ID|Python',text)
        print(matching3)      
        
        print(re.findall(str(patron2),text, re.IGNORECASE))
        
        #Impresion del resultado de la busqueda con un For
        for resultado in matching:
            print(resultado)
            
        variables = re.findall(str(patron2),text, re.IGNORECASE)
        for variable in variables:
            print(variable)
            if variable == 'ID':
                #Sustituir valor con Regex
                 text_sub = re.sub(patron2,'ID-TextoSustituido',text,re.IGNORECASE)
                 print(text_sub)
                 
        search = re.search(patron2, text,re.IGNORECASE)
        if search:
            print(search)
        
        search = re.search(patron5, text,re.IGNORECASE)
        if search:
            print(search)
            
        print(re.search(patron4, text))
        
        #Impresion de Busqueda con Split
        print(re.split(patron3,text, re.IGNORECASE))
        
        #Impresion busqueda con Splir con For
        Splits = re.split(patron3,text, re.IGNORECASE)
        for Split in Splits:
            print(Split)