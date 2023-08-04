import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class usando_unittest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path='c:\cdDriver\chromedriver')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches",['enable-automation'])
        self.driver = webdriver.Chrome(service=service, options=options)

    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.google.com")
        myDynamicElement = driver.find_element(By.NAME,"q")
    
if __name__ == '__main__':
    unittest.main()