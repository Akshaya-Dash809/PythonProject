from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# config driver and get web page
driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/auth/login")
driver.maximize_window()
sleep(3)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"))
).click()
sleep(4)
driver.back()
sleep(4)
driver.forward()
sleep(4)
driver.refresh()
sleep(4)
driver.close()
driver.quit()

