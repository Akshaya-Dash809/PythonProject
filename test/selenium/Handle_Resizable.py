from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
url = "https://demo.automationtesting.in/Resizable.html"
browser.get(url)

resizable_element = browser.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
initial_elements_size = browser.find_element(By.XPATH, "//div[@id='resizable']")
initial_size = initial_elements_size.size
print("Initial Size : ",initial_size)
sleep(3)
action_chain = ActionChains(browser)
action_chain.click_and_hold(resizable_element).move_by_offset(100,100).release().perform()
sleep(3)
resized_element= initial_elements_size.size
print("Resized Size : ",resized_element)
browser.quit()