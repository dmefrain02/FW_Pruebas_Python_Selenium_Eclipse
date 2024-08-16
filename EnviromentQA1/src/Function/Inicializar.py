# -*- coding: utf-8 -*-
import os

class Inicializar():
    
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
    TestCase_x_Context = "" #S o N
    Warning_Capturas = "Warning: Sin configurar el Path y el contexto para las capturas de pantalla."

    
    #Directorio Json
    Json = BaseDir + u'\Pages'
    JsonRespondata = BaseDir + u'\Data\Json'
    
    #Formato Hora y Fecha
    DateFormat = '%d-%m-%Y'
    HourFormat = '%H%M%S'
    
    #Navegador a Utilizar
    Navegador = u'Edge'
    
    #Ruta Excel para escribir resultados o leer datos
    Excel_Leer_Escribir = BaseDir + u'\Data\Pruebas1.xlsx'
    
    #Ruta Excel para crear excel
    Excel_Crear = BaseDir + u'\Data'
    
    #Ambientes de Pruebas
    #Enviroment == 'Dev':
    URL_Dev = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_Dev = ''
    Cadena_Conexion_Dev = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=EFRAIN-CD\EFRAINCD;DATABASE=Pruebas_Automatizadas_Python_DEV;UID=EFRAIN_ACD;PWD=114660137'

    #Enviroment == 'QA':    
    URL_QA = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_QA = '' 
    Cadena_Conexion_QA = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=EFRAIN-CD\EFRAINCD;DATABASE=Pruebas_Automatizadas_Python_QA;UID=EFRAIN_ACD;PWD=114660137'
    
    #Enviroment == 'UAT':
    URL_UAT = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_UAT = ''
    Cadena_Conexion_UAT = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=EFRAIN-CD\EFRAINCD;DATABASE=Pruebas_Automatizadas_Python_UAT;UID=EFRAIN_ACD;PWD=114660137'

    #Enviroment == 'PROD':
    URL_PROD = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_PROD = ''
    Cadena_Conexion_Prod = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=EFRAIN-CD\EFRAINCD;DATABASE=Pruebas_Automatizadas_Python_PROD;UID=EFRAIN_ACD;PWD=114660137'