import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)#globally aplicabble for all the lines
#5 second is max time out, if got in 2 seconds,it will proceed further(3seconds save)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)

driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys('ber')
time.sleep(2)
results = driver.find_elements(By.XPATH,'//div[@class="products"]/div')
count = len(results)
assert count > 0 #put whenever necessary to test the scenarios as some products should be shown

for result in results:
    result.find_element(By.XPATH,'div/button').click() #this is chaining of webelemets in selenium where we dont give driver. as it scans the whole pae
    #we are using result. to start from above code only, chaining child to parent

driver.find_element(By.CSS_SELECTOR,'img[alt = "Cart"]').click()
driver.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]').click()
driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()
codeApplied = driver.find_element(By.CLASS_NAME,'promoInfo')
print(codeApplied.text)
assert "Code" in codeApplied

