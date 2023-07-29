import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        service = Service(executable_path='c:\cdDriver\chromedriver')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def test_Explicit_wait(self):
        driver  = self.driver
        driver.get("https://www.youtube.com")
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'contents')))
        finally:
            driver.quit()

if __name__ == '__main__':
    unittest.main()