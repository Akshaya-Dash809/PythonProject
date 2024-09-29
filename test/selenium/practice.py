from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import keys_to_typing

# tuple = (3,4,5,6)
# sett = {32,32,3,43,31,'a',"hfg"}
# list = [232,32,42.31,3]
# dict = {1:"ak",2:"bk",3:'lk',4:'ck'}
#
# name = input("Enter your name: ")
# print(name)
# print(type(tuple))
# print(type(sett))
# print(type(list))
# print(type(dict))
#
# print(tuple)
# print(sett)
# print(list)
# print(dict)

driver=webdriver.Firefox()
driver.get('https://www.selenium.dev/')
sleep(3)
#        REFRESH
driver.get(driver.current_url)
sleep(3)
# driver.find_element(By.NAME("s")).send_keys(Keys.F5)
sleep(2)

#           CLOSE vs QUIT
# driver.switch_to.new_window()
# driver.get('https://www.google.com')
# driver.switch_to.new_window()
# driver.get('https://www.google.com')
# sleep(2)
# driver.close()
# sleep(2)
# driver.quit()




