# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://www.google.com/search?q=virat+kohli&sca_esv=620c24330b4497e4&sca_upv=1&source=hp&ei=QjPhZoGgM7ns1e8PjtLFwQ8&iflsig=AL9hbdgAAAAAZuFBUrd_EBudLGHxrc3Wwp5vxQWeazH-&gs_ssp=eJzj4tLP1TcwLswuq0wzYPTiLsssSixRyM7PyMkEAGaQCFc&oq=vi&gs_lp=Egdnd3Mtd2l6IgJ2aSoCCAIyDhAuGIAEGLEDGIMBGIoFMggQABiABBixAzIIEC4YgAQYsQMyCxAuGIAEGLEDGIMBMgsQLhiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMg4QABiABBixAxiDARiKBTIOEC4YgAQYsQMYgwEYigUyDhAuGIAEGLEDGIMBGOUESJ7oA1DVzANY8MwDcAN4AJABAJgBmAGgAaYCqgEDMC4yuAEByAEA-AEBmAIFoAKMA6gCCsICEhAAGAMY5QIY6gIYChiMAxiPAcICEBAuGAMY5QIY6gIYjAMYjwHCAhAQABgDGOUCGOoCGIwDGI8BmAMUkgcDMy4yoAftHw&sclient=gws-wiz')
# browser.get("https://www.google.com/search?q=anushka+sharma&sca_esv=620c24330b4497e4&sca_upv=1&ei=qzThZveDIMD21e8Pzrie8Qw&gs_ssp=eJzj4tLP1TcwyUlPNjYxYPTiS8wrLc7ITlQozkgsyk0EAHaoCPE&oq=anu&gs_lp=Egxnd3Mtd2l6LXNlcnAiA2FudSoCCAAyDRAuGIAEGLEDGEMYigUyChAuGIAEGEMYigUyChAAGIAEGEMYigUyEBAuGIAEGLEDGEMYgwEYigUyDRAAGIAEGLEDGEMYigUyCBAuGIAEGLEDMgUQLhiABDIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTILEC4YgAQYsQMYgwEyHBAuGIAEGLEDGEMYigUYlwUY3AQY3gQY3wTYAQJI4ihQpxRY3BtwAXgBkAEAmAGJAaABhwOqAQMwLjO4AQHIAQD4AQGYAgWgAvwPqAIKwgIQEC4YAxi0AhjqAhiPAdgBAcICEBAAGAMYtAIY6gIYjwHYAQHCAhkQLhiABBhDGIoFGJcFGNwEGN4EGN8E2AECmAMxugYECAEYCroGBggCEAEYFJIHCTEuMS4yLjctMaAHyo0B&sclient=gws-wiz-serp")
# browser.minimize_window()
# title = browser.title
# print(title)
# assert "virat kohli - Google Search" in title
# print(browser.page_source)

#Browser call
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#Element & Locators
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.minimize_window()
title = driver.title
print(title)
assert title == "OrangeHRM"



