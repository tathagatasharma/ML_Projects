#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:25:25 2023

@author: tathagatasharma
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


driver = webdriver.Chrome('/Users/tathagatasharma/Documents/chrome_driver/chromedriver')
driver.get('https://www.nike.com/in/w/sale-3yaep')

last_page_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_page_height = driver.execute_script('return document.body.scrollHeight')
    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height
    
    
soup = BeautifulSoup(driver.page_source,'lxml')

product_card = soup.find_all('div', class_='product-card__body')

df = pd.DataFrame({'Link':[''],'Name':[''],'Subtitle':[''],'Full Price':[''],'Sale Price':['']})

for product in product_card:
    try:
        link = product.find('a',class_= 'product-card__link-overlay').get('href')
        name = product.find('div', class_ = 'product-card__title').text.strip()
        subtitle = product.find('div',class_ = 'product-card__subtitle').text.strip()
        full_price = product.find('div',class_ = 'product-price in__styling is--striked-out css-0').text.strip()
        sale_price = product.find('div',class_ = 'product-price is--current-price css-1ydfahe').text.strip()
        df = df.append({'Link':link,'Name':name,'Subtitle':subtitle,
                        'Full Price':full_price,'Sale Price':sale_price},ignore_index=True)
    except:
        pass
    
    
df.to_csv('/Users/tathagatasharma/Documents/Infinite_scrolling_project_1.csv')