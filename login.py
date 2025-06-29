
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# import pandas as pd

# def read_data_from_file(file_path):
#     data = {}
#     with open(file_path, 'r') as file:
#         for line in file:
#             key, value = line.strip().split(':')
#             data[key] = value
#     return data
# data =pd.read_data_from_file('C:\\Users\\vglug\\Documents\\Abii\\signup txt files\\dataa.xlsx')

# email = data['email']
# password = data['password']
# companyname = data['companyname']
# site = data['site']
# mobilenumber = data['mobilenumber']


# driver=webdriver.Chrome() 
# driver.get(f"https://dash.sagasoft.io/sagasuite/signup")
# time.sleep(5)


# email_input = driver.find_element(By.ID, "email")  
# email_input.send_keys(email)
# time.sleep(2)

# password_input = driver.find_element(By.ID,"password" )   
# password_input.send_keys(password)
# time.sleep(2)

# company_input = driver.find_element(By.ID, "company")  
# company_input.send_keys(companyname)
# time.sleep(2)

# site_input = driver.find_element(By.ID,"sitevalue")
# site_input.send_keys(site)
# time.sleep(2) 

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup driver
driver = webdriver.Chrome()  # Or Firefox(), Edge(), etc.
driver.get("https://www.google.com")

# Find search box and enter text
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()
