import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(5)

driver.find_element(By.LINK_TEXT,"Forgot password?").click() #by using Link Text, text should have link attached to it
driver.find_element(By.XPATH, "//form/div/input").send_keys("Hello@gmail.com")#xpath
#driver.find_element(By.CSS_SELECTOR,"form div;nth-child(2) input").send_keys("Test1234")#css
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("Test1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Test1234")#css id
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click() #xpath used text on a button

time.sleep(5) 