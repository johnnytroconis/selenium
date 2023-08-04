import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path='c:\cdChrome\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)

    def test_usando_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(3)
        radio_bt = driver.find_element(by=By.XPATH, value="//*[@id='main']/div[3]/div[1]/input[4]")
        radio_bt.click()
        time.sleep(3)
        radio_bt = driver.find_element(by=By.XPATH, value="//*[@id='main']/div[3]/div[1]/input[3]")
        radio_bt.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()