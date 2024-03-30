echo ## Ir a la carpeta del archivo ##
cd "C:\Users\dmefr\Desktop\Carpeta MEGA\Framework Pruebas Automatizadas\EnviromentQA\src"

echo ## Ejecucion del Archivo desde la Consola ##
python -m pytest test37.py --alluredir allure-results

echo ## Fin de la ejecucion del archivo ##
pause