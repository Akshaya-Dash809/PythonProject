import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set URL
driver = webdriver.Firefox()
url = 'https://jqueryui.com/'
driver.get(url)

#Find links available in a webpage
all_links = driver.find_elements(By.TAG_NAME, 'a' )
print(f'There are {len(all_links)} links found in the page')

# Find out broken links by http response
for link in all_links:
    href = link.get_attribute('href')
    response =requests.get(href)
    if response.status_code >= 400:
        print(f"Broken link : {href}(Status code : {response.status_code})")

driver.quit()