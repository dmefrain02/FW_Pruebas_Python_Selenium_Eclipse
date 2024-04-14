import allure
import os
import time

from allure import attachment_type
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriverSetup:

    def get_chrome_driver():
        options = Options()
        options.add_argument("start-maximized")  # Opens browser in maximized mode
        options.add_argument("disable-infobars")  # Disables info bars
        options.add_argument("--disable-gpu")  # Applicable to windows os only
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        options.add_argument("--no-sandbox")  # Bypass os security model
        options.add_argument("--headless")  # Start in headless mode
        options.add_argument("--ignore-certificate-errors") # To ignore errors related to certificate installation
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return driver

    def take_screenshot(driver):
        time.sleep(1)
        file_prefix = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0].strip('[]')
        now = datetime.now()
        print("now =", now)
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        file_name = f'{dt_string}.png'.replace("/", "_").replace("::", "__")
        image_path = f"{file_prefix}{file_name}"
        allure.attach(driver.get_screenshot_as_png(), name=image_path, attachment_type=attachment_type.PNG)
