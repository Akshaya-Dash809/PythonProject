import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the url and get the web page
driver = webdriver.Firefox()
url = 'https://the-internet.herokuapp.com/broken_images'
driver.get(url)
driver.maximize_window()
# find all images in that web page
all_images = driver.find_elements(By.TAG_NAME, 'img' )
broken_images = []

# Iterate all images to find broken images by using if condition
for img in all_images:
    src = img.get_attribute('src')
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print("broken image found")
if broken_images:
    print("List of broken images")
    for broken_img in broken_images:
        print(broken_img)
else:
    print("No broken images found")


driver.quit()