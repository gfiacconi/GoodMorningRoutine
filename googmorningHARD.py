from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#create an input where i can put any website until i write FINISH and store in a list
list_of_websites = []
while True:
    website = input("Insert a website: ")
    if website == "FINISH":
        break
    list_of_websites.append(website)

#take this list of websites and open them in different tabs
driverpath = '/Users/gabrielefiacconi/chromedriver/chromedriver 2'
driver = webdriver.Chrome(driverpath)
for website in list_of_websites:
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(website)
    driver.execute_script("window.open('');")
    time.sleep(2)

