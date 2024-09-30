from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://demo.automationtesting.in/Register.html")

# Two ways to  take screenshot of a web page
driver.save_screenshot("screenshot.png")
driver.get_screenshot_as_file("screenshot.png")
driver.quit()