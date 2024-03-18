import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

Driver = webdriver.Chrome()
Driver.get("https://duckduckgo.com/")

searchBar = Driver.find_element(By.ID, 'searchbox_input')
searchBar.send_keys("DuckDuck")
time.sleep(1)
searchBar.send_keys(Keys.ENTER)
time.sleep(1)
