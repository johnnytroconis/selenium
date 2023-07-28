from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='c:\cdDriver\chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://google.com")

title = driver.title

assert title == "Google"

driver.implicitly_wait(15.5)

search_box = driver.find_element(by=By.NAME,value="q")

search_botton = driver.find_element(by=By.NAME,value="btnK")

search_box.send_keys("Selenium")
search_botton.click()

search_box = driver.find_element(by=By.NAME, value="q")
value = search_box.get_attribute("value")
assert value == "Selenium"


driver.quit()