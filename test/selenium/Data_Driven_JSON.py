from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

with open('Testdata_python_json.json','r') as file:
    test_data = json.load(file)

for data in test_data['users']:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/")
    sleep(3)
    driver.find_element(By.ID,"user-name").send_keys(data['username'])
    driver.find_element(By.ID,"password").send_keys(data['password'])
    sleep(3)
    driver.find_element(By.ID,"login-button").click()
    sleep(3)

    sleep(3)
    driver.quit()
