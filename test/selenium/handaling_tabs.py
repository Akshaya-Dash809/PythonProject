from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# config 1st web page and get that page
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.selenium.dev/")
sleep(3)
# Switch to another web page / another tab
driver.switch_to.new_window()
driver.get("https://playwright.dev/")
sleep(3)
# Find the no of tab opens
number_of_tabs = len(driver.window_handles)
print(number_of_tabs)
tab_value = driver.window_handles
print(tab_value)
# config current tab
current_tab = driver.current_window_handle.title()
print(current_tab)
driver.find_element(By.CSS_SELECTOR,'.getStarted_Sjon').click()

# config switch from current tab to 1st tab, if 1st tab not open
first_tab = driver.window_handles[0]
if current_tab != first_tab:
    driver.switch_to.window(first_tab)
    driver.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()
driver.quit()