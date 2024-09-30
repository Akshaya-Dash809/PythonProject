### Incognito mode for Chrome Browser

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# driver = webdriver.Chrome(options=chrome_options)
# sleep(3)
# driver.get("https://google.com/")


### Incognito mode for Firefox
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--private")
driver = webdriver.Chrome(options=firefox_options)
sleep(3)
driver.get("https://google.com/")





