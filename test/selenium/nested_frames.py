from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# set browser url and get web page
browser = webdriver.Firefox()
url= 'https://the-internet.herokuapp.com/nested_frames'
browser.get(url)

# switch to top frame
browser.switch_to.frame('frame-top')
sleep(2)


# switch to middle frame
browser.switch_to.frame("frame-middle")
# check the content of middle frame
content= browser.find_element(By.ID,'content').text
print('Content of middle frame :',content)

# Switch to default content or back from current frame
browser.switch_to.default_content()

# switch to bottom frame
browser.switch_to.frame('frame-bottom')
# Print the content of bottom frame
content_btm= browser.find_element(By.TAG_NAME,'body').text
print('Content of bottom frame :',content_btm)