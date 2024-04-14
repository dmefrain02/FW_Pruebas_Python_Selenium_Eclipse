# -*- coding: utf-8 -*-
import os

class Inicializar():
    
    Tiempo_Espera = 1
    #Pagina en nuevo tab abierto
    Page_Tab = 'about:blank'
    Archivo_Cargar = "C:\\Users\\dmefr\\Desktop\\Carpeta MEGA\\Videos QA\\software-quality.png"
    Ruta_Descarga = "C:\\Users\\dmefr\\Desktop\\Carpeta MEGA\\Videos QA\\Curso Automatizacion Pruebas\\Framework Pruebas Automatizadas\\Entornos Virtuales\\EnviromentQA\\Framework Automatizacion Pruebas Python\\src\\Archivos Descargados"
    Archivo_Descargado = "requirements.txt"
    Bitacora= "C:\\Users\\dmefr\\Desktop\\Carpeta MEGA\\Videos QA\\Curso Automatizacion Pruebas\\Framework Pruebas Automatizadas\\Entornos Virtuales\\EnviromentQA\\Framework Automatizacion Pruebas Python\\src\\Archivos Descargados\\Pruebas Descargas Archivos.txt"
    
    #Directorio Base
    BaseDir = os.path.abspath(os.path.join(__file__,"../.."))#Obtiene la ruta del directorio src del proyecto
    
    Imagenes_Cortadas = BaseDir + u'\Data\Imagenes Cortadas'
    
    DateFormat = '%d-%m-%Y'
    HourFormat = '%H%M%S'
    
    #DirectorioJson
    Json = BaseDir + u'\Pages'
    JsonRespondata = BaseDir + u'\Data\Json'
    
    #Navegador a Utilizar
    Navegador = u'Chrome'
    
    #Directorio de Pruebas
    Path_Evidencias = BaseDir + u'\Data\Capturas'
    
    #Ruta Excel para escribir resultados o leer datos
    Excel_Leer_Escribir = BaseDir + u'\Data\Pruebas1.xlsx'
    
    #Ruta Excel para crear excel
    Excel_Crear = BaseDir + u'\Data'
    
    #Ambientes de Pruebas
    Enviroment = 'Test'
    if Enviroment == 'Dev':
        URL = f'' #La f solo va si requerimos pasarle parametros en el link
        USER = ''
        DB_HOST = 'EFRAIN-CD'
        DB_PORT = '1433'
        DB_DATABASE = 'Pruebas_Automatizadas_Python'
        DB_USER = 'EFRAINCD'
        DB_PASS = 'EfCastaned-2023' 
    if Enviroment == 'Test':
        URL = f'' #La f solo va si requerimos pasarle parametros en el link
        USER = ''
        DB_HOST = 'EFRAIN-CD'
        DB_PORT = ''
        DB_DATABASE = 'Pruebas_Automatizadas_Python'
        DB_USER = 'EFRAINCD'
        DB_PASS = 'EfCastaned-2023' 