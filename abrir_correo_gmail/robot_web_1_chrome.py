from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path='c:\cdDriver\chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://gmail.com")
#driver.implicitly_wait(15.5)

#Identificar Elementos a utilizar




#usar los Elementos seleccionados

#USUARIO
usuario = driver.find_element(by=By.ID ,value="identifierId")
usuario.send_keys("ALEXANDERTRC2020@GMAIL.COM")
usuario.send_keys(Keys.ENTER)
time.sleep(15)

#CLAVE
clave = driver.find_element(by=By.NAME , value="Passwd")
clave.send_keys("updf2018")
clave.send_keys(Keys.ENTER)


#driver.quit()