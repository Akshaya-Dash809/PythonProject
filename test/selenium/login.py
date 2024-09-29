# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Firefox()
# driver.maximize_window()
#
# username = "standard_user"
# password = "secret_sauce"
#
# login_url = "https://www.saucedemo.com/v1/"
# driver.get(login_url)
#
# username_field = driver.find_element(By.ID, "user-name")
# password_field = driver.find_element(By.ID, "password")
#
# username_field.send_keys(username)
# password_field.send_keys(password)
#
# login_button = driver.find_element(By.ID, "login-button")
# sleep(7)
# login_button.click()
# sleep(10)
# driver.close()
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() # store firefox webdriver in driver
driver.maximize_window() # maximize the browser/window

login_url = "https://www.saucedemo.com/v1/"   #store the url of the browser which we want to test in a variable login_url
driver.get(login_url)  #call the url to open webpage

username= "standard_user"  # Store the username in a variable username as a key-value
password= "secret_sauce"   # Store the password in a variable password as a key-value

username_field = driver.find_element(By.NAME, "user-name") # store the field of username box in a variable username_field
password_field = driver.find_element(By.NAME, "password")  # store the field of password box in a variable password_field

username_field.send_keys(username)  # send the value of username in username_field as a key
password_field.send_keys(password)  # send the value of password in password_field as a key
sleep(6)

login_button=driver.find_element(By.ID, "login-button")   #  store the  login button in a variable login_button
assert not login_button.get_attribute("disabled")  # Check whether the login button should not disabled
login_button.click()  # login by using click() function

success_element = driver.find_element(By.CSS_SELECTOR,".product_label") # Store the css_selector of title  of the page after login i.e. Products
assert  success_element.text == "Products"  # Check the title page name is same as given string

sleep(6)
driver.close()




