from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='c:\cdDriver\chromedriver')
options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches",['enable-automation'])

driver = webdriver.Chrome(service=service, options=options)

driver.get("file:///C:/Proyecto/FormulariosHTML/login.html")

time.sleep(5)

with open('C:\Proyecto\FormulariosHTML\datos.txt', 'r') as file:
    for i, line in enumerate(file):
        usuario = (line)
        sep = ','
        dividir = usuario.split(sep)
        try:
            gotdata = dividir[1]
            user = dividir[0]
            pas = dividir[1]
        except IndexError:
            gotdata='null'
        driver.find_element(by=By.ID, value="login").send_keys(user)
        time.sleep(2)
        driver.find_element(by=By.ID, value="pass").send_keys(pas)
        time.sleep(2)
        driver.find_element(by=By.ID, value="acceso").click()
        time.sleep(5)

file.close()
driver.quit()