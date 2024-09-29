from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# config driver and get web page
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
driver.find_element(By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
sleep(4)
driver.back()
sleep(4)
driver.forward()
sleep(4)
driver.refresh()
sleep(4)
driver.close()


