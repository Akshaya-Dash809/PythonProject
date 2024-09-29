from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# Set browser and get webpage
browser = webdriver.Firefox()
url ="https://the-internet.herokuapp.com/drag_and_drop"
browser.get(url)
# find source and destination elements
source_element = browser.find_element(By.ID,"column-a")
destination_element = browser.find_element(By.ID,"column-b")
# Us eActionChains class from selenium-webdriver  to perform the drop_and-drag operation
actions= ActionChains(browser)
actions.drag_and_drop(source_element,destination_element).perform()
sleep(3)
browser.quit()