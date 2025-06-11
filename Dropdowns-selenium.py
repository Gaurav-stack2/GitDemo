import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome() #driver is basicallhy the object of the Chrome class
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
message = driver.title
print(message)
print(driver.current_url)

time.sleep(5)
#Static Dropdown from practise sites

dropdown = Select(driver.find_element(By.ID,"dropdown-class-example"))
dropdown.select_by_index(2)  #if we see select tag for the element then use this select tag
dropdown.select_by_visible_text("Option1")
