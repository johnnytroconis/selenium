import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class uso_unittest(unittest.TestCase):

    def setUp(self):      
        service = Service(executable_path='c:\cdDriver\chromedriver')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def test_usando_hover_action(self):
        driver = self.driver
        driver.get("https://google.com")
        time.sleep(3)
        elem = driver.find_element(by=By.LINK_TEXT, value="Privacidad")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform() 
        time.sleep(3)
        elem.click()

if __name__ == '__main__':
    unittest.main()