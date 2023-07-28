import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

class uso_unittest(unittest.TestCase):

    def setUp(self):      
        service = Service(executable_path='c:\cdDriver\chromedriver')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(5)
        driver.execute_script("window.open('');")
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://stackoverflow.com")
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        driver.get("https://www.youtube.com/")
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()