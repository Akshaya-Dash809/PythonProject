from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# Set the browser and get the webpage
browser = webdriver.Firefox()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)
# Mouse hover to the SwitchTo and click to the Frame option by using Action and Perform()
actions = ActionChains(browser)
hover_element=browser.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
actions.move_to_element(hover_element).perform()
sleep(3)
browser.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()

# Switch to the Iframe , then click to the txt box and enter your message
frame = browser.find_element(By.NAME,"SingleFrame")
browser.switch_to.frame(frame)
txt_box = browser.find_element(By.XPATH,"//input[@type='text']")
txt_box.send_keys("Hii Akshaya")
browser.quit()
