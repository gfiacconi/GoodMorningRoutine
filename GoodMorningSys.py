from pathlib import Path
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyttsx3
from playsound import playsound
from threading import Thread
from multiprocessing import Process
import sys 

driverpath = '/Users/gabrielefiacconi/chromedriver/chromedriver 2'
name = sys.argv[1]

#read the file txt and cancel '.txt' every time
def read_file():
        with open('all.txt') as f:
                for line in f:
                        line = line.strip()
                        line = line.replace('.txt', '')
                        print(line)

    
def speak(text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 300)
        engine.say(text)
        engine.runAndWait()
        
def open_browser():
    driver = webdriver.Chrome(driverpath)
    driver.maximize_window()

    driver.get('https://www.ansa.it/')
    driver.execute_script("window.open('');")

    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.internazionale.it/")
    driver.execute_script("window.open('');")

    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://www.ilsole24ore.com/?refresh_ce=1")

    driver.switch_to.window(driver.window_handles[0])
    sleep(100000)

def playMusic(music):
        playsound(music)

def alltogether():
        music = 'acdc.mp3'
        text = 'Good morning' + name + '! Here are the fucking Bullshit of today. Have a nice day!'
        p1 = Process(target=open_browser)
        p1.start()
        p2 = Process(target=speak(text))
        p2.start()
        p3 = Process(target=playMusic(music))
        p3.start()

        p1.join()
        p2.join()
        p3.join()
    
if __name__ == '__main__':
    try:
        alltogether()
       
    except Exception as e:
        print(e)
