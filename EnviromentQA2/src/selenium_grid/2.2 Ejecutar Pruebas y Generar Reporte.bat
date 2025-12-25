echo ## Ir a la carpeta del archivo ##
cd "C:\Users\dmefr\OneDrive\Escritorio\FW_Pruebas_Python_Selenium_VSCode\EnviromentQA\src"

echo ## Ejecucion del Archivo desde la Consola ##
python -m pytest Test\test39.py --alluredir allure-results

echo ## Fin de la ejecucion del archivo ##
pause
allure generate "C:\Users\dmefr\OneDrive\Escritorio\FW_Pruebas_Python_Selenium_VSCode\EnviromentQA\src\allure-results" --output "C:\Users\dmefr\OneDrive\Escritorio\FW_Pruebas_Python_Selenium_VSCode\EnviromentQA\src\allure-report" --clean

pause
