import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #driver is basicallhy the object of the Chrome class
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
message = driver.title
print(message)
print(driver.current_url)

#Locators - ID,Xpath,CSSselector,classname,name,linktext
driver.find_element(By.CLASS_NAME,"theme-btn").click()
driver.find_element(By.ID,"name").send_keys("Hi Testing the name @#")
driver.find_element(By.ID,"email").send_keys("Hello@gmail.com")
driver.find_element(By.ID,"allowMarketingEmails").click()


#XPATH - //tagname[@attribute='value'] -> // button[@type='send code']
#driver.find_element(By.XPATH,'//button[@type="button"]').click()

#CSS - 'tagname[attribute = 'value']'
driver.find_element(By.CSS_SELECTOR,'button[type="button"]').click()
assert "Rahul" in message  #testing using text in the title using assert
time.sleep(10)
message1 = driver.find_element(By.CSS_SELECTOR,"#my-error-id").text ##id css
print(message1)

















time.sleep(10)