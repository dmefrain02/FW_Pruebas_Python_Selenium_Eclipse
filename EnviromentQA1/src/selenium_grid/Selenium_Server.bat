start java -jar selenium-server-standalone-3.5.3.jar -role hub -hubConfig hubconfig.json

start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -jar selenium-server-standalone-3.5.3.jar -role node -nodeConfig nodeconfig1.json
start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -jar selenium-server-standalone-3.5.3.jar -role node -nodeConfig nodeconfig2.json