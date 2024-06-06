start java -jar selenium-server-4.21.0.jar standalone -role hub -hubConfig hubconfig.json

start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -Dwebdriver.edge.driver="msedgedriver.exe" -jar selenium-server-4.21.0.jar standalone -role node -nodeConfig nodeconfig1.json
start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -Dwebdriver.edge.driver="msedgedriver.exe" -jar selenium-server-4.21.0.jar standalone -role node -nodeConfig nodeconfig2.json
start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -Dwebdriver.edge.driver="msedgedriver.exe" -jar selenium-server-4.21.0.jar standalone -role node -nodeConfig nodeconfig3.json
start java -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -Dwebdriver.edge.driver="msedgedriver.exe" -jar selenium-server-4.21.0.jar standalone -role node -nodeConfig nodeconfig4.json
