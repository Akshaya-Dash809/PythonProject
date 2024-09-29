from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)
browser.maximize_window()
# select the alert bottom and click
Alert_btn= browser.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
Alert_btn.click()
sleep(2)
# handle the alert box and print the text inside it
alert= browser.switch_to.alert
alert_Text= alert.text
print(alert_Text)
sleep(2)
# click ok from the alert message by using accept()
alert.accept()
sleep(3)

confirm_btm=browser.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
confirm_btm.click()
confirm=browser.switch_to.alert
confirm_txt=confirm.text
print(confirm_txt)
sleep(2)
alert.dismiss()
sleep(2)
# Click on prompt bottom and write some message in alert page and click ok by accept
prompt_btm= browser.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
prompt_btm.click()
prompt=browser.switch_to.alert
alert.send_keys("Hii Akshaya")
sleep(2)
alert.accept()
sleep(2)