from selenium import webdriver


username = "admin"
password = "admin"
driver = webdriver.Firefox()
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
driver.get(url)

# The pattern of auth. to a browser is written below
#https://username:password@domain/path