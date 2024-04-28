# -*- coding: utf-8 -*-
import os

class Inicializar():
    
    URL_SeleniumGrid = "http://localhost:4444/wd/hub"
    
    #Directorio Base - Obtiene la ruta del directorio src del proyecto
    BaseDir = os.path.abspath(os.path.join(__file__,"../.."))
    
    #Tiempo de espera utilizado dentro del Framework
    Tiempo_Espera = 1
    
    #Pagina en nuevo tab abierto
    Page_Tab = 'about:blank'
    
    #Rutas utilizadas dentro del Framework
    Archivo_Cargar = BaseDir + u'\Archivos a Cargar\software-quality.png'
    Ruta_Descarga = BaseDir + u'\Archivos Descargados'
    Archivo_Descargado = "requirements.txt"
    Bitacora= BaseDir + u'\Archivos Descargados\Pruebas Descargas Archivos.txt'
    Imagenes_Cortadas = BaseDir + u'\Data\Imagenes Cortadas'
    Ruta_Grabacion= BaseDir + u'\Data\Grabaciones'
    Path_Evidencias = BaseDir + u'\Data\Capturas'
    
    #DirectorioJson
    Json = BaseDir + u'\Pages'
    JsonRespondata = BaseDir + u'\Data\Json'
    
    #Formato Hora y Fecha
    DateFormat = '%d-%m-%Y'
    HourFormat = '%H%M%S'
    
    #Navegador a Utilizar
    Navegador = u'Chrome'
    
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