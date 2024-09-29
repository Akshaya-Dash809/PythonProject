from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# set the driver by URL and get the web page
browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/iframe')
# From web page to switch frame of that page
frame = browser.find_element(By.ID,'mce_0_ifr')
browser.switch_to.frame(frame)

# click that frame and edit the text and sed your customize text
text_Editor = browser.find_element(By.ID,'tinymce')
text_Editor.send_keys('Hii This is AKD')
sleep(3)

# Switch or Back to the page from frame
browser.switch_to.default_content()
outside_link = browser.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']")
outside_link.click()
