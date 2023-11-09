from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.get("https://hub.link/oFFZDYW")
delay = 15 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'ui-root')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
driver.close()
