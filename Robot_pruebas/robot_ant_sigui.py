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
        time.sleep(3)
        driver.get("https://www.gmail.com")
        time.sleep(3)
        driver.get("https://www.youtube.com")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()