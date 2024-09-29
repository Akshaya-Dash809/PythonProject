from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the url in driver and get web page
driver=webdriver.Firefox()
driver.get('https://cosmocode.io/automation-practice-webtable/')
driver.maximize_window()
# Scroll down the web page
driver.execute_script("window.scrollTo(0, 700);")
sleep(3)
# set the path of table and rows
table = driver.find_element(By.ID,'countries')
rows = driver.find_elements(By.TAG_NAME,'tr')
# find  all rows present in the table by len() function
row_count = len(rows)
print(row_count)
# Find the target value by iterate all rows of the table
target_value = 'Austria'
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME,'td')
    for cell in cells:
        if target_value in cell.text:
            print(f'found value {target_value}')
            found = True
            break
    if found:
        break

if not found:
    print(f'Target value {target_value} not found')

driver.close()