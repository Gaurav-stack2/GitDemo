import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.maximize_window()
print(driver.title)
print(driver.current_url)


checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
print(len(checkboxes))


for checkbox in checkboxes: #above is the list of all checkboxes elements and we use for loop to reiterate till it matches our condition
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        time.sleep(1)
        print(checkbox.is_selected())
        assert checkbox.is_selected()
        break

