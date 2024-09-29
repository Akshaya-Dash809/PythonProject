
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown_element = driver.find_element(By.ID, "dropdown") # Store the id of dropdown box
#dropdown_element = Select(driver.find_element(By.XPATH, "//select"))

#select = Select(dropdown_element)     # Select from the dropdown box
#select.select_by_index(1)    # Select the value by index
#select.select_by_value("2")  # Select the value by value
#select.select_by_visible_text("Option 2")  # Select the value by visible text

target_value = "Option 3"
select = Select(dropdown_element)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
else:
        print(f"option '{target_value}' not found")






# How to interact with dropdown
# How to use select class
# How to use 3 different select methods (visible text,value,index)
# How to count the values
# Loop the dropdown value and if the desired value found select that value
