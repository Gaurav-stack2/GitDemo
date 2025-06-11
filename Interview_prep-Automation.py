import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,'textarea[class^="gLFyf"]').send_keys("hi selenium")
time.sleep(2)

