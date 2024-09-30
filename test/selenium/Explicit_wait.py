from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriver, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Open Menu']").click()

element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='logout_sidebar_link']")))
element.click()

driver.quit()


# EXPLICIT WAIT
# The syntax for explicit waits in Selenium Python involves two main parts:
#
# Creating a WebDriverWait object
# from selenium.webdriver.support.ui import WebDriver Wait
#
# wait WebDriver Wait(driver, timeout)
#
# Using Expected Conditions
#
# from selenium.webdriver.support import expected_conditions as EC
#
# Element walt.until(EC.presence_of_element_located((By.ID, "my_element_id")))