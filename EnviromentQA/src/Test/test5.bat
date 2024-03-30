echo ## Ir a la carpeta del archivo ##
cd "C:\Users\dmefr\Desktop\Carpeta MEGA\Videos QA\Curso Automatizacion Pruebas\Framework Pruebas Automatizadas\Entornos Virtuales\EnviromentQA\Framework Automatizacion Pruebas\src\Test"

echo ## Ejecucion del Archivo desde la Consola ##
python -m pytest Test18.py --junitxml=..\Results\results.xml
python -m pytest Test18.py --html=..\Results\results1.html --self-contained-html

echo ## Fin de la ejecucion del archivo ##
pause