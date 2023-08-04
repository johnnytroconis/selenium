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
    
    def test_scrooldown(self):
        driver = self.driver
        driver.get("https://www.amazon.com.mx/")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()