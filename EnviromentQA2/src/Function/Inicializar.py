# -*- coding: utf-8 -*-
import os

class Inicializar():
    
    #Nombre por defecto video grabado en pruebas
    VideoPruebas = "Video_Prueba"
    Formato_Video = "mp4"
    ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
    
    '''Formatos_Soportados = {
        "mp4": {"codec": "libx264", "extra": ["-preset", "ultrafast", "-crf", "25"]},
        "avi": {"codec": "libxvid", "extra": ["-q:v", "5"]},
        "mkv": {"codec": "libx264", "extra": ["-preset", "medium", "-crf", "23"]},
        "webm": {"codec": "libvpx", "extra": ["-b:v", "1M"]}
    }'''
    
    #Directorio Base - Obtiene la ruta del directorio src del proyecto
    BaseDir = os.path.abspath(os.path.join(__file__,"../.."))
    
    Carpeta_Videos = BaseDir + u'\Data\Videos'
    
    #Variable en el archivo inicializar
    PortSelGrid = "4444"
    URL_SeleniumGrid = r"http://localhost:"+PortSelGrid+"/wd/hub"
    #Para utilizar con Docker Compose. Si quiere utilizar con Dockers individuales, se requiere dejar solo el browser en docker a enviar el browser docker por medio de la variable navegador.
    Navegadores_Sel_Grid = ["Chrome_Docker","Firefox_Docker"]
    #Navegadores_Sel_Grid = ["Chrome_Docker","Edge_Docker","Firefox_Docker"]
    #Navegadores_Sel_Grid = ["Chrome_Remote","Edge_Remote"]#,"Firefox_Remote"]
    
    #Tiempo de espera utilizado dentro del Framework
    Tiempo_Espera = 1
    
    #Pagina en nuevo tab abierto
    Page_Tab = 'about:blank'
    
    #Rutas utilizadas dentro del Framework
    Archivo_Cargar = BaseDir + r'\Archivos a Cargar\software-quality.png'
    Ruta_Descarga = BaseDir + r'\Archivos Descargados'
    Archivo_Descargado = "requirements.txt"
    Bitacora= BaseDir + r'\Archivos Descargados\Pruebas Descargas Archivos.txt'
    Imagenes_Cortadas = BaseDir + r'\Data\Imagenes Cortadas'
    Ruta_Grabacion= BaseDir + r'\Data\Grabaciones'
    Path_Evidencias = BaseDir + r'\Data\Capturas'
    #Path_Evidencias = ""
    TestCase_x_Context = "S" #S o N
    Warning_Capturas = "Warning: Sin configurar el Path y el contexto para las capturas de pantalla."
      
    #Directorio Localizadores en formato JSON
    Json = BaseDir + r'\Localizadores'
    JsonRespondata = BaseDir + r'\Data\Json'
    
    #Formato Hora y Fecha
    DateFormat = '%d-%m-%Y'
    HourFormat = '%H%M%S'
    
    #Navegador a Utilizar
    Navegador = 'Edge'
    
    #Ruta Excel para escribir resultados o leer datos
    Excel_Leer_Escribir = BaseDir + r'\Data\Pruebas1.xlsx'
    
    #Ruta Excel para crear excel
    Excel_Crear = BaseDir + r'\Data'
    
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

    ## Ejecutar pruebas en behave en consola ##
    #En consola: behave
    
    ## Ejecutar pruebas en behave con generacion de reportes allure y html en consola 

    #Allure
    #behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
    #behave -f allure_behave.formatter:AllureFormatter -o allure-results
    #allure serve reports/allure-results
    #allure serve allure-results

    #Generar reporte Allure limpiar resultados anteriores
    #allure generate reports/allure-results -o reports/allure-report --clean
    #allure generate allure-results -o allure-report --clean

    #Reporte HTML
    #behave -f behave_html_formatter:HTMLFormatter -o reports/html_report.html