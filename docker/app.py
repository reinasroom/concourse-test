import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TestPythonOrgTest(object):
    def setup_method(self):
        options = Options()
        options.binary_location = '/app/chrome-linux64/chrome'
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        chrome_driver_path='/app/chromedriver-linux64/chromedriver'
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def test_python_org(self):
        self.driver.get('https://www.google.com/')

        self.driver.maximize_window()

        self.driver.find_element(By.NAME,"q").send_keys("セキセイインコ")
        self.driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)

        time.sleep(2)

        assert self.driver.title == "セキセイインコ - Google 検索"

    def teardown_method(self):
        self.driver.close()
