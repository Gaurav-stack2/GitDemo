import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.maximize_window()
print(driver.title)
print(driver.current_url)

radioButton=driver.find_elements(By.CSS_SELECTOR,'.radioButton')#making it a class and assigning it to the object, for selecting class in CSS selector use .classname

radioButton[2].click()#then calling by the object
assert radioButton[2].is_selected()

radioButton1=driver.find_elements(By.CSS_SELECTOR,'input[name="radioButton"]')
print(len(radioButton1))

for radio in radioButton1:
    if radio.get_attribute('value') == 'radio3':
        radio.click()
        print(radio.is_selected())
        assert radio.is_selected()
        break


