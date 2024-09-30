from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/horizontal_slider"
browser.get(url)

slider = browser.find_element(By.XPATH, "//input[@type='range']")
action = ActionChains(browser)
# Here using "move_by_offset" because we are sliding horizontal. here X-axis for horizontal and Y-axis for vertical
action.click_and_hold(slider).move_by_offset(50,0).release().perform()
sleep(5)
browser.quit()