<<<<<<< HEAD:EnviromentQA1/src/selenium_grid/Versiones Selenium Grid/Selenium_Server.bat
start java -jar selenium-server-4.21.0.jar standalone -role hub -hubConfig hubconfig.json

start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -Dwebdriver.edge.driver="msedgedriver.exe" -jar selenium-server-4.21.0.jar standalone -role node -nodeConfig nodeconfig1.json
start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -Dwebdriver.edge.driver="msedgedriver.exe" -jar selenium-server-4.21.0.jar standalone -role node -nodeConfig nodeconfig2.json
start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -Dwebdriver.edge.driver="msedgedriver.exe" -jar selenium-server-4.21.0.jar standalone -role node -nodeConfig nodeconfig3.json
start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -Dwebdriver.edge.driver="msedgedriver.exe" -jar selenium-server-4.21.0.jar standalone -role node -nodeConfig nodeconfig4.json
=======
start java -jar selenium-server-standalone-3.5.3.jar -role hub -hubconfig hubconfig.json

start java -jar -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -jar selenium-server-standalone-3.5.3.jar -role node -id node_1 -nodeconfig nodeconfig1.json
start java -jar -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -jar selenium-server-standalone-3.5.3.jar -role node -id node_2 -nodeconfig nodeconfig2.json
>>>>>>> main:EnviromentQA1/src/selenium_grid/Selenium_Server.bat
