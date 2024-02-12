# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# import undetected_chromedriver as uc
# import pandas as pd
import time
# import re
# import csv
# from datetime import datetime
# from datetime import date
from seleniumbase import Driver

driver = Driver(uc=True)
driver.maximize_window()
url = 'https://www.oreilly.com/member/login/'
driver.get(url)

time.sleep(5)

# email input
userEmail = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div[1]/section/section/form/div/label/input')
userEmail.send_keys("chariesdevstar@gmail.com")

emailButt = driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/section/section/form/button')
emailButt.click()

time.sleep(1)

# password input
userPass = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div[1]/section/section/section/form/div[1]/div/label/input')
userPass.send_keys("Devstar@0212")

submitButt = driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/section/section/section/form/div[3]/button')
submitButt.click()

time.sleep(1)

driver.get('https://learning.oreilly.com/library/view/clean-code-a/9780136083238/chapter07.xhtml#ch7lev1sec10')

totalText = driver.find_element(By.ID, 'sbo-rt-content')

# Find all elements inside the parent element
child_elements = totalText.find_elements(By.XPATH, ".//*")

# Iterate over the child elements
for element in child_elements:
    # Do something with each child element
    print(element.tag_name)
    print(element.text)
# print(totalText)



# while True:
#     pass
driver.close()
