from datetime import datetime, timedelta
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Set webdriver, get web page
browser=webdriver.Firefox()
url="https://demo.automationtesting.in/Datepicker.html"
browser.get(url)
# identify datepicker and click it
browser.find_element(By.ID,'datepicker2').click()
# Current date
current_date = datetime.now()
print(current_date)
# Next day
next_day = current_date + timedelta(days=1)
print(next_day)
next__day = str(next_day.day)
print(next__day)
current_month = datetime.now().month
current_year = current_date.year

next_month = (current_month % 12) +1
# Format of month and year Ex- 03/2024
next_month_year = f"{next_month}/{current_year}"
# Identify and Select mont dropdown
month_dropdown = browser.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select = Select(month_dropdown)
select.select_by_value(str(next_month_year))
# Identify and Select mont dropdown
year_dropdown = browser.find_element(By.CSS_SELECTOR,"select[title='Change the year']")
select= Select(year_dropdown)
select.select_by_visible_text("2024")
# Select a date from date picker
browser.find_element(By.LINK_TEXT,next__day).click()

sleep(3)

