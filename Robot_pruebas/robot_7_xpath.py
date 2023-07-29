import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        service = Service(executable_path='c:\cdDriver\chromedriver')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def test_buscar_x_xpath(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(5)
        buscar = driver.find_element(by=By.XPATH,value="//*[@id='APjFqb']")    
        time.sleep(3)
        buscar.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(3)
        buscar.send_keys(Keys.ARROW_DOWN)
        buscar.send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        buscar.send_keys(Keys.ENTER)
        time.sleep(3)
        
        


if __name__ == '__main__':
    unittest.main()

 # //*[@id='APjFqb']
#  //*[@id="tsf"]/div[1]/div[1]/div[1]/div[1]/div/input
    #    /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea