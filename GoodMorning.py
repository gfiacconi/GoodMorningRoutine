from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driverpath = '/Users/gabrielefiacconi/chromedriver/chromedriver 2'
driver = webdriver.Chrome(driverpath)
driver.maximize_window()

driver.get('https://www.ansa.it/')
driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.internazionale.it/")
driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.ilsole24ore.com/?refresh_ce=1")
time.sleep(2)







