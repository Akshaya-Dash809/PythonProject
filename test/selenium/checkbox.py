import time


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Firefox()
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
browser.maximize_window()
time.sleep(3)



# checkbox = driver.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click()   # click the check box of Sunday
# time.sleep(3)
# checkbox2 = driver.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click()  # Unclick the check box Sunday
# time.sleep(3)
browser.execute_script("window.scrollBy(0, document.body.scrollHeight);")  # scroll the web page
checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")  # store Xpath of checkbox
for checkbox in checkboxes:     # Iterate each check box
    checkbox.send_keys(Keys.SPACE)  # Make checkbox unchecked by send keys as SPACE

checked_count =0
for checkbox in checkboxes:        # Iterate each check box
     if checkbox.is_selected:      # check the checkbox if selected
         checked_count+=1          # if selected then increase checked_count value by 1

expected_checked_count=7           # Expected check boxes to be checked

if checked_count == expected_checked_count:    # check the checked_count & expected_checked_count values are equal or not
    print('checked count verified')            # If equal then print statement verified
else:
    print('checked count mismatches')          # If not equal then mismatches
time.sleep(3)

browser.quit()