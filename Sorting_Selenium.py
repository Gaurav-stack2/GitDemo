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

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#Click on the column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#collect all vegetables names-> BrowserSortedveggieList(A,B,C)
#CSS to write in console to verify the CSS - $$('tr td:nth-child(1)')
#Xpath to write in console to verify the Xpath - $x("//tr/td[1]")
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()#to make a copy of the browsersorted list before sorting it using our code

#Sort this veggielist=> newSortedList ->(A,B,C)
browserSortedVeggies.sort()

#BrowserSortedveggieList = newSortedlist
assert browserSortedVeggies == originalBrowserSortedList
time.sleep(3)

#Test scenario is if browser is returning the sorted list then it should match our sorted list, but if browser is not returning the
#sorted list then on assertion it should fail as it will not match with our sorted list

