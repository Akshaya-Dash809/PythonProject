from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.youtube.com/watch?v=iAIBF2ngbWY')
sleep(3)