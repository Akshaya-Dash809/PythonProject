from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://www.saucedemo.com/v1/")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Open Menu']").click()
driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()

driver.quit()


# IMPLICIT WAIT
#
# Selenium has a built-in way to automatically wait for elements called an implicit wait.
# An implicit wait value can be set either with the timeouts capability in the browser options, or with a driver method
# This is a global setting that applies to every element location call for the entire session.
# The default value is 0, which means that if the element is not found, it will immediately return an error.
# If an implicit wait is set, the driver will wait for the duration of the provided value before returning the error




