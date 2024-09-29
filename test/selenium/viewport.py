import time
from time import sleep

from selenium import webdriver
# store a set of views in view variable
view = [(300,200),(500,400),(600,500),(700,600),(800,700)]
# Set the url in driver and get webpage
driver = webdriver.Firefox()
driver.get('https://google.com')
# Iterate all views from view set one by one
try :
    for width,height in view:
        driver.set_window_size(width,height)
        time.sleep(2)

finally:
    driver.quit()

