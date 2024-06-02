start java -jar selenium-server-standalone-3.5.3.jar -role hub -hubconfig hubconfig.json

start java -jar -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -jar selenium-server-standalone-3.5.3.jar -role node -id node_1 -nodeconfig nodeconfig1.json
start java -jar -Dwebdriver.chrome.driver="chromedriver.exe" -Dwebdriver.gecko.driver="geckodriver.exe" -jar selenium-server-standalone-3.5.3.jar -role node -id node_2 -nodeconfig nodeconfig2.json