import unittest
import re
import selenium

class Test(object):

    #Expresiones Regulares en Python
    text = "ID 123456: Esto es un texto en Python ID"
    
    patron2 = r"(^\w+)"
    patron3 = r"\s"
    patron4 = r"\d+"
    patron5 = r"\D+"
    
    matching = re.findall('123456', text)
    print(matching)
    matching2 = re.findall('Python',text)
    print(matching2)
    matching3 = re.findall('Python|ID',text)
    print(matching3)
    
    print(re.findall(patron2,text,re.IGNORECASE))
    
    for resultado in matching3:
        print(resultado)
        
    variables = re.findall(str(patron2),text,re.IGNORECASE)
    for variable in variables:
        print(variable)
        if variable == 'ID':
            text_sub = re.sub(patron2, 'ID_Texto-Sust', text,re.IGNORECASE)
            print(text_sub)
            
    search = re.search(patron2, text,re.IGNORECASE)
    if search:
        print(search)
        
    print(re.search(patron4,text))
    print(re.split(patron3, text, re.IGNORECASE))
    Splits = re.split(patron3,text,re.IGNORECASE)
    for Split in Splits:
        print(Split)