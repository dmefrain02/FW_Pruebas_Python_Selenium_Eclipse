echo ## Ir a la carpeta del archivo ##
cd "C:\Users\dmefr\Desktop\FW_Pruebas_Python_Selenium\FW_Pruebas_Python_Selenium\EnviromentQA1\src"

echo ## Ejecucion del Archivo desde la Consola ##
python -m pytest test44.py --alluredir allure-results

echo ## Fin de la ejecucion del archivo ##
pause
allure generate "C:\Users\dmefr\Desktop\FW_Pruebas_Python_Selenium\FW_Pruebas_Python_Selenium\EnviromentQA1\src\allure-results" --output "C:\Users\dmefr\Desktop\FW_Pruebas_Python_Selenium\FW_Pruebas_Python_Selenium\EnviromentQA1\src\allure-report" --clean

pause
