import time
from itertools import count
browserSortedVeggies = []
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--ignore-certificate-errors")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized') #it will start in maximized mode even before invoking the browser
#chrome_options.add_argument('--headless')#it will do all actions without showing the browser in the frontend
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-gpu')


driver = webdriver.Chrome(options=chrome_options)
#driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/angularpractice")
time.sleep(2)

print(driver.title)