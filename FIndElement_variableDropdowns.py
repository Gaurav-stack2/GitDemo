import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID,'autosuggest').send_keys('Ind')
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,'li[class="ui-menu-item"] a')#CSS selector needs space to go from parent to child tags
print(len(countries))

for country in countries:
   if country.text == 'India': # we used text as its given the inspect element
       country.click()
       break

#print(driver.fin_element(By.ID,'autosuggest').text)#.text will not work as the value for india is dynamically updated through script, so we use .get_attribute('value')
print(driver.find_element(By.ID,'autosuggest').get_attribute('value'))
assert driver.find_element(By.ID,'autosuggest').get_attribute('value') == 'basIndia' #assert will give only if condition is false, if true nothing id displayed.
