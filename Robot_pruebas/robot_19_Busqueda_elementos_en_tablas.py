from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='c:\cdDriver\geckodriver')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(5)

valor = driver.find_element(by=By.XPATH, value="//*[@id='customers']/tbody/tr[2]/td[2]")

print(valor)

rows=len(driver.find_elements(by=By.XPATH, value="//*[@id='customers']/tbody/tr"))
	 
cols=len(driver.find_elements(by=By.XPATH, value="//*[@id='customers']/tbody/tr[1]/th"))

print(rows)
print(cols)

for n in range(2,rows+1):
	for b in range(1,cols+1):
		dato=driver.find_element(by=By.XPATH, value="//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text      
		print(dato, end=' - ')
	print(" ")
	
driver.close()