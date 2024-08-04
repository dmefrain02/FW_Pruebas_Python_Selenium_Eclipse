# -*- coding: utf-8 -*-
import os

class Inicializar():
    
    URL_SeleniumGrid = "http://localhost:4444/wd/hub"
    Navegadores_Sel_Grid = ["Edge_Remote","Chrome_Remote"]
    
    #Directorio Base - Obtiene la ruta del directorio src del proyecto
    BaseDir = os.path.abspath(os.path.join(__file__,"../.."))
    
    #Variable en el archivo inicializar
    URL_SeleniumGrid = "http://localhost:4444/wd/hub"
    Navegadores_Sel_Grid = ["Chrome","Edge_Remote","Chrome_Remote"]
    
    
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
    #Path_Evidencias = ""
    TestCase_x_Context = "S" #S o N
    
    #Directorio Json
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
    #Enviroment == 'Dev':
    URL_Dev = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_Dev = ''
    DB_HOST_Dev = 'EFRAIN-CD\EFRAINCD'
    DB_PORT_Dev = '1433'
    DB_DATABASE_Dev = 'Pruebas_Automatizadas_Python_DEV'
    DB_USER_Dev = 'EFRAIN_ACD'
    DB_PASS_Dev = '114660137'
    
    #Enviroment == 'QA':    
    URL_QA = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_QA = ''
    DB_HOST_QA = 'EFRAIN-CD\EFRAINCD'
    DB_PORT_QA = '1433'
    DB_DATABASE_QA = 'Pruebas_Automatizadas_Python_QA'
    DB_USER_QA = 'EFRAIN_ACD'
    DB_PASS_QA = '114660137' 
    #Enviroment == 'UAT':
    URL_UAT = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_UAT = ''
    DB_HOST_UAT = 'EFRAIN-CD\EFRAINCD'
    DB_PORT_UAT = '1433'
    DB_DATABASE_UAT = 'Pruebas_Automatizadas_Python_UAT'
    DB_USER_UAT = ''
    DB_PASS_UAT = '' 
    #Enviroment == 'PROD':
    URL_PROD = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_PROD = ''
    DB_HOST_PROD = 'EFRAIN-CD\EFRAINCD'
    DB_PORT_PROD = '1433'
    DB_DATABASE_PROD = 'Pruebas_Automatizadas_Python_PROD'
    DB_USER_PROD = ''
    DB_PASS_PROD = '' 