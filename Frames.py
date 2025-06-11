import time
from itertools import count

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(3)

actions = ActionChains(driver)
actions.click(driver.find_element(By.CSS_SELECTOR,'div[aria-label="Close"]')).perform()

driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.ID,'tinymce').click()
driver.find_element(By.ID,'tinymce').send_keys("iam able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,'h3').text)





