#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:38:09 2023

@author: tathagatasharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time



driver = webdriver.Chrome('/Users/tathagatasharma/Documents/chrome_driver/chromedriver')

driver.get('https://twitter.com/login?lang=en')

time.sleep(10)

#login = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label')
                                     #//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label
                                     #/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label
#login = driver.find_element(By., '/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label')
#login.send_keys('bot_scrapping')

#username = driver.find_element(By.XPATH, "//input[@autocomplete='username']" )
username = driver.find_element(By.XPATH, "//input[contains(@autocomplete,'username')]" )
# enter your username and password
username.send_keys("bot_scrapping")


login_button = driver.find_elements(By.XPATH, "//*[contains(@class, 'r-qvutc0') and contains(@style,'color: rgb(15, 20, 25);')]")[1]

#login_button = driver.find_element('xpath','//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]/div')
login_button.click()

time.sleep(4)

password = driver.find_element('xpath', "//input[contains(@autocomplete,'current-password')]" )
password.send_keys('thisisabot')

#password = driver.find_element_by_name("session[password]")
#password.send_keys("your_password")

login_button_2 = driver.find_element(By.XPATH, "//*[contains(@data-testid,'LoginForm_Login_Button')]")

#login_button_2 = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div')
#//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div/div/div
login_button_2.click()


time.sleep(5)

celebrity = 'Alia Bhatt'

search = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')

search.send_keys(celebrity)
search.send_keys(Keys.RETURN)

time.sleep(2)

people_tab = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div/span')

people_tab.click()

time.sleep(2)

Result = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span')

Result.click()


time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'lxml')

postings = soup.find_all('div', class_ = 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')


tweet = []

while True:
    for post in postings:
        tweet.append(post.text)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_ = 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    tweets2 = list(set(tweet))
    if len(tweets2)>100:
        break


tweet_new = []
for i in tweets2:
    if 'Abhishek' in i:
        tweet_new.append(i)
        



