import time

from selenium import webdriver
#chrome driver service- it intreprets all the commands given by webdriver and then invoke the chrome
#Selenium 160->160 checks the chrome driver version , it downloads it and perform the action
#Edge Driver
driver = webdriver.Chrome() #driver is basicallhy the object of the Chrome class
driver.get('http://google.com')
print(driver.page_source)
print(driver.title)
print(driver.current_url)





















time.sleep(2)