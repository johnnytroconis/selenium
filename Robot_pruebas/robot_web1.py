import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service


class usando_unittest(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path='c:\cdChrome\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)

    def test_usando_Explicit_wait(self):
        driver = self.driver
        driver.get("https://www.google.com")
        try:
            element = WebDriverWait(driver, 100).until(ec.presence_of_all_elements_located((By.NAME, "q")))
        finally:
            driver.quit()

if __name__ == '__main__':
    unittest.main()

    